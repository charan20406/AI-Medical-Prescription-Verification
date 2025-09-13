# Mock drug database
drug_db = {
    "aspirin": {"interactions": ["warfarin"], "dosage": {"adult": "325mg", "child": "10mg/kg"}, "use": "Pain, fever, heart protection", "key_interactions": "Avoid with NSAIDs, anticoagulants; GI bleeding risk."},
    "warfarin": {"interactions": ["aspirin"], "dosage": {"adult": "5mg", "child": "not recommended"}, "use": "Anticoagulant", "key_interactions": "Many drug/food interactions (antibiotics, leafy greens)."},
    "ibuprofen": {"interactions": ["aspirin"], "dosage": {"adult": "200mg", "child": "5mg/kg"}, "use": "Pain, inflammation", "key_interactions": "Avoid with NSAIDs, ulcers, blood thinners."},
    "paracetamol": {"interactions": [], "dosage": {"adult": "500–1000 mg q6–8h (max 4g/day)", "child": "10–15 mg/kg q6–8h (max 60 mg/kg/day)"}, "use": "Pain, fever", "key_interactions": "Avoid alcohol, other paracetamol products (liver damage)."},
    "diclofenac": {"interactions": ["warfarin"], "dosage": {"adult": "50 mg 2–3× daily (max 150 mg/day)", "child": "Not usually given <14 yrs"}, "use": "Arthritis, pain", "key_interactions": "GI irritation, avoid with warfarin, other NSAIDs."},
    "amoxicillin": {"interactions": ["methotrexate"], "dosage": {"adult": "500 mg q8h or 875 mg q12h", "child": "25–50 mg/kg/day divided doses"}, "use": "Bacterial infections", "key_interactions": "May reduce contraceptive effect; avoid with methotrexate."},
    "azithromycin": {"interactions": [], "dosage": {"adult": "500 mg day 1, then 250 mg/day ×4 days", "child": "10 mg/kg day 1, then 5 mg/kg ×4 days"}, "use": "Respiratory infections", "key_interactions": "Avoid with QT-prolonging drugs, antacids."},
    "ciprofloxacin": {"interactions": ["warfarin"], "dosage": {"adult": "500–750 mg q12h", "child": "Avoid in <18 yrs (joint issues)"}, "use": "UTI, GI infections", "key_interactions": "Avoid with dairy, antacids, warfarin."},
    "metronidazole": {"interactions": [], "dosage": {"adult": "400–500 mg q8h", "child": "15 mg/kg q8h"}, "use": "Anaerobic infections, amoebiasis", "key_interactions": "Avoid alcohol (disulfiram-like reaction)."},
    "cetirizine": {"interactions": [], "dosage": {"adult": "10 mg daily", "child": "2.5–5 mg daily (2–6 yrs)"}, "use": "Allergies", "key_interactions": "Sedation ↑ with alcohol/antihistamines."},
    "loratadine": {"interactions": [], "dosage": {"adult": "10 mg daily", "child": "5 mg daily (2–12 yrs)"}, "use": "Allergies", "key_interactions": "Safer than cetirizine (less sedation)."},
    "montelukast": {"interactions": ["phenobarbital", "rifampin"], "dosage": {"adult": "10 mg at night", "child": "4–5 mg chewable (2–12 yrs)"}, "use": "Asthma, allergies", "key_interactions": "Avoid with phenobarbital, rifampin."},
    "salbutamol": {"interactions": ["beta-blockers"], "dosage": {"adult": "100–200 mcg inhaled q4–6h", "child": "100 mcg inhaled q4–6h"}, "use": "Asthma (inhaler)", "key_interactions": "Tremors, avoid with beta-blockers."},
    "prednisolone": {"interactions": [], "dosage": {"adult": "5–60 mg/day (tapered)", "child": "0.5–2 mg/kg/day"}, "use": "Inflammation, asthma", "key_interactions": "Long-term: osteoporosis, diabetes, immune suppression."},
    "metformin": {"interactions": [], "dosage": {"adult": "500–850 mg 1–2× daily (max 2g)", "child": "≥10 yrs: 500 mg once daily (titrate)"}, "use": "Type 2 diabetes", "key_interactions": "Avoid alcohol, caution in kidney disease."},
    "glibenclamide": {"interactions": ["beta-blockers"], "dosage": {"adult": "2.5–10 mg daily (max 20 mg)", "child": "Not recommended"}, "use": "Type 2 diabetes", "key_interactions": "Risk of hypoglycemia; interacts with beta-blockers."},
    "atorvastatin": {"interactions": [], "dosage": {"adult": "10–40 mg daily", "child": "≥10 yrs: 10 mg daily"}, "use": "High cholesterol", "key_interactions": "Avoid grapefruit juice; interacts with antifungals/antibiotics."},
    "losartan": {"interactions": ["potassium-sparing diuretics", "lithium"], "dosage": {"adult": "50 mg daily (max 100 mg)", "child": "≥6 yrs: 0.7 mg/kg/day (max 50 mg)"}, "use": "Hypertension", "key_interactions": "Avoid with potassium-sparing diuretics, lithium."},
    "amlodipine": {"interactions": [], "dosage": {"adult": "5–10 mg daily", "child": "≥6 yrs: 2.5–5 mg daily"}, "use": "Hypertension", "key_interactions": "Avoid with strong CYP3A4 inhibitors."},
    "enalapril": {"interactions": ["potassium supplements"], "dosage": {"adult": "5–20 mg daily", "child": "0.1 mg/kg daily (≥1 month)"}, "use": "Hypertension, heart failure", "key_interactions": "Avoid in pregnancy, with potassium supplements."},
    "furosemide": {"interactions": ["aminoglycosides"], "dosage": {"adult": "20–80 mg/day", "child": "1–2 mg/kg/dose (max 6 mg/kg/day)"}, "use": "Edema, hypertension", "key_interactions": "Risk of low potassium; avoid with aminoglycosides."},
    "omeprazole": {"interactions": ["iron", "b12", "clopidogrel"], "dosage": {"adult": "20–40 mg daily", "child": "0.7–3.3 mg/kg/day"}, "use": "GERD, ulcers", "key_interactions": "Reduces absorption of iron, B12, and clopidogrel efficacy."},
    "ranitidine": {"interactions": [], "dosage": {"adult": "150 mg 2× daily", "child": "2–4 mg/kg/dose q12h"}, "use": "Acid reflux", "key_interactions": "Withdrawn in many countries (NDMA impurity)."},
    "levothyroxine": {"interactions": ["iron", "calcium"], "dosage": {"adult": "25–150 mcg daily (adjusted)", "child": "10–15 mcg/kg/day (neonates)"}, "use": "Hypothyroidism", "key_interactions": "Avoid with iron, calcium; check TSH."},
    "insulin": {"interactions": ["beta-blockers"], "dosage": {"adult": "Individualized; often 0.5–1 U/kg/day", "child": "Same (weight-based)"}, "use": "Diabetes", "key_interactions": "Hypoglycemia if overdosed; interacts with beta-blockers."},
    "clopidogrel": {"interactions": ["omeprazole"], "dosage": {"adult": "75 mg daily", "child": "Not routine in kids"}, "use": "Antiplatelet", "key_interactions": "Interaction with omeprazole; bleeding risk."},
    "amiodarone": {"interactions": ["warfarin", "digoxin"], "dosage": {"adult": "200–400 mg daily", "child": "10–15 mg/kg/day loading"}, "use": "Arrhythmias", "key_interactions": "Interacts with warfarin, digoxin; thyroid/lung toxicity."},
    "sertraline": {"interactions": ["mao inhibitors"], "dosage": {"adult": "50–200 mg daily", "child": "Adolescents: 25–50 mg daily"}, "use": "Depression, anxiety", "key_interactions": "Avoid with MAOIs; serotonin syndrome risk."},
    "diazepam": {"interactions": ["alcohol", "opioids"], "dosage": {"adult": "2–10 mg up to 3× daily", "child": "0.2–0.5 mg/kg/day"}, "use": "Anxiety, seizures, muscle spasm", "key_interactions": "Sedation ↑ with alcohol, opioids."},
    "morphine": {"interactions": ["sedatives"], "dosage": {"adult": "5–30 mg q4h (oral)", "child": "0.1–0.2 mg/kg q4h"}, "use": "Severe pain", "key_interactions": "High abuse potential; interacts with sedatives."},
}

