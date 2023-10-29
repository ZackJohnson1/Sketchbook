import csv
import random

# Initialize a hash table (dictionary)
hash_table = {}

def add_profile_to_table(hash_table, profile):
    """Adds a profile to the hash table with a unique random key."""
    while True:
        profile_key = "Profile_" + str(random.randint(10000000, 99999999))
        if profile_key not in hash_table:
            break

    hash_table[profile_key] = profile
    return profile_key  # Return the generated key so it can be displayed to the user

def save_to_csv(hash_table, filename="default.csv"):
    """Saves the hash table to a CSV file."""
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Profile Key", "Name", "Age", "City", "State", "Country"])
        
        for key, profile in hash_table.items():
            writer.writerow([key, profile.get('name', ''), profile.get('age', ''), profile.get('city', ''), profile.get('state', ''), profile.get('country', '')])

def input_profile():
    while True:
        name = input("Enter the name: ").strip()
        if not name or not all(word.isalpha() for word in name.split()):
            print("Please enter a valid name (alphabets only).")
            continue
        break
    
    while True:
        age = input("Enter the age: ").strip()
        if not age.isdigit() or not (0 <= int(age) <= 120):
            print("Please enter a valid age (0-120).")
            continue
        break
    
    while True:
        city = input("Enter the city: ").strip()
        if not city or not all(word.isalpha() for word in city.split()):
            print("Please enter a valid city name (alphabets only).")
            continue
        break

    state = input("Enter the state (leave empty if not applicable): ").strip()
    while state and not all(word.isalpha() for word in state.split()):
        print("Please enter a valid state name (alphabets only) or leave it empty.")
        state = input("Enter the state (leave empty if not applicable): ").strip()

    while True:
        country = input("Enter the country: ").strip()
        if not country or not all(word.isalpha() for word in country.split()):
            print("Please enter a valid country name (alphabets only).")
            continue
        break

    profile = {
        'name': name,
        'age': age,
        'city': city,
        'country': country
    }
    
    if state:
        profile['state'] = state

    return profile

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
            change_filename = input("Would you like to change the default filename (default.csv)? (yes/no) ").strip().lower()
            if change_filename == 'yes':
                filename = input("Enter the new filename (no need to add .csv, it will be added automatically): ")
                save_to_csv(hash_table, filename)
            else:
                save_to_csv(hash_table)
            print(f"Saved to {filename if change_filename == 'yes' else 'default.csv'}")
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
