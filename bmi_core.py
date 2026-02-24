"""Shared BMI calculation utilities for CLI and web app."""

HEALTHY_BMI_MIN = 18.5
HEALTHY_BMI_MAX = 24.9


def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Return BMI using metric units."""
    height_m = height_cm / 100
    return weight_kg / (height_m * height_m)


def ideal_weight_range(height_cm: float) -> tuple[float, float]:
    """Return ideal weight range (kg) for a given height in cm."""
    height_m = height_cm / 100
    min_weight = HEALTHY_BMI_MIN * (height_m * height_m)
    max_weight = HEALTHY_BMI_MAX * (height_m * height_m)
    return min_weight, max_weight
