from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from .models import extract_drug_info
from .drug_logic import check_interactions, get_dosage, suggest_alternatives
from .gemini_api import GeminiAPI

app = FastAPI()

class ExtractRequest(BaseModel):
    text: str

class InteractionRequest(BaseModel):
    drugs: list[str]

class DosageRequest(BaseModel):
    drug: str
    age: int

class AlternativeRequest(BaseModel):
    drug: str
    age: int

@app.post("/extract_drugs")
def extract_drugs(request: ExtractRequest):
    result = extract_drug_info(request.text)
    return {"extracted_info": result}

@app.post("/extract_text_from_image")
async def extract_text_from_image(file: UploadFile = File(...)):
    gemini = GeminiAPI(api_key="AIzaSyBgl-L1XzFr62P4L_XYAn1qcSVPhOoV-ms")
    image_data = await file.read()
    extracted_text = gemini.extract_text_from_image(image_data)
    if extracted_text:
        return {"extracted_text": extracted_text}
    else:
        return {"error": "Failed to extract text from image"}

@app.post("/check_interactions")
def check_interactions_endpoint(request: InteractionRequest):
    interactions = check_interactions(request.drugs)
    return {"interactions": interactions}

@app.post("/get_dosage")
def get_dosage_endpoint(request: DosageRequest):
    dosage = get_dosage(request.drug, request.age)
    return {"dosage": dosage}

@app.post("/suggest_alternatives")
def suggest_alternatives_endpoint(request: AlternativeRequest):
    alternatives = suggest_alternatives(request.drug, request.age)
    return {"alternatives": alternatives}
