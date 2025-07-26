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
        raw_value = info["value"]
        data["segments"][name] = raw_value  # assign as-is (string)

    return data, errors
