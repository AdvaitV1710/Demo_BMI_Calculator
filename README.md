# BMI Calculator (CLI + FastAPI Web App)

This project includes:

- A CLI BMI calculator (`bmi_calculator.py`)
- A FastAPI + HTMX web app with live updates and Chart.js visualization (`app/main.py`)

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

## Web app behavior

- Form submits asynchronously with HTMX (no full page reload)
- Only the result section updates
- Weight slider triggers live recalculation while dragging
- Height can be entered in `cm`, `in`, or `ft`
- BMI category is shown alongside the numeric value
- A height unit converter is available on the page
- Chart.js renders a horizontal BMI scale (15 to 40) with a marker for the user's BMI

## Run the CLI version

```powershell
python bmi_calculator.py
```
