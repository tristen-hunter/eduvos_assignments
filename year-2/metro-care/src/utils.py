def get_inspection_info(inspection_template):
    inspection_id = input("Enter Inspection ID: ")
    inspection_template["inspection_id"] = inspection_id

    equipment_code = input("Enter Equipment Code: ")
    inspection_template["equipment_code"] = equipment_code

    facility = input("Enter Facility Name: ")
    inspection_template["facility"] = facility

    technician = input("Enter Technician Name: ")
    inspection_template["technician"] = technician

    inspection_score = input("Enter Inspection Score: ")
    inspection_template["inspection_score"] = inspection_score

    status = input("Enter Equipment Status: ")
    inspection_template["status"] = status

    return inspection_template
