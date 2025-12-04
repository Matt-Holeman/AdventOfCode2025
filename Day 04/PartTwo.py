import time

def main():
    start = time.time()
    solve()
    end = time.time()
    print(f"Took: {round((end-start) * 10**3)}ms")

def solve():
    with open('input.txt') as file:
        matrix = []
        total = 0

        for line in file:
            matrix.append([c for c in line.strip()])

        for _ in range(1000):
            count = 0
            removals = []
            for y in range(len(matrix)):
                for x in range(len(matrix[y])):
                    if matrix[y][x] == '@' and check_coord(matrix, x, y):
                        removals.append((y,x))
                        count += 1

            for remove in removals:
                matrix[remove[0]][remove[1]] = 'x'

            if count == 0:
                output_matrix(matrix)
                break

            total += count
        print(total)
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

def output_matrix(matrix):
    for y in matrix:
        for x in y:
            print(x, end=" ")
        print()


if __name__ == "__main__":
    main()