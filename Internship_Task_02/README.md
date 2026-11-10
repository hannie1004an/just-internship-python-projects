
# JSON Data Cleaner – CSV Generator

## 1. Project Overview

The JSON Data Cleaner is a Python-based data processing application that reads nested JSON data, extracts required information, and exports clean data into a CSV file.

## 2. Objective

The objective is to demonstrate Python file handling, nested JSON decoding, exception handling, and CSV file generation.

## 3. Technologies Used

- Python 3.11.9
- JSON module
- CSV module
- pathlib module
- Pytest

## 4. Project Structure

```text
Internship_Task_02/
├── data/
│   └── input.json
├── output/
│   └── cleaned_data.csv
├── screenshots/
├── src/
│   └── json_cleaner/
│       ├── __init__.py
│       └── cleaner.py
├── tests/
│   └── test_cleaner.py
└── README.md
```

## 5. Features

- Reads JSON data from a local file.
- Decodes nested JSON strings.
- Extracts selected student and academic information.
- Exports cleaned records into CSV format.
- Handles missing files and invalid JSON data.
- Includes automated tests using Pytest.

## 6. How to Run

Run the following command from the project directory:

```powershell
python .\src\json_cleaner\cleaner.py
```

## 7. Output

The application generates:

`output/cleaned_data.csv`

The CSV contains the following columns:

- student_id
- name
- department
- year
- python
- database

## 8. Testing

Run the automated tests using:

```powershell
python -m pytest tests/test_cleaner.py -v
```

Both automated tests passed successfully.

## 9. Conclusion

This project demonstrates how Python can process nested JSON data, handle file-related errors, and generate structured CSV output. It provides practical experience with file operations, JSON decoding, exception handling, and automated testing.
