from pathlib import Path
import xml.etree.ElementTree as ET

import utils
import xml_sample_data

# --- Global Variables ---
cwd = Path.cwd()
XML_FILE = cwd / "metrocare_inspections.xml"

LOW_SCORE_THRESHOLD = 60

TABLE_LINE = "+--------------+----------------+----------------------------+---------+----------------+"
TABLE_HEADER = "| Inspection ID | Equipment Code | Facility                   | Score   | Status         |"


# --- Helper Functions ---
def get_field(inspection, tag):
    """Return the stripped text of a child tag, or 'N/A' if missing/empty."""
    text = inspection.findtext(tag)
    return text.strip() if text and text.strip() else "N/A"


def get_score(inspection):
    """Return the Score as an int, or None if missing or not a number."""
    try:
        return int(inspection.findtext("Score", "").strip())
    except ValueError:
        return None


def print_inspection_table(inspections):
    """Print a list of <Inspection> elements as a formatted table."""
    print(TABLE_LINE)
    print(TABLE_HEADER)
    print(TABLE_LINE)

    for inspection in inspections:
        print(
            "| {:<12} | {:<14} | {:<26} | {:<7} | {:<14} |".format(
                get_field(inspection, "InspectionID"),
                get_field(inspection, "EquipmentCode"),
                get_field(inspection, "Facility"),
                get_field(inspection, "Score"),
                get_field(inspection, "Status"),
            )
        )

    print(TABLE_LINE)
    print()


# --- Main Functions ---
def create_xml(sample_data, xml_file):
    """Build the XML tree from sample_data and save it to xml_file."""
    root = ET.Element("MetroCareInspections")

    for record in sample_data:
        inspection = ET.SubElement(root, "Inspection")
        ET.SubElement(inspection, "InspectionID").text = str(record["InspectionID"])
        ET.SubElement(inspection, "EquipmentCode").text = str(record["EquipmentCode"])
        ET.SubElement(inspection, "Facility").text = str(record["Facility"])
        ET.SubElement(inspection, "Score").text = str(record["Score"])
        ET.SubElement(inspection, "Status").text = str(record["Status"])

    ET.indent(root)  # Pretty-print (Python 3.9+)

    try:
        tree = ET.ElementTree(root)
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)
        print(f"Saved {len(sample_data)} inspections to {xml_file}")
    except OSError as e:
        print(f"Could not write XML file: {e}")
    print()


def load_xml(xml_file):
    """Parse xml_file and return the root element, or None if loading fails."""
    try:
        return ET.parse(xml_file).getroot()
    except FileNotFoundError:
        print(f"File not found: {xml_file}")
        print("Use option 1 to create it first.")
    except ET.ParseError as e:
        print(f"The XML file is malformed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print()
    return None


def display_all_inspections(xml_file):
    """Load the XML and print every inspection."""
    root = load_xml(xml_file)
    if root is None:
        return

    inspections = root.findall("Inspection")
    if not inspections:
        print("No inspections found in the file.")
        print()
        return

    print_inspection_table(inspections)


def search_by_equipment_code(xml_file, equipment_code):
    """Print inspection(s) matching the equipment code (case-insensitive)."""
    root = load_xml(xml_file)
    if root is None:
        return

    search = equipment_code.strip().upper()
    matches = [
        inspection
        for inspection in root.findall("Inspection")
        if get_field(inspection, "EquipmentCode").upper() == search
    ]

    if matches:
        print(f"Found {len(matches)} inspection(s) for {search}:")
        print_inspection_table(matches)
    else:
        print(f"No inspections found for equipment code '{equipment_code}'.")
        print()


def find_low_scores(xml_file, threshold):
    """Print inspections with a score below threshold."""
    root = load_xml(xml_file)
    if root is None:
        return

    low_scores = []
    skipped = 0

    for inspection in root.findall("Inspection"):
        score = get_score(inspection)
        if score is None:
            skipped += 1
        elif score < threshold:
            low_scores.append(inspection)

    if low_scores:
        print(f"{len(low_scores)} inspection(s) scored below {threshold}:")
        print_inspection_table(low_scores)
    else:
        print(f"No inspections scored below {threshold}.")
        print()

    if skipped:
        print(f"Note: {skipped} record(s) skipped due to a missing/invalid score.")
        print()


def calculate_average_score(xml_file):
    """Print the average of all valid scores in the XML file."""
    root = load_xml(xml_file)
    if root is None:
        return

    scores = []
    skipped = 0

    for inspection in root.findall("Inspection"):
        score = get_score(inspection)
        if score is None:
            skipped += 1
        else:
            scores.append(score)

    if scores:
        average = sum(scores) / len(scores)
        print(f"Average score: {average:.2f} (from {len(scores)} inspections)")
    else:
        print("No valid scores found.")

    if skipped:
        print(f"Note: {skipped} record(s) skipped due to a missing/invalid score.")
    print()


while True:
    print("====================================================================")
    print("          METROCARE EMERGENCY EQUIPMENT MONITORING SYSTEM           ")
    print("====================================================================")
    print("  XML REPORT MANAGER")
    print("--------------------------------------------------------------------")
    print("1. Create and Save XML File")
    print("2. View All Inspections")
    print("3. Search by Equipment Code")
    print("4. Show Scores Below 60")
    print("5. Calculate Average Score")
    print("6. Exit")
    print("--------------------------------------------------------------------")
    action = input("Select Option: ")

    if action == "1":
        # Build XML from SAMPLE_DATA + write to disk
        create_xml(xml_sample_data.SAMPLE_DATA, XML_FILE)

    elif action == "2":
        utils.print_headers(" ALL XML EQUIPMENT INSPECTIONS")
        # Parse file + print all inspections
        display_all_inspections(XML_FILE)

    elif action == "3":
        utils.print_headers(" FIND INSPECTIONS BY EQUIPMENT CODE")
        # Get equipment code + search parsed XML
        equipment_code = input("Enter Equipment Code: ")
        search_by_equipment_code(XML_FILE, equipment_code)

    elif action == "4":
        utils.print_headers(" VIEW CRITICAL INSPECTIONS")
        # List inspections with score < 60
        find_low_scores(XML_FILE, LOW_SCORE_THRESHOLD)

    elif action == "5":
        utils.print_headers(" CALC AVG SCORE")
        # Sum of scores / number of inspections
        calculate_average_score(XML_FILE)

    elif action == "6":
        print()
        print("Goodbye!")
        break

    else:
        print("Invalid input, try again")
        continue