from .gemini_api import GeminiAPI

gemini = GeminiAPI(api_key="AIzaSyBgl-L1XzFr62P4L_XYAn1qcSVPhOoV-ms")

def check_interactions(drugs):
    interactions = []
    for i in range(len(drugs)):
        for j in range(i+1, len(drugs)):
            drug1 = drugs[i].lower()
            drug2 = drugs[j].lower()
            if drug1 in drug_db and drug2 in drug_db[drug1]["interactions"]:
                interactions.append(f"{drug1} interacts with {drug2}")
            elif drug1 not in drug_db or drug2 not in drug_db:
                # Query Gemini API if drug not found locally
                gemini_result1 = gemini.query_drug(drug1) if drug1 not in drug_db else None
                gemini_result2 = gemini.query_drug(drug2) if drug2 not in drug_db else None
                # Basic interaction check logic can be enhanced here based on Gemini API response
                if gemini_result1 or gemini_result2:
                    interactions.append(f"Possible interaction between {drug1} and {drug2} (from Gemini API)")
    return interactions

def get_dosage(drug, age):
    drug = drug.lower()
    if drug not in drug_db:
        gemini_result = gemini.query_drug(drug)
        if gemini_result and "dosage" in gemini_result:
            return gemini_result["dosage"]
        else:
            return "Dosage information not found"
    if age >= 18:
        return drug_db[drug]["dosage"]["adult"]
    else:
        return drug_db[drug]["dosage"]["child"]

def suggest_alternatives(drug, age):
    drug = drug.lower()
    if drug in drug_db:
        if drug == "aspirin":
            return ["ibuprofen"] if age >= 18 else ["acetaminophen"]
        elif drug == "warfarin":
            return ["heparin"]
        else:
            return ["consult doctor"]
    else:
        gemini_result = gemini.query_drug(drug)
        if gemini_result and "alternatives" in gemini_result:
            return gemini_result["alternatives"]
        else:
            return ["consult doctor"]
