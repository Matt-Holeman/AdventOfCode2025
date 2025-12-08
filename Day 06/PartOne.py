import time
import math

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    with open('input.txt') as file:
        file_str = ''
        for line in file:
            file_str += line.strip()
            file_str += ' '

        num_of_columns = file_str.count('+') + file_str.count('*')
        math_list = [num for num in file_str.split(' ') if num.strip()]
        nums_per_operation = int(len(math_list) / num_of_columns - 1)
        count = 0

        for col in range(num_of_columns):
            if math_list[nums_per_operation * num_of_columns + col] == '+':
                count += sum([int(math_list[num * num_of_columns + col]) for num in range(nums_per_operation)])
            else:
                count += math.prod([int(math_list[num * num_of_columns + col]) for num in range(nums_per_operation)])
        print(count)
    return

if __name__ == "__main__":
    main()