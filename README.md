# 🚘 License Plate Detection with YOLOv8 and PostgreSQL

This project uses [YOLOv8](https://github.com/ultralytics/ultralytics) for automatic **license plate detection** from images and stores the detection metadata in a **PostgreSQL** database. Cropped images of the detected plates are saved locally.

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



