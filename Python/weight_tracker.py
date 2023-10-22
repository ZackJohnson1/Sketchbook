import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

FILE_NAME = "weight_data.csv"

def add_weight_entry(weight):
    date = datetime.date.today()
    data = {'Date': [date], 'Weight': [weight]}
    df = pd.DataFrame(data)

    if os.path.exists(FILE_NAME):
        df.to_csv(FILE_NAME, mode='a', header=False, index=False)
    else:
        df.to_csv(FILE_NAME, index=False)

def plot_weight_graph():
    if not os.path.exists(FILE_NAME):
        print("No data available!")
        return

    df = pd.read_csv(FILE_NAME)
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Weight'], '-o', color='blue', label="Weight")
    plt.xlabel("Date")
    plt.ylabel("Weight (in kg)")
    plt.title("Weight Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\nWeight Tracker")
        print("1. Add weight entry")
        print("2. Show weight graph")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            weight = float(input("Enter your weight (in kg): "))
            add_weight_entry(weight)
            print("Weight entry added.")
        elif choice == '2':
            plot_weight_graph()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
