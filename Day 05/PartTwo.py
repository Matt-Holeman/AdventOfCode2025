import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    with open('input.txt') as file:
        file_string = file.read()
        fresh_array = sorted(create_fresh_array(file_string.split('\n\n')[0].split('\n')))
        count = 0

        for _ in range(100):
            done = True
            for r1 in fresh_array:
                for r2 in fresh_array:
                    if r1 is not r2 and is_overlapping(r1, r2):
                        r1[0] = min(r1[0], r2[0])
                        r1[1] = max(r1[1], r2[1])
                        fresh_array.remove(r2)
                        done = False
            if done:
                break

        for r in fresh_array:
            count += (r[1]+1) - r[0]

        print(count)

    return

def create_fresh_array(fresh_ranges):
    return [[int(x.split('-')[0]), int(x.split('-')[1])] for x in fresh_ranges]

def is_overlapping(a, b):
    return max(a[0],b[0]) < min(a[1]+1,b[1]+1)

if __name__ == "__main__":
    main()