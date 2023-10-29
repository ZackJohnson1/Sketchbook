import csv
import os

def merge_csvs_with_prefix(filenames, output_filename):
    """Merge multiple CSV files into one, with a prefix derived from each filename added to keys from each file."""

    with open(output_filename, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        
        for filename in filenames:
            # Extract prefix from filename (without extension)
            prefix = os.path.splitext(os.path.basename(filename))[0]
            
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                
                # Write headers from the first CSV, skip headers for the rest
                if filename == filenames[0]:
                    writer.writerow(next(reader))
                else:
                    next(reader)
                
                # Write content of current CSV with its filename as a prefix
                for row in reader:
                    row[0] = f"{prefix}_{row[0]}"
                    writer.writerow(row)

if __name__ == "__main__":
    # Prompt the user for number of files to merge
    n = int(input("Enter the number of CSV files you want to merge: "))
    
    # Collect filenames
    filenames = []
    for i in range(n):
        file_name = input(f"Enter the name of CSV file {i + 1}: ")
        filenames.append(file_name)
    
    output_filename = input("Enter the name for the merged output file: ")

    merge_csvs_with_prefix(filenames, output_filename)
    print(f"Files {' ,'.join(filenames)} have been merged into {output_filename}.")
