def validate_input(agency, paid_by, start_date, end_date, segment_inputs):
    errors = []
    data = {
        "agency": agency.strip(),
        "paid_by": paid_by.strip(),
        "start_date": str(start_date),
        "end_date": str(end_date),
        "segments": {}
    }

    if not agency:
        errors.append("Agency is required.")
    if not paid_by:
        errors.append("Paid by is required.")
    if start_date > end_date:
        errors.append("Start date must be before or equal to end date.")

    for name, info in segment_inputs.items():
        if not info["flag"]:
            continue
        value = info["value"].strip().replace("%", "")
        try:
            val_float = float(value)
            if name == "participation" and len(value.split(".")[-1]) != 3:
                errors.append(f"Participation must have 3 decimal places (got {value}).")
            data["segments"][name] = round(val_float, 3)
        except ValueError:
            errors.append(f"Invalid value for {name}: '{info['value']}'")

    return data, errors