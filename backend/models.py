from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import json

model_path = "ibm-granite/granite-3.3-2b-instruct"
device = "auto"  # Use auto to fallback to CPU if no GPU

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map=device,
    torch_dtype=torch.bfloat16,
)
tokenizer = AutoTokenizer.from_pretrained(model_path)

def extract_drug_info(text):
    # Use the Granite model to extract drug information from text with plain text output
    prompt = f"""You are a medical information assistant. Your task is to parse prescription text into a clear, neat, and human-friendly output.

Always identify and neatly list:

* Drug name
* Dosage (mg/ml/units)
* Frequency (e.g., twice daily, q8h, once daily, bedtime)
* Form/Route (tablet, syrup, injection, topical, etc.) if available

If any detail is missing or unclear, make a best-effort guess but mark it with (uncertain).

Also provide:

1. Prescription Summary — neatly formatted, one medicine per line.
2. Interactions — note any common drug–drug interactions within the given prescription.
3. Alternatives — suggest common alternatives if available (always add a warning: "Consult a doctor before switching medications.").
4. Dosage by Age — if the patient’s age is specified, adjust accordingly; if not, give standard adult dosage and note pediatric adjustments if known.

⚠️ Always include a final disclaimer:
“This information is for educational purposes only. Please consult a licensed doctor or pharmacist before making any medical decisions.”

You must never give definitive medical instructions; only general educational information.

Prescription text: {text}

Output:"""
    try:
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_new_tokens=500, temperature=0.1, do_sample=True)
        response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        return response.strip()
    except Exception as e:
        return "Error: " + str(e)
