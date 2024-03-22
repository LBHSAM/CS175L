#anthony mendes
#cs174
def read_values(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    num = float(line.strip())
                    numbers.append(num)
                    print(f"I read in {len(numbers)} number (s) Current number is: {num:.2f} Total is: {sum(numbers):.2f}")
                except ValueError:
                    print("Bad data: xyz skipping")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return numbers

def calculate_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0

def print_average(average):
    print(f"Average: {average:.1f}")

def main():
    filename = 'numbers.txt'
    numbers = read_values(filename)
    average = calculate_average(numbers)
    print_average(average)

if __name__ == "__main__":
    main()
