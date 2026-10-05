import csv


def get_inspection_info(inspection_template):
    inspection_id = input("Enter Inspection ID      : ")
    inspection_template["inspection_id"] = inspection_id

    equipment_code = input("Enter Equipment Code     : ")
    inspection_template["equipment_code"] = equipment_code

    facility = input("Enter Facility Name      : ")
    inspection_template["facility"] = facility

    technician = input("Enter Technician Name    : ")
    inspection_template["technician"] = technician

    inspection_score = input("Enter Inspection Score   : ")
    inspection_template["inspection_score"] = inspection_score

    print()
    print("Available Statuses: ")
    print("1. Operational")
    print("2. Review")
    print("3. Faulty")

    status = input("Select Status            : ")
    statuses = {"1": "Operational", "2": "Review", "3": "Faulty"}
    inspection_template["status"] = statuses[status]

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
