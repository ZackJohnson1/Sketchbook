import csv

def merge_csvs(file1, file2, output_file):
    """
    Merge the contents of two CSV files and save to an output file.

    Args:
    - file1: Path to the first CSV file.
    - file2: Path to the second CSV file.
    - output_file: Path to the output CSV file where merged data will be saved.
    """
    # Hold all rows from both CSVs
    all_rows = []

    # Read first CSV
    with open(file1, 'r', newline='') as f1:
        reader = csv.reader(f1)
        for row in reader:
            all_rows.append(row)

    # Read second CSV
    with open(file2, 'r', newline='') as f2:
        reader = csv.reader(f2)
        # Skip the header if it's the same as the first file
        next(reader)
        for row in reader:
            all_rows.append(row)

    # Write merged rows to output file
    with open(output_file, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerows(all_rows)

# Example Usage

merge_csvs('profiles.csv', 'files.csv', 'merged.csv')
