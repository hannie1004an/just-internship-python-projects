
import json
import csv
from pathlib import Path

def load_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("JSON file loaded successfully!")
        return data

    except FileNotFoundError:
        print("Error: Input file not found.")

    except json.JSONDecodeError as error:
        print(f"Error: Invalid JSON format. {error}")

    return None

def clean_student_records(data):
    cleaned_records = []

    for student in data.get("students", []):
        try:
            # Decode the nested JSON strings
            student_details = json.loads(student["student_record"])
            academic_details = json.loads(student["academic_record"])

            # Select the columns we need
            cleaned_records.append({
                "student_id": student["student_id"],
                "name": student_details.get("name", ""),
                "department": student_details.get("department", ""),
                "year": student_details.get("year", ""),
                "python": academic_details.get("python", ""),
                "database": academic_details.get("database", "")
            })

        except (KeyError, TypeError, json.JSONDecodeError) as error:
            print(f"Skipping invalid student record: {error}")

    return cleaned_records



def export_to_csv(records, output_path):
    if not records:
        print("No valid records to export.")
        return

    fieldnames = [
        "student_id",
        "name",
        "department",
        "year",
        "python",
        "database"
    ]

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with output_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)

        print(f"CSV file created successfully: {output_path}")

    except OSError as error:
        print(f"Error writing CSV file: {error}")

        
def main():
    # Find the project folder
    project_root = Path(__file__).resolve().parents[2]

    # Define input and output file paths
    input_path = project_root / "data" / "input.json"
    output_path = project_root / "output" / "cleaned_data.csv"

    # Load JSON data
    data = load_json_file(input_path)

    if data is None:
        return

    # Clean nested JSON records
    records = clean_student_records(data)

    # Export cleaned records to CSV
    export_to_csv(records, output_path)


if __name__ == "__main__":
    main()



