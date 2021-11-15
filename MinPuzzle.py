# Name: Peter Storum
# Time Complexity: n * m

def minEffort(puzzle):
    m = n = 0
    x = (len(puzzle) - 1)
    y = (len(puzzle[0])-1)
    route = []
    effort = 0
    route.append(puzzle[m][n])
    while m != x or n != y:
        if m != x and n != y:
            effort_next = min(abs(puzzle[m + 1][n] - puzzle[m][n]), abs(puzzle[m][n + 1] - puzzle[m][n]))
            if min(abs(puzzle[m + 1][n] - puzzle[m][n]), abs(puzzle[m][n + 1] - puzzle[m][n])) == abs(puzzle[m + 1][n] - puzzle[m][n]):
                route.append(puzzle[m + 1][n])
                m += 1
            else:
                route.append(puzzle[m][n + 1])
                n += 1
            effort = max(effort, effort_next)
        elif m == x:
            route.append(puzzle[m][n+1])
            effort = max(effort, abs(puzzle[m][n+1] - puzzle[m][n]))
            n += 1
        elif n == y:
            route.append(puzzle[m+1][n])
            effort = max(effort, abs(puzzle[m + 1][n] - puzzle[m][n]))
            m += 1
    return effort


if __name__ == '__main__':
    arr = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
    print(minEffort(arr))
