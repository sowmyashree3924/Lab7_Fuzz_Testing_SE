
import json
import math
import re


def calculate_dimensional_weight(dimensions_str):
    try:
        if not isinstance(dimensions_str, str):
            return None

        dims = dimensions_str.strip().split('x')

        if len(dims) != 3:
            return None

        length, width, height = map(float, dims)

        if not all(math.isfinite(d) and d > 0 for d in (length, width, height)):
            return None

        return round((length * width * height) / 5000.0, 2)

    except (ValueError, TypeError, OverflowError):
        return None


def format_tracking_label(raw_code):
    try:
        if not isinstance(raw_code, str):
            return None

        raw_code = raw_code.strip()

        if not re.fullmatch(r'[A-Za-z][0-9]+', raw_code):
            return None

        prefix = raw_code[0].upper()
        tracking_num = int(raw_code[1:])

        return f"{prefix}-{tracking_num:06d}"

    except (ValueError, TypeError, OverflowError):
        return None


def parse_package_manifest(json_payload):
    try:
        if not isinstance(json_payload, str):
            return None

        data = json.loads(json_payload)

        if not isinstance(data, dict) or "weight" not in data:
            return None

        weight = data["weight"]

        if isinstance(weight, bool):
            return None

        weight = float(weight)

        if not math.isfinite(weight) or weight <= 0:
            return None

        return weight

    except (ValueError, TypeError, KeyError, OverflowError):
        return None


def main():
    print("==== Running calculate_dimensional_weight ====")
    dims_input = input("Enter dimensions LxWxH in cm (e.g. 20x30x10): ")
    dim_weight = calculate_dimensional_weight(dims_input)
    print("Dimensional Weight (kg):", dim_weight)

    print("\n==== Running format_tracking_label ====")
    code_input = input("Enter raw code (e.g. E123): ")
    label = format_tracking_label(code_input)
    print("Formatted Label:", label)

    print("\n==== Running parse_package_manifest ====")
    json_input = input('Enter manifest JSON (e.g. {"weight": 12.5}): ')
    weight = parse_package_manifest(json_input)
    print("Manifest Weight:", weight)


if __name__ == "__main__":
    main()
