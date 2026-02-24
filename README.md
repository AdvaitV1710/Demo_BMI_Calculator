# BMI Calculator (CLI + FastAPI Web App)

This project includes:

- A CLI BMI calculator (`bmi_calculator.py`)
- A FastAPI web app with a frontend (`app/main.py`)

## Requirements

- Python 3.10 or newer

## Setup

From the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the web app (localhost)

```powershell
uvicorn app.main:app --reload
```

Open:

- `http://127.0.0.1:8000`

The page lets you enter weight (kg) and height (cm), then shows:

- BMI value
- Ideal weight range for that height (based on BMI 18.5 to 24.9)

## Run the CLI version

```powershell
python bmi_calculator.py
```
