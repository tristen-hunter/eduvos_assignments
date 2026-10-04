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
def create_csv(csv_file, fieldnames):
    try:
        with open(csv_file, "x") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
        print(f"Created {csv_file} with fieldnames: {fieldnames}")
    except FileExistsError:
        return


def add_inspection(inspection_template, csv_dir, fieldnames):
    new_inspection = utils.get_inspection_info(inspection_template)

    create_csv(csv_dir, fieldnames)

    try:
        with open(csv_dir, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(new_inspection)
        print("New Inspection successfully added")
    except IOError:
        print("Error writing to CSV file")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def load_inspections(csv_dir):
    try:
        with open(csv_dir, "r", newline="") as f:
            reader = csv.DictReader(f)
            headers = next(reader)
            print("{:<15} {:<10} {:<20}".format(headers[0], headers[1], headers[2]))
            for row in reader:
                print("{:<15} {:<10} {:<20}".format(row[0], row[1], row[2]))
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def find_inspection():
    return


def calculate_average_score():
    return


add_inspection(INSPECTION_TEMPLATE, CSV_FILE, FIELDNAMES)

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
    print("5. Inspection Summary")
    print("6. Exit")
    print("--------------------------------------------------------------------")
    input("Select Option: ")
