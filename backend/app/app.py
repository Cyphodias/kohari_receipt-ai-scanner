from fastapi import FastAPI, UploadFile
import shutil

from ocr import run_ocr
from parser import parse_receipt
from calculator import calculate_total

app = FastAPI()

@app.post("/scan")

async def scan_receipt(file: UploadFile):

    path = "uploads/" + file.filename

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = run_ocr(path)

    items = parse_receipt(text)

    total = calculate_total(items)

    return {
        "items": items,
        "total": total
    }
