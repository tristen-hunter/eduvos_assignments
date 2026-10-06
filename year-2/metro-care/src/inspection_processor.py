import re
from concurrent.futures import ThreadPoolExecutor


# Validation Functions
def validate_inspection_reference(value):
    return bool(re.fullmatch(r"MC-\d{4}-\d{4}", str(value).strip().upper()))


def validate_inspection_id(value):
    return bool(re.fullmatch(r"INSP\d{3}", value.strip().upper()))


def validate_equipment_code(value):
    return bool(re.fullmatch(r"EQ-\d{4}", value.strip().upper()))


def validate_name(value):
    return bool(value.strip()) and all(part.isalpha() for part in value.strip().split())


def validate_email(value):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value))


def validate_score(value):
    try:
        score = int(value.strip())
        return 0 <= score <= 100
    except ValueError:
        return False


def validate_status(value):
    return value.strip() in {"1", "2", "3"}


# Process inspections
def process_inspection(record):
    errors = []

    if not validate_inspection_reference(record["reference"]):
        errors.append("Invalid inspection reference")

    if not validate_equipment_code(record["equipment"]):
        errors.append("Invalid equipment code")

    if not validate_email(record["email"]):
        errors.append("Invalid technician email")

    if errors:
        record["validation_status"] = "Invalid"
        record["validation_errors"] = errors
    else:
        record["validation_status"] = "Valid"
        record["validation_errors"] = []

    return record


# Spawn workers & write inspections
def process_batch(records, batch_size, worker_threads):
    batch = records[:batch_size]

    print(
        f"\nProcessing {len(batch)} inspection records "
        f"using {worker_threads} worker threads...\n"
    )

    with ThreadPoolExecutor(max_workers=worker_threads) as executor:
        futures = [executor.submit(process_inspection, record) for record in batch]

        results = []

        for future in futures:
            try:
                result = future.result()
                results.append(result)

                if result["validation_status"] == "Valid":
                    print(f"✓ {result['reference']} - Valid")
                else:
                    print(
                        f"✗ {result['reference']} - "
                        f"Invalid: {result['validation_errors']}"
                    )

            except Exception as e:
                print(f"✗ Unexpected processing error: {e}")

    return results
