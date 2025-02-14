# DOB Updater

This Python script updates the Date of Birth (DOB) values in a CSV file based on the student's grade. It uses a grade-to-age mapping to calculate the expected birth year and adjusts the DOB accordingly.

## Prerequisites

* Python 3.6 or higher
* pandas library (`pip install pandas`)

## File Structure

app/
├── input_folder/
│   └── input.csv      # Your input CSV file
├── output_folder/
│   └── output.csv     # Updated CSV file will be saved here
└── update_dob.py    # The Python script

## How to Use

1. **Clone the Repository (if you haven't already):**
   ```bash
   git clone [https://github.com/](https://github.com/)[your-username]/[repo-name].git
Replace [your-username] and [repo-name] with your actual GitHub username and repository name.

2. Navigate to the Directory:

```
cd update-demo-dob
```

3. Create Input and Output Folders:

```
mkdir input_folder output_folder
```

4. Prepare Input Data:

Place your CSV file containing the student data in the input_folder and name it input.csv. The CSV should have at least two columns: grade and dob. The dob column should be in MM-DD-YYYY format.

## Run the Script:

```
python update_dob.py
```

View the Output
The updated CSV file with corrected DOBs will be saved as output.csv in the output_folder.

Grade Mapping
The script uses a dictionary (grade_map) to map grades to expected ages.  You can modify this dictionary within the update_dob.py script to customize the age mapping for different grades.

Error Handling
The script includes basic error handling for:

- Missing input CSV file.
- Invalid DOB formats in the input data.
- Grades without a defined mapping in the grade_map.


## Virtual Environments (Recommended)

It's highly recommended to use a virtual environment to manage dependencies.

Create a virtual environment:

```
python3 -m venv.venv
```

Activate the virtual environment:
```
source.venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

Install pandas:

```
pip install pandas
```

Run the script (inside the virtual environment):

```
python update_dob.py
```

Deactivate the virtual environment:

```
deactivate
```
