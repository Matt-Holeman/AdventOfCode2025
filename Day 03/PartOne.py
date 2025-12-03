import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    count = 0
    with open('input.txt') as file:
        for bank in file:
            arr = [int(b) for b in bank.strip()]
            count += int(f"{max(arr[:-1])}{max(arr[arr.index(max(arr[:-1]))+1:])}")
    print(count)
    return

if __name__ == "__main__":
    main()