# CSV Splitter and MySQL Database Importer

This repository contains two Python scripts: 

1. **split_csv.py** - Splits a large CSV file into smaller ones.
2. **import_database_mysql.py** - Imports data from a CSV file into a MySQL database.

## Prerequisites

Make sure to have the following prerequisites:

- Python 3.6 or higher
- MySQL database server

Python libraries:
- os
- csv
- pandas
- mysql-connector
- tqdm

## Usage

### 1. Splitting a CSV file

To split a large CSV file into multiple smaller files, use the `split_csv.py` script. 

You need to provide the path to the input CSV file, the path to the output directory where the split files will be saved, and the number of lines per file.

```python
input_csv = 'path_to_your_csv_file'
output_directory = 'path_to_output_directory'
lines_per_file = 50000  # number of lines per output file

split_csv(input_csv, output_directory, lines_per_file)

