import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    with open('input.txt') as file:
        matrix = []
        count = 0
        for line in file:
            matrix.append([c for c in line.strip()])

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == '@' and check_coord(matrix, x, y):
                    count += 1
        print(count)
    return

def check_coord(matrix, x, y):
    c = []
    if y > 0:
        c.append(matrix[y-1][max(x-1,0):min(x+2,len(matrix[y]))])

    c.append(matrix[y][max(x-1,0):min(x+2,len(matrix[y]))])

    if y < len(matrix)-1:
        c.append(matrix[y+1][max(x-1,0):min(x+2,len(matrix[y]))])

    if sum(r.count('@') for r in c) <= 4:
        return True

    return False


if __name__ == "__main__":
    main()