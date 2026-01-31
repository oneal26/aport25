import csv 
import os

FILE_NAME = 'fiance_data.csv'

def initialize_csv():
    """create CSV file with header"""
    if not os.path.exists(FILE_NAME): 
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writernow(['Date', 'Type', 'Category', 'Amount', 'Description'])
        print(f"Created new file: {FILE_NAME}")

def add_transaction(transaction_type): 
    """ user enters transaction details & add to the CSV file"""
    try: 
        amount = float(input("Enter amount: "))
        category = input("Enter category") 
        description = input("Enter description: ")

        # expenses stored as positive values, type determines income/expense
        if transaction_type.lower() == 'expense' and amount > 0:
            pass # keep as positive, typeis expense 
        
        elif transaction_type.lower() == 'income' and amount < 0: 
            amount = abs(amount) # ensure income is stored positive
        
        with open(FILE_NAME, mode='a', newline='') as file: 
            writer = csv.writer(file)
            import datetime
            date = datetime.date.today().strftime("%Y-%m-%d")
            writer.writerow([date, transaction_type.capitalize(), category, amount, description])
        print("Transaction added sucessfully.")
    except ValueError: 
        print("Invalid amount entered. Please enter a numerical value.")

def view_summary():
    if not os.path.exists(FILE_NAME):
        print("No transactions recorded yet.")
        return 

    income_total = 0.0
    expense_total = 0.0

    with open(FILE_NAME, mode='r') as file: 
        reader = csv.reader(file)
        next(reader, None) # skip header row
        for row in reader: 
            if not row: 
                continue
            # Date, Type, Category, Amount, Description 
            trans_type = row[1]
            amount = float(row[3])
            if trans_type == 'Income': 
                income_total += amount 
            elif trans_type == 'Expense': 
                expense_total += amount 

    print("\n--- Financial Summary ---")
    print(f"Totoal Income: ${income_total:.2f}")
    print(f"Total Expense: ${expense_total:.2f}")
    print(f"Net Balance: ${income_total - expense_total:.2f}")
    print("-------------------------\n")

def main(): 
    initialize_csv()
    while True: 
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1': 
            add_transaction('Income')
        elif choice == '2':
            add_transaction('Expense')
        elif choice == '3':
            view_summary()
        elif choice == '4': 
            break
        else: 
            print("Invalid choice. Please choose a choice listed.")

if __name__ == "__main__": 
    main()