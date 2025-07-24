# 🚘 License Plate Detection with YOLOv8 and PostgreSQL

This project uses [YOLOv8](https://github.com/ultralytics/ultralytics) for automatic **license plate detection** from images and stores the detection metadata in a **PostgreSQL** database. Cropped images of the detected plates are saved locally.


-This project leverages YOLOv8, a state-of-the-art object detection model, to automatically detect and extract vehicle license plates from images. It is designed as a pipeline that performs the following steps:

-Object Detection: YOLOv8 is used to detect license plates within input images with high accuracy and speed.

-Image Cropping: Detected license plates are cropped from the original images and saved locally for further analysis or archiving.

-Metadata Storage: Detection results — including image filenames, bounding box coordinates, timestamps, and confidence scores — are stored in a PostgreSQL database for efficient querying and tracking.

-Scalable Architecture: The modular design allows integration with video streams, APIs, or edge devices (e.g., Raspberry Pi, Jetson Nano) for real-time detection scenarios.

-This project can be used in applications such as parking management systems, traffic monitoring, toll collection, and smart surveillance, where license plate recognition is essential.

---

## 📌 Features

- 🔍 Detects license plates in images using YOLOv8.
- 💾 Saves bounding box metadata and image paths in PostgreSQL.
- 🖼 Automatically crops and saves detected plate images.
- 🧱 Modular structure for easy extension (e.g. OCR, API endpoints).







---

## 🛠️ Requirements

- Python 3.8+
- PostgreSQL 13+
- YOLOv8 model (custom-trained or pretrained)


----
##🧾 Clone the Repository

git clone https://github.com/fsaavedra0003/license-plate-detector.git
cd license-plate-detector

Install dependencies:

```bash
pip install -r requirements.txt




## 📁 Project Structure

```bash
license-plate-detector/
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── config.py               # PostgreSQL & model config
├── detect_and_save.py      # Main detection & DB logic
├── db/
│   └── init.sql            # SQL script to initialize DB schema
├── detected/               # Saved cropped license plate images
├── images/                 # Input images for detection



