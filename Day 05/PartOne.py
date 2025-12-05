import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    with open('input.txt') as file:
        file_string = file.read()
        count = 0
        split = file_string.split('\n\n')
        fresh_ranges = split[0].split('\n')
        product_range = split[1].split('\n')
        fresh_array = create_fresh_array(fresh_ranges)
        for p in product_range:
            print(f"Checking {p}")
            for r in fresh_array:
                if int(p) >= r[0] and int(p) <= r[1]:
                    count += 1
                    break
        print(count)
    return

def create_fresh_array(fresh_ranges):
    fresh_array = []
    for fresh_range in fresh_ranges:
        start = int(fresh_range.split('-')[0])
        end = int(fresh_range.split('-')[1])
        fresh_array.append((start, end))
    return fresh_array

if __name__ == "__main__":
    main()