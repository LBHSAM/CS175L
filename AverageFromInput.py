#anthonymendes
#cs175
def calculate_average(numbers):
    total = sum(numbers)  # calculate the sum
    return total / len(numbers)  # get the average


total_numbers = 0  # keep track of numbers read
current_total = 0  # keep track of current sum
with open('numbers.txt', 'r') as file:  # open the file named 'numbers.txt'
    for line in file:  # ooop
        number = int(line.strip())
        total_numbers += 1  # increase
        current_total += number  # add the current number to the current sum
        print(
            f'I read in {total_numbers} number(s) Current number is: {number:8.2f} Total is: {current_total:8.2f}')

    # calculate the average
    average = current_total / total_numbers
    print(f'Average: {average: .1f}')
