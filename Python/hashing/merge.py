import csv

def merge_csvs_with_prefix(csv1, csv2, output_filename):
    """Merge two CSV files into one with a unique prefix added to keys from each file."""
    
    with open(csv1, 'r') as file1, open(csv2, 'r') as file2, open(output_filename, 'w', newline='') as output_file:
        reader1 = csv.reader(file1)
        reader2 = csv.reader(file2)
        writer = csv.writer(output_file)

        # Write headers (assuming both CSVs have the same headers)
        writer.writerow(next(reader1))
        next(reader2)  # Skip header of the second CSV

        # Write content of first CSV with a prefix 'A_'
        for row in reader1:
            row[0] = "A_" + row[0]
            writer.writerow(row)

        # Write content of the second CSV with a prefix 'B_'
        for row in reader2:
            row[0] = "B_" + row[0]
            writer.writerow(row)

# Usage example:
merge_csvs_with_prefix('profiles.csv', 'flies.csv', 'merged_file.csv')
