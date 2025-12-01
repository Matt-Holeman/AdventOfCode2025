import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    running_count = 50
    hits_zero = 0
    print(f"In\tNum\tc\tz")
    print(f"\t\t{running_count}\t{hits_zero}")
    with open('input.txt') as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            dial_change = int(line[1:]) if line[0] == 'R' else 0 - int(line[1:])
            running_count += dial_change
            running_count = running_count % 100
            if running_count == 0:
                hits_zero += 1
            print(f"{line}\t{int(line[1:]) if line[0] == 'R' else 0 - int(line[1:])}\t{running_count}\t{hits_zero}")
    print(hits_zero)
    return

if __name__ == "__main__":
    main()