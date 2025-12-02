import time

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
    if len(product) % 2 > 0:
        return False
    return product[0:int(len(product)/2)] * 2 == product

if __name__ == "__main__":
    main()