# MetroCare Inspection Management System

**Student:** Tristen Hunter Strydom  
**Student Number:** EDUV6474364  
**Assessment:** ITAPA Block 2 Formative Assessment

## Requirements

- Python 3.14
- No external dependencies required.

## How to Run

Run all commands from the project root directory.

### Question 1 and 2: Inspection Management and Processing

```bash
python3 src/inspection_manager.py
```

Use this to run the 6 unit tests

```bash
python3 src/test_inspection_manager.py
```

### Question 3: Emergency Alert System

Open two terminals.

**Terminal 1: Start the server**

```bash
python3 src/alert_server.py
```

**Terminal 2: Start the client**

```bash
python3 src/alert_client.py
```

Successful communication and the received alert will be displayed in the server terminal.

### Question 4: XML Report Management

```bash
python3 src/xml_report_manager.py
```

The program generates and processes `metrocare_inspections.xml`.
