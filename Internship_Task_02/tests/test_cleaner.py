
import json

from src.json_cleaner.cleaner import clean_student_records


def test_clean_student_records():
    data = {
        "students": [
            {
                "student_id": 101,
                "student_record": json.dumps({
                    "name": "Arun",
                    "department": "AI&DS",
                    "year": 3
                }),
                "academic_record": json.dumps({
                    "python": 85,
                    "database": 90
                })
            }
        ]
    }

    result = clean_student_records(data)

    assert len(result) == 1
    assert result[0]["name"] == "Arun"
    assert result[0]["department"] == "AI&DS"
    assert result[0]["python"] == 85
    assert result[0]["database"] == 90

    
import csv

from src.json_cleaner.cleaner import export_to_csv


def test_export_to_csv(tmp_path):
    records = [
        {
            "student_id": 101,
            "name": "Arun",
            "department": "AI&DS",
            "year": 3,
            "python": 85,
            "database": 90
        }
    ]

    output_file = tmp_path / "cleaned_data.csv"

    export_to_csv(records, output_file)

    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0]["name"] == "Arun"
    assert rows[0]["python"] == "85"
    
from src.json_cleaner.cleaner import load_json_file


def test_load_missing_file(tmp_path):
    missing_file = tmp_path / "missing.json"

    result = load_json_file(missing_file)

    assert result is None
    
def test_load_invalid_json(tmp_path):
    invalid_file = tmp_path / "invalid.json"

    invalid_file.write_text(
        '{"students": [invalid data]}',
        encoding="utf-8"
    )

    result = load_json_file(invalid_file)

    assert result is None



