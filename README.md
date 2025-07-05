# G28-FLASK-FORM-PARSER

This project extracts filled form fields from a government-issued PDF (Form G-28), converts them into JSON, and displays them through a secure Flask API and a visual HTML viewer.

---

## Features

- Extracts PDF AcroForm field values.
- Outputs a clean JSON structure.
- Flask API with Basic Auth protection.
- Web-based viewer with search functionality.
- Dockerized app with tests included.

---

## Requirements

- Python 3.9+ or Docker
- `pip install -r requirements.txt` (if running locally)
- Internet access for installing dependencies

---

## Local Development

1. Clone the repository

```bash
git clone https://github.com/JaiderDazaP/g28-flask-form-parser.git
cd g28-flask-form-parser
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app/main.py
```

4. Access:

- Viewer: [http://localhost:4532](http://localhost:4532)
- JSON (requires auth):  
```bash
curl -u admin:admin http://localhost:4532/api/json
```

---

## Docker Instructions

### Build the image

```bash
docker build -t g28-flask-app .
```

### Run the container

```bash
docker run -p 4532:4532 g28-flask-app
```

---

## Authentication

The `/api/json` route is protected with HTTP Basic Auth.

- **Username:** `admin`  
- **Password:** `admin`

---

## Running Tests

This project uses `pytest`.

```bash
PYTHONPATH=. pytest
```

If you want to run tests in Docker:

```bash
docker build -t g28-flask-app .  # tests run during build
```

---

## Deploy to AWS EC2

1. Create an EC2 instance with Ubuntu or Amazon Linux.

2. Connect via SSH using the credentials and key provided by AWS.

3. Install Docker:

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo usermod -aG docker $USER
```

4. Clone the repo and build:

```bash
git clone https://github.com/JaiderDazaP/g28-flask-form-parser.git
cd g28-flask-form-parser
docker build -t g28-flask-app .
docker run -d -p 80:4532 g28-flask-app
```

5. Access from your browser:  
`http://<EC2-IP>`

---

## 📂 Project Structure

```
.
├── app/
│   ├── main.py
│   ├── pdf_extractor.py
│   └── templates/
│       └── viewer.html
├── tests/
│   └── test_pdf_extractor.py
├── g-28_data.pdf
├── output.json
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ✏️ Notes

- `output.json` is generated on startup.
- You can replace the sample PDF with another fillable form for testing.
- The viewer supports live filtering of keys.
