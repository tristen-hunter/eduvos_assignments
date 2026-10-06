import csv
import inspection_processor


def get_inspection_info(inspection_template):
    while True:
        inspection_id = input("Enter Inspection ID      : ")
        if inspection_processor.validate_inspection_id(inspection_id):
            inspection_template["inspection_id"] = inspection_id.strip().upper()
            break
        print("Invalid Inspection ID. Format must be INSP001.")

    while True:
        equipment_code = input("Enter Equipment Code     : ")
        if inspection_processor.validate_equipment_code(equipment_code):
            inspection_template["equipment_code"] = equipment_code.strip().upper()
            break
        print("Invalid Equipment Code. Format must be EQ-2045.")

    while True:
        facility = input("Enter Facility Name      : ")
        if inspection_processor.validate_name(facility):
            inspection_template["facility"] = facility.strip()
            break
        print("Invalid facility name. Please enter a valid name.")

    while True:
        technician = input("Enter Technician Name    : ")
        if inspection_processor.validate_name(technician):
            inspection_template["technician"] = technician.strip()
            break
        print("Invalid technician name. Please enter a valid name.")

    while True:
        inspection_score = input("Enter Inspection Score   : ")
        if inspection_processor.validate_score(inspection_score):
            inspection_template["inspection_score"] = int(inspection_score.strip())
            break
        print("Invalid score. Enter a number between 0 and 100.")

    print()
    print("Available Statuses:")
    print("1. Operational")
    print("2. Review")
    print("3. Faulty")

    while True:
        status = input("Select Status            : ")
        if inspection_processor.validate_status(status):
            statuses = {"1": "Operational", "2": "Review", "3": "Faulty"}
            inspection_template["status"] = statuses[status.strip()]
            break
        print("Invalid status. Please select 1, 2, or 3.")

    return inspection_template


def find_inspection_by_id(csv_dir, search_column, search_value):
    try:
        with open(csv_dir, "r", newline="") as f:
            reader = csv.DictReader(f)

            if search_column not in reader.fieldnames:
                print(
                    f"Error: column '{search_column}' not found in CSV headers: "
                    f"{reader.fieldnames}"
                )
                return

            found_rows = []

            for row in reader:
                if (
                    str(row[search_column]).strip().lower()
                    == str(search_value).strip().lower()
                ):
                    found_rows.append(row)

            if not found_rows:
                print(
                    f"No match found for '{search_value}' in column '{search_column}'"
                )
                return

            # Table header
            print(
                "+--------------+----------------+---------------------------+----------------------+------------------+----------------+"
            )
            print(
                "| Inspection ID | Equipment Code | Facility                  | Technician           | Inspection Score | Status         |"
            )
            print(
                "+--------------+----------------+---------------------------+----------------------+------------------+----------------+"
            )

            # Matching rows
            for row in found_rows:
                print(
                    "| {:<12} | {:<14} | {:<25} | {:<20} | {:<16} | {:<14} |".format(
                        row["inspection_id"],
                        row["equipment_code"],
                        row["facility"],
                        row["technician"],
                        row["inspection_score"],
                        row["status"],
                    )
                )

            # Table footer
            print(
                "+--------------+----------------+---------------------------+----------------------+------------------+----------------+"
            )

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def print_headers(action_name):
    print()
    print("====================================================================")
    print("          METROCARE EMERGENCY EQUIPMENT MONITORING SYSTEM           ")
    print("====================================================================")
    print(f" {action_name}")
    print("--------------------------------------------------------------------")
