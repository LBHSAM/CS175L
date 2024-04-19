
#anthony Mendes
#cs 175

import matplotlib.pyplot as plt

def read_expenses(file_name):
    data = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                category, amount = line.strip().split('\t')
                try:
                    data[category] = float(amount)
                except ValueError:
                    print(f"Error: Invalid amount '{amount}' for category '{category}'")
    except IOError:
        print("Error: could Not open or read the Rile.")
    return data

def plot_pie_chart(expenses):
    labels = expenses.keys()
    amounts = expenses.values()

    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=labels)
    plt.title('Monthly Expenses')
    plt.show()

def main():
    file_name = 'expenses.txt'
    expenses = read_expenses(file_name)
    if expenses:
        plot_pie_chart(expenses)

if __name__ == "__main__":
    main()
