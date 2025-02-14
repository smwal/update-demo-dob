import pandas as pd
import datetime
import os

def adjust_dob_by_grade(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    current_year = datetime.datetime.now().year

    # Grade to age mapping (dictionary)
    grade_map = {
        -2: 3,  # Toddler/Pre-K Special Ed
        -1: 4,  # Pre-K
        "PreKindergarten": 4,  # Pre-K
        0: 5,  # Kindergarten
        "Kindergarten": 5,  # Kindergarten
        1: 6,
        2: 7,
        3: 8,
        4: 9,
        5: 10,
        6: 11,
        7: 12,
        8: 13,
        9: 14,
        10: 15,
        11: 16,
        12: 17,
        "1": 6,
        "2": 7,
        "3": 8,
        "4": 9,
        "5": 10,
        "6": 11,
        "7": 12,
        "8": 13,
        "9": 14,
        "10": 15,
        "11": 16,
        "12": 17,
    }

    def update_dob(row):
        grade = row['grade']
        dob = row['dob']

        try:
            month = dob[:2]
            day = dob[3:5]

            expected_age = grade_map.get(grade)

            if expected_age is None:
                print(f"Warning: No mapping for grade {grade}. Setting birth year to {current_year - 10}")
                expected_birth_year = current_year - 10
            else:
                expected_birth_year = current_year - expected_age

            updated_dob = f"{month}-{day}-{expected_birth_year}"
            return updated_dob
        except (ValueError, TypeError):
            print(f"Warning: Invalid DOB format '{dob}' in row. Skipping...")
            return dob

    df['dob'] = df.apply(update_dob, axis=1)

    try:
        df.to_csv(output_file, index=False)  # Save to the specified output file
        print(f"DOB values updated successfully. Saved to '{output_file}'.")
    except Exception as e:
        print(f"Error writing to CSV: {e}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(script_dir, "input_folder")
    output_folder = os.path.join(script_dir, "output_folder")

    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    input_file = os.path.join(input_folder, "input.csv")  # Path to your input file
    output_file = os.path.join(output_folder, "output.csv")  # Path to the output file

    adjust_dob_by_grade(input_file, output_file)  # Call the function with file paths