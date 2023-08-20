# Simple ETL Process for User Data
--
## Overview

This Python program demonstrates a simple ETL (Extract, Transform, Load) process for handling user data. The script reads a CSV file containing user information, performs basic data transformation, and then loads the processed data into an SQLite database.

## Features

- **Extract:** Reads user data from a CSV file.
- **Transform:** Cleans the user data by filling missing names with 'Unknown'.
- **Load:** Inserts the transformed data into an SQLite database.

## Prerequisites

- Python 3.x
- pandas
- SQLAlchemy

## How to Run

1. **Install Dependencies:** Make sure pandas and SQLAlchemy are installed in your environment. You can install them using pip:

   ```bash
   pip install pandas sqlalchemy
   ```

2. **Prepare the CSV File:** Ensure that a CSV file named `data.csv` is in the same directory as the script. The file should have the following structure:

   ```csv
   id,name,age
   1,John,25
   2,Jane,30
   ```

3. **Run the Program:** Execute the script by running the following command in your terminal:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the actual filename of the script.

4. **Check the Database:** After running the program, you will find a new SQLite database file named `database.db` in the same directory. You can use an SQLite browser to view the contents of the `users` table.

## Code Structure

- `extract(file_path)`: Reads a CSV file and returns a DataFrame.
- `transform(data)`: Cleans the data by filling missing names.
- `load(data, database_path)`: Loads the cleaned data into an SQLite database.
- `etl(file_path, database_path)`: Executes the entire ETL process.

--
