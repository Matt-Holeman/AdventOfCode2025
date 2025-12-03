import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    with open('input.txt') as file:
        count = 0
        for bank in file:
            arr = [int(b) for b in bank.strip()]
            running_min_index = 0
            out_str = ""
            for i in range(1, 13):
                search_arr = arr[running_min_index:(i-12) if i < 12 else None]
                out_str += str(max(search_arr))
                running_min_index += search_arr.index(max(search_arr))+1
            count += int(out_str)
        print(count)
    return

if __name__ == "__main__":
    main()