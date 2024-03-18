#anthony mendes
# cs175
def calculate_average(numbers):
    total = sum(numbers)  # Calculate the sum of all numbers in the list
    return total / len(numbers)  # Divide the total sum by the number of numbers to get the average


def main():
    total_numbers = 0
    current_total = 0
    with open('numbers.txt', 'r') as file:  # Open the file
        for line in file:  # Loop
            number = int(line.strip())
            total_numbers += 1
            current_total += number  # add the current number to the current sum
            print(
                f'I read in {total_numbers} number(s) Current number is: {number:8.2f} Total is: {current_total:8.2f}')

        # calculatethe average
        average = current_total / total_numbers
        print(f'Average: {average: .1f}')


if __name__ == "__main__":
    main()
