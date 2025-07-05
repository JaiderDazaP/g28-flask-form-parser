# tests/test_pdf_extractor.py

import os
import json
from app.pdf_extractor import extract_form_data

def test_extract_form_data_creates_json():
    test_pdf = "g-28_data.pdf"
    test_output = "test_output.json"

    # Run the extraction
    data = extract_form_data(test_pdf, output_path=test_output)

    # Check the file was created and is not empty
    assert os.path.exists(test_output)
    assert isinstance(data, dict)
    assert len(data) > 0

    # Load and compare
    with open(test_output, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        assert loaded_data == data

    # Cleanup
    os.remove(test_output)
