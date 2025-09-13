import requests
import base64

class GeminiAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.gemini.com/v2.5/flash"  # Using Gemini 2.5 Flash API endpoint

    def query_drug(self, drug_name: str):
        """
        Query the Gemini API for drug information.
        :param drug_name: Name of the drug to query.
        :return: Dictionary with drug information or None if not found.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "query": f"Provide information about the drug {drug_name}, including dosage, interactions, and alternatives."
        }
        try:
            response = requests.post(self.base_url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            # Assuming the response contains a 'results' field with drug info
            if "results" in data and len(data["results"]) > 0:
                return data["results"][0]
            else:
                return None
        except requests.RequestException as e:
            print(f"Gemini API request failed: {e}")
            return None

    def extract_text_from_image(self, image_data: bytes):
        """
        Extract text from image using Gemini API.
        :param image_data: Image bytes.
        :return: Extracted text or None if failed.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        # Encode image to base64
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        payload = {
            "query": "Extract the text from this image, focusing on any prescription or drug information.",
            "image": image_b64
        }
        try:
            response = requests.post(self.base_url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            # Assuming the response contains 'extracted_text'
            if "extracted_text" in data:
                return data["extracted_text"]
            else:
                return None
        except requests.RequestException as e:
            print(f"Gemini API image extraction failed: {e}")
            return None

# Usage example:
# gemini = GeminiAPI(api_key="YOUR_API_KEY_HERE")
# result = gemini.query_drug("aspirin")
# print(result)
# text = gemini.extract_text_from_image(image_bytes)
# print(text)
