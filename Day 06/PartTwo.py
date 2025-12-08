import time
import math

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    with open('input.txt') as file:
        file_str = file.read()
        file_split = file_str.split('\n')
        for c in range(len(file_split[0])):
            for l in file_split:
                if l[c] != ' ':
                    break
            else:
                for l in range(len(file_split)):
                    line = file_split[l]
                    file_split[l] = line[:c] + '.' + line[c+1:]
                    
        math_list = ''.join(str(x) + '.' for x in file_split).split('.')
        num_of_columns = file_str.count('+') + file_str.count('*')
        nums_per_operation = int(len(math_list) / num_of_columns - 1)
        count = 0

        for col in range(num_of_columns):
            nums = [math_list[num * num_of_columns + col] for num in range(nums_per_operation)]
            operation = math_list[nums_per_operation * num_of_columns + col].strip()
            total = 0 if operation == '+' else 1
            max_len = max([len(x) for x in nums])
            for i in range(max_len):
                num_str = ''
                for num in nums:
                    if len(num) >= i + 1:
                        num_str += num[i]
                if operation == '+':
                    total += int(num_str)
                else:
                    total *= int(num_str)
            count += total

        print(count)

    return

if __name__ == "__main__":
    main()