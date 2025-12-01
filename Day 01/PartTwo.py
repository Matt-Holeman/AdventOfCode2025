import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

# Very inefficient solve!
def solve():
    running_count = 50
    hits_zero = 0
    with open('input.txt') as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            num = int(line[1:])
            dir =  line[0]

            for _ in range(num):
                if dir == 'R':
                    running_count += 1
                else:
                    running_count -= 1

                if running_count == 0:
                    hits_zero += 1
                if running_count < 0:
                    running_count = 99
                if running_count == 100:
                    hits_zero += 1
                    running_count = 0
        print(hits_zero)
    return

if __name__ == "__main__":
    main()