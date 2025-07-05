import json
from PyPDF2 import PdfReader

def extract_form_data(pdf_path, output_path="output.json"):
    reader = PdfReader(pdf_path)
    root = reader.trailer["/Root"].get_object()  

    # Check if the PDF contains a form (AcroForm)
    if "/AcroForm" in root:
        fields = reader.get_fields()
        if fields:
            result = {k: v.get("/V") for k, v in fields.items() if v.get("/V") is not None}
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4, ensure_ascii=False)
            return result
        else:
            return {}
    else:
        return {}
