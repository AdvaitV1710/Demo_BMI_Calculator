"""Simple CLI BMI calculator."""

from bmi_core import calculate_bmi, ideal_weight_range


def get_positive_number(prompt: str) -> float:
    """Prompt until a valid positive number is entered."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main() -> None:
    print("BMI Calculator")
    print("--------------")

    weight = get_positive_number("Enter your weight in kg: ")
    height = get_positive_number("Enter your height in cm: ")

    bmi = calculate_bmi(weight, height)
    ideal_min, ideal_max = ideal_weight_range(height)

    print(f"\nYour BMI is: {bmi:.1f}")
    print(
        "Ideal weight range for your height: "
        f"{ideal_min:.1f} kg to {ideal_max:.1f} kg"
    )


if __name__ == "__main__":
    main()
