import csv 
import os
import datetime
import pandas as pd 
from pandas.errors import EmptyDataError
import matplotlib.pyplot as plt

FILE_NAME = 'finance_data.csv'
budgets = {}

def initialize_csv():
    """create CSV file with header"""
    if not os.path.exists(FILE_NAME): 
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Type', 'Category', 'Amount', 'Description'])
        print(f"Created new file: {FILE_NAME}")

def set_budget(): 
    """sets or updates budget limit for a category"""
    category = input("Enter category name: ")
    limit_str = input("Enter budget limit amount: $")
    try: 
        limit_value = float(limit_str)
        if category not in budgets: 
            budgets[category] = {'limit': limit_value, 'spent': 0}
        else: 
            budgets[category]['limit'] = limit_value
        print(f"Budget of ${limit_value:.2f} set for {category}.")
    except ValueError: 
        print("Invalid limit entered. Enter numerical value.")

def add_transaction(transaction_type): 
    """ user enters transaction details & add to the CSV file"""
    try: 
        amount = float(input("Enter amount: "))
        category = input("Enter category") 
        description = input("Enter description: ")

        # expenses stored as positive values, type determines income/expense
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        with open(FILE_NAME, mode='a', newline='') as file: 
            writer = csv.writer(file)
            date = datetime.date.today().strftime("%Y-%m-%d")
            writer.writerow([date, transaction_type.capitalize(), category, amount, description])
        print("Transaction added sucessfully.")
    except ValueError: 
        print("Invalid amount entered. Please enter a numerical value.")

def calculate_spending(budgets):
    """calculates total spending per category from CSV and updates the budgets"""
    for category in budgets: 
        budgets[category]['spent'] = 0 # reset spent amount before recalculating
    
    if os.path.exists(FILE_NAME): 
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file: 
            reader = csv.reader(file)
            next(reader, None) # skip header
            for row in reader: 
                try: 
                     # Date, Type, Category, Amount, Description
                    if len(row) < 4: continue 
                    trans_type = row[1].strip()
                    category = row[2].strip()
                    amount = float(row[3])
                    
                    # Only calculate if it is an Expense
                    if trans_type.lower() == 'expense':
                        if category in budgets:
                            budgets[category]['spent'] += amount
                except ValueError:
                    continue  # Skip rows with invalid amount format

def monitor_budgets(budgets): 
    """monitors and reports on current spending vs. budget"""
    calculate_spending(budgets) # makes spent values current
    print("\n--- Budget Report ---")
    for category, data in budgets.items():
        limit = data['limit']
        spent = data['spent']
        remaining = limit - spent
        status = "Under Budget" if remaining >= 0 else "Over Budget"
        print(f"Category: {category} | Limit: ${limit:.2f} | Spent: ${spent:.2f} | Remaining: #{remaining:.2f} | Status: {status}")
    print("------------------\n")

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
            if not row: continue
            try: 
            # Date, Type, Category, Amount, Description 
                trans_type = row[1]
                amount = float(row[3])
                if trans_type == 'income': 
                    income_total += amount 
                elif trans_type == 'expense': 
                    expense_total += amount 

            except (ValueError, IndexError): 
                continue

    print("\n--- Financial Summary ---")
    print(f"Totoal Income: ${income_total:.2f}")
    print(f"Total Expense: ${expense_total:.2f}")
    print(f"Net Balance: ${income_total - expense_total:.2f}")
    print("-------------------------\n")

    df = pd.read_csv("finance_data.csv", parse_dates=['Date'])

    expenses_df = df[df['Type'] == 'Expense']
    print("\nFiltered Expenses:")
    print(expenses_df.head())
    print("--------------------------------------------------------\n")

    try: 
        # load data, making sure to parse dates correctly
        df = pd.read_csv(FILE_NAME)
        if df.empty:  
            print("No data to analyze.")
        
        else: 
            required_cols = ['Date', 'Category', 'Amount', 'Type', 'Description']
            if not all(col in df.columns for col in required_cols): 
                print(f"Error: Missing one or more required columns: {required_cols}")
            else: 
                # create Month/Year columns for grouping
                df['Month'] = df['Date'].dt.to_period('M')
                df['Year'] = df['Date'].dt.to_period('Y')
       
        # # convert Data column to datetime for grouping 
        # df['Date'] = pd.to_datetime(df['Date'])
        # # create Month/Year columns for grouping
        # df['Month'] = df['Date'].dt.to_period('M')
        # df['Year'] = df['Date'].dt.to_period('Y')

                # group by month and category to get summary totals
                print("Monthly Summary:")
                monthly_summary = df.groupby(["Month", "Category"])["Amount"].sum().unstack().fillna(0)
                print(monthly_summary)

                # group by year and category for yearly totals
                print("\nYearly Summary:")
                yearly_summary = df.groupby(["Year", "Category"])["Amount"].sum().unstack().fillna(0) 
                print(yearly_summary)

                # plot total monthly spending 
                monthly_total = df[df['Type'] == 'Expense'].groupby('Month')['Amount'].sum()
                if not monthly_total.empty:
                    monthly_total.plot(kind='bar', title='Total MonthlySpending')
                    plt.tight_layout() # prevents label cutoff
                    plt.show()
                else:
                    print("No expense data to plot.")
    # except (EmptyDataError, KeyError, FileNotFoundError): 
    #     print("Error processing data with pandas.")
    except Exception as e:
        print(f"Error: {e}")
    print("\nSearch Results for 'Spotify':")
    # Case=False ensures it finds 'Spotify', 'spotify', etc.
    search_results = df[df['Description'].str.contains('Spotify', case=False, na=False)] 
    if search_results.empty:
        print("No Spotify transactions found.")
    else:
        print(search_results[['Date', 'Description', 'Amount']]) # Print relevant columns for cleaner output

def main(): 
    initialize_csv()
    while True: 
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. View Summary")
        print("5. Budget Report")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1': 
            add_transaction('income')
        elif choice == '2':
            add_transaction('expense')
        elif choice == '3':
            set_budget()
        elif choice == '4': 
            view_summary()
        elif choice == '5': 
            monitor_budgets(budgets)
        elif choice == '6':
            break
        else: 
            print("Invalid choice. Please choose a choice listed.")

if __name__ == "__main__": 
    main()