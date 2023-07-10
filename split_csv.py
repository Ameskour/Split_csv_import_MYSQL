import os
import csv

def split_csv(input_file, output_directory, lines_per_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header line

        line_count = 0
        file_count = 1
        output_file = os.path.join(output_directory, f'output_{file_count}.csv')

        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)  # Write the header to each output file

            for row in reader:
                writer.writerow(row)
                line_count += 1

                if line_count >= lines_per_file:
                    line_count = 0
                    file_count += 1
                    output_file = os.path.join(output_directory, f'output_{file_count}.csv')
                    outfile = open(output_file, 'w', newline='', encoding='utf-8')
                    writer = csv.writer(outfile)
                    writer.writerow(header)  # Write the header to each output file

        print(f"Splitting complete. {file_count} files generated.")

# Usage example
input_csv = 'path_to/Splite_csv/file.csv'
output_directory = 'path_to/Splite_csv/output'
lines_per_file = 50000

split_csv(input_csv, output_directory, lines_per_file)