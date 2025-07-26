def validate_input(agency, paid_by, start_date, end_date, segment_inputs):
    errors = []
    data = {
        "agency": agency.strip(),
        "paid_by": paid_by.strip(),
        "start_date": str(start_date),
        "end_date": str(end_date),
    }

    # Validate basic required fields
    if not agency.strip():
        errors.append("Agency is required.")
    if not paid_by.strip():
        errors.append("Paid by is required.")
    if start_date > end_date:
        errors.append("Start date must be before or equal to end date.")

    # Extract segment values as strings (skip unflagged)
    for name, info in segment_inputs.items():
        if not info["flag"]:
            continue

        value = info["value"].strip()

        # Optional validation: participation must be % and 3 decimal places
        if name.lower() == "participation":
            if not value.endswith("%"):
                errors.append("Participation must be a percentage (e.g., 0.689%)")
            else:
                raw = value.replace("%", "")
                if "." not in raw or len(raw.split(".")[-1]) != 3:
                    errors.append(f"Participation must have 3 decimal places (e.g., 0.689%)")

        data[name] = value  # Preserve value as-is (e.g., '19.8%')

    return data, errors
