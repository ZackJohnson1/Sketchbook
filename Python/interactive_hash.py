import csv
import random

# Initialize a hash table (dictionary)
hash_table = {}

def add_profile_to_table(hash_table, profile):
    """Adds a profile to the hash table with a random key."""
    profile_key = "Profile_" + str(random.randint(10000000, 99999999))
    hash_table[profile_key] = profile
    return profile_key  # Return the generated key so it can be displayed to the user

def save_to_csv(hash_table, filename="profiles.csv"):
    """Saves the hash table to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Profile Key", "Name", "Age", "City"])
        
        # Write data
        for key, profile in hash_table.items():
            writer.writerow([key, profile.get('name', ''), profile.get('age', ''), profile.get('city', '')])

def input_profile():
    """Interactively inputs a profile."""
    name = input("Enter the name: ")
    age = input("Enter the age: ")
    city = input("Enter the city: ")
    return {
        'name': name,
        'age': age,
        'city': city
    }

def main():
    while True:
        print("\nMenu:")
        print("1. Add a new profile")
        print("2. Save profiles to CSV")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            profile = input_profile()
            generated_key = add_profile_to_table(hash_table, profile)
            print(f"Profile saved with key: {generated_key}")
            
        elif choice == '2':
            change_filename = input("Would you like to change the default filename (profiles.csv)? (yes/no) ").strip().lower()
            if change_filename == 'yes':
                filename = input("Enter the new filename: ")
                save_to_csv(hash_table, filename)
            else:
                save_to_csv(hash_table)
            print(f"Saved to {filename if change_filename == 'yes' else 'profiles.csv'}")
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
