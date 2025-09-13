# Drug Interaction Detection System

This project analyzes drug interactions, identifies correct drug dosages, and provides safe alternative medication options based on age and drug details. It integrates multiple datasets and leverages advanced NLP models (IBM Granite) and APIs for accurate drug information extraction and interaction understanding.

## Features

- **Drug Interaction Detection**: Detects and flags harmful interactions between multiple drugs.
- **Age-Specific Dosage Recommendation**: Recommends accurate dosages based on patient age and drug safety profiles.
- **Alternative Medication Suggestions**: Suggests safer or equivalent drugs when interactions or contraindications are identified.
- **NLP-Based Drug Information Extraction**: Uses IBM Granite model to extract structured drug details (name, dosage, frequency) from unstructured medical text.
- **User-Friendly Interface**: Interactive Streamlit frontend for easy user interaction, with a FastAPI backend for real-time analysis.

## Technologies Used

- Python
- Streamlit (Frontend)
- FastAPI (Backend)
- IBM Granite (NLP Model)
- HuggingFace Transformers
- PyTorch

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/drug-interaction-system.git
   cd drug-interaction-system
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the backend:
   ```
   uvicorn backend.app:app --reload
   ```

4. In another terminal, run the frontend:
   ```
   streamlit run frontend/app.py
   ```

5. Open your browser to http://localhost:8501 for the Streamlit UI.

## Usage

- Enter medical text in the "Extract Drug Information" section to extract drug details.
- Input drug names separated by commas in "Check Drug Interactions" to detect interactions.
- Specify drug and age for dosage recommendations and alternative suggestions.

## Project Structure

- `backend/`: FastAPI backend code
  - `app.py`: Main FastAPI application
  - `models.py`: IBM Granite model loading and NLP functions
  - `drug_logic.py`: Drug interaction, dosage, and alternative logic
- `frontend/`: Streamlit frontend code
  - `app.py`: Streamlit UI
- `requirements.txt`: Python dependencies
- `.gitignore`: Git ignore file

## Contributing

Feel free to submit issues and pull requests.

## License

MIT License
