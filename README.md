# kohari_receipt-ai-scanner
# Receipt AI Scanner

AI-powered receipt scanner that extracts items and totals from photos.

Features:

• Android app (Flutter)
• OCR receipt detection
• Automatic item extraction
• Total calculation
• API backend
• AI receipt understanding

Architecture:

Android App → API → OCR → Parser → Database

-----------------------------------------------------------------------

Mobile App
   |
Upload Receipt
   |
Backend API
   |
Image Processing
   |
OCR Engine
   |
Receipt Parser
   |
Database

-------------------------------------------------------------------------

# Receipt AI Starter Repo

AI-powered receipt scanner starter project. Scans receipt images, extracts items and prices, and calculates the total amount.

---

## Repository Structure

```
receipt_ai_starter/
├── backend/
│   ├── app.py
│   ├── ocr.py
│   ├── parser.py
│   └── calculator.py
├── android_app/  (Flutter project placeholder)
├── dataset/
│   ├── images/
│   └── labels/
└── README.md
```

---

## Prerequisites

- Python 3.9+
- pip
- Tesseract OCR installed on your system
- Flutter SDK (for Android app)
- Android Studio (for Android APK build)

### Install Tesseract OCR

**Ubuntu/Debian:**
```bash
sudo apt install tesseract-ocr
```

**Windows:**
- Download from https://github.com/tesseract-ocr/tesseract
- Add installation path to system PATH

**macOS:**
```bash
brew install tesseract
```

---

## Backend Installation

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create an `uploads/` directory to store uploaded receipt images:
```bash
mkdir uploads
```

5. Run the backend server:
```bash
uvicorn app:app --reload
```
- The API will be available at `http://127.0.0.1:8000/scan`

---

## Using the Backend API

- Send a POST request with a receipt image to `/scan` endpoint.
- Example using `curl`:
```bash
curl -X POST "http://127.0.0.1:8000/scan" -F "file=@../dataset/images/receipt1.jpg"
```
- Response:
```json
{
  "items": [
    {"name": "Tusker Lager", "price": 350},
    {"name": "Beef Burger", "price": 900},
    {"name": "Soda", "price": 150}
  ],
  "total": 1400
}
```

---

## Flutter Android App

1. Navigate to the Flutter project directory:
```bash
cd android_app
```

2. Get dependencies:
```bash
flutter pub get
```

3. Connect your Flutter app to the backend `/scan` endpoint.

4. Build Android APK:
```bash
flutter build apk --release
```
- The APK will be located at `build/app/outputs/flutter-apk/app-release.apk`

---

## Dataset Structure

- `dataset/images/` : Store receipt images.
- `dataset/labels/` : Store corresponding JSON labels (optional for future AI training).

Example label format:
```json
{
  "items": [
    {"name": "Beer", "price": 350},
    {"name": "Wine", "price": 700}
  ],
  "total": 1050
}
```

---

## Next Steps / Future Improvements

- Integrate advanced AI models for better accuracy (LayoutLM, Donut)
- Image preprocessing with OpenCV (deskewing, contrast)
- Mobile app features: bill splitting, tax calculation, merchant recognition
- Database integration (PostgreSQL or SQLite) for storing receipts
- Dockerize backend for easy deployment

---

## License

GNU General Public License v2.0
