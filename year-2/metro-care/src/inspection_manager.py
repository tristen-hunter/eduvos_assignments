import csv
from pathlib import Path
import utils


# --- Global Variables ---
cwd = Path.cwd()
CSV_FILE = cwd / "data" / "inspections.csv"

INSPECTION_TEMPLATE = {
    "inspection_id": "",
    "equipment_code": "",
    "facility": "",
    "technician": "",
    "inspection_score": 0,
    "status": "",
}

FIELDNAMES = list(INSPECTION_TEMPLATE.keys())


# --- Functions ---
def create_csv(csv_dir, fieldnames):
    try:
        with open(csv_dir, "x") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
        print(f"Created {csv_dir} with fieldnames: {fieldnames}")
    except FileExistsError:
        return


def add_inspection(inspection_template, csv_dir, fieldnames):
    new_inspection = utils.get_inspection_info(inspection_template)

    create_csv(csv_dir, fieldnames)

    try:
        with open(csv_dir, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(new_inspection)
        print()
        print("New Inspection successfully added")
    except IOError:
        print("Error writing to CSV file")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def load_inspections(csv_dir):
    try:
        with open(csv_dir, "r", newline="") as f:
            reader = csv.DictReader(f)

            print(
                "+--------------+----------------+---------------------------+----------------------+------------------+----------------+"
            )
            print(
                "| Inspection ID | Equipment Code | Facility                  | Technician           | Inspection Score | Status         |"
            )
            print(
                "+--------------+----------------+---------------------------+----------------------+------------------+----------------+"
            )

            for row in reader:
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

            print(
                "+--------------+----------------+---------------------------+----------------------+------------------+----------------+"
            )
            print()
            print()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def find_inspection(csv_dir, fieldnames):
    inspection_id = input("Inspection ID: ")
    print()

    utils.find_inspection_by_id(csv_dir, fieldnames[0], inspection_id)
    print()


def calculate_average_score(csv_dir):
    try:
        with open(csv_dir, "r", newline="") as f:
            reader = csv.DictReader(f)

            scores = []

            for row in reader:
                score = int(row["inspection_score"])
                scores.append(score)

            if scores:
                average = sum(scores) / len(scores)
                print(f"Average score: {average:.2f}")
            else:
                print("No inspection scores found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


while True:
    print("====================================================================")
    print("          METROCARE EMERGENCY EQUIPMENT MONITORING SYSTEM           ")
    print("====================================================================")
    print("  INSPECTION FILE MANAGER")
    print("--------------------------------------------------------------------")
    print("1. Add New Inspection")
    print("2. View All Inspections")
    print("3. Search Inspection")
    print("4. Calculate Average Score")
    print("5. Exit")
    print("--------------------------------------------------------------------")
    action = input("Select Option: ")

    if action == "1":
        utils.print_headers(" ADD NEW INSPECTION")
        # Create + write the new inspection
        add_inspection(INSPECTION_TEMPLATE, CSV_FILE, FIELDNAMES)

    elif action == "2":
        utils.print_headers(" VIEW ALL INSPECTIONS")
        # Fetch and display all as a table
        load_inspections(CSV_FILE)

    elif action == "3":
        utils.print_headers(" FIND BY ID")

        find_inspection(CSV_FILE, FIELDNAMES)

    elif action == "4":
        utils.print_headers(" AVERAGE SCORE")

        calculate_average_score(CSV_FILE)

    elif action == "5":
        print()
        print("Goodbye!")
        break
