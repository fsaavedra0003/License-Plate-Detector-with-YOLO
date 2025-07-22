import cv2
import psycopg2
from pathlib import Path
from datetime import datetime
from ultralytics import YOLO
from config import DB_CONFIG, MODEL_PATH

# Load YOLOv8 model
model = YOLO(MODEL_PATH)

# Connect to PostgreSQL
conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

# Ensure detected folder exists
Path("detected").mkdir(exist_ok=True)

def detect_and_store(image_path):
    image = cv2.imread(image_path)
    results = model(image)[0]

    for det in results.boxes.data:
        x1, y1, x2, y2, conf, cls = det.cpu().numpy()
        cropped = image[int(y1):int(y2), int(x1):int(x2)]

        timestamp = datetime.now()
        filename = f"plate_{timestamp.strftime('%Y%m%d_%H%M%S%f')}.jpg"
        save_path = f"detected/{filename}"
        cv2.imwrite(save_path, cropped)

        bbox_str = f"{int(x1)},{int(y1)},{int(x2)},{int(y2)}"
        cursor.execute(
            "INSERT INTO plates (timestamp, image_path, bbox) VALUES (%s, %s, %s)",
            (timestamp, save_path, bbox_str)
        )
        conn.commit()
        print(f"[✔] Saved plate to DB and {save_path}")

def main():
    for img_path in Path("images").glob("*.jpg"):
        detect_and_store(str(img_path))
    conn.close()

if __name__ == "__main__":
    main()
