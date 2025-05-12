# Normalize the Data by stripping extra spaces and newlines
def normalize_data(data_str):
    return ' '.join(data_str.split())


# Compare the expected and actual Data
def compare_data(expected_data, actual_data):
    normalized_expected_data = normalize_data(expected_data)
    normalized_actual_data = normalize_data(actual_data)

    # If the addresses do not match, return a detailed message
    if normalized_expected_data != normalized_actual_data:
        return False, f"Data mismatch: \nExpected: '{normalized_expected_data}'\nActual: '{normalized_actual_data}'"

    return True, "Data match."
