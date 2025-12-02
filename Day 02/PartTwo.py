import time
import math

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    sum = 0
    with open('input.txt') as file:
        for product_range in file.readline().split(','):
            start =  int(product_range.split('-')[0])
            end =  int(product_range.split('-')[1])
            diff = end - start
            for i in range(diff+1):
                if is_product_invalid(str(start+i)):
                    sum += (start+i)
    print(sum)
    return

def is_product_invalid(product):
    for i in range(1, math.floor(len(product)/2)+1):
        if len(product) % i == 0:
            if product[0:i] * int(len(product)/i) == product:
                return True
    return False

if __name__ == "__main__":
    main()