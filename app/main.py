from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from bmi_core import calculate_bmi, ideal_weight_range

app = FastAPI(title="BMI Calculator")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


def build_result(
    weight: str, height: str, height_unit: str
) -> tuple[dict | None, str | None]:
    """Build BMI result payload and validation message from form strings."""
    try:
        weight_kg = float(weight)
        height_value = float(height)
        if weight_kg <= 0 or height_value <= 0:
            raise ValueError
        if height_unit == "cm":
            height_cm = height_value
        elif height_unit == "in":
            height_cm = height_value * 2.54
        elif height_unit == "ft":
            height_cm = height_value * 30.48
        else:
            raise ValueError

        bmi = calculate_bmi(weight_kg, height_cm)
        ideal_min, ideal_max = ideal_weight_range(height_cm)

        return (
            {
                "bmi": f"{bmi:.1f}",
                "ideal_min": f"{ideal_min:.1f}",
                "ideal_max": f"{ideal_max:.1f}",
            },
            None,
        )
    except ValueError:
        return None, "Please enter valid positive numbers for both fields."


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    weight = "70"
    height = "170"
    height_unit = "cm"
    result, error = build_result(weight, height, height_unit)

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "result": result,
            "error": error,
            "weight": weight,
            "height": height,
            "height_unit": height_unit,
        },
    )


@app.post("/calculate", response_class=HTMLResponse)
def calculate(
    request: Request,
    weight: str = Form(...),
    height: str = Form(...),
    height_unit: str = Form(...),
):
    result, error = build_result(weight, height, height_unit)
    context = {
        "result": result,
        "error": error,
        "weight": weight,
        "height": height,
        "height_unit": height_unit,
    }

    # Return only the result fragment for HTMX async updates.
    if request.headers.get("HX-Request") == "true":
        return templates.TemplateResponse(request, "partials/result.html", context)

    return templates.TemplateResponse(request, "index.html", context)
