"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def dfs(g, i, j, n):
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0
    if g[i][j] == 0:
        return 0

    g[i][j] = 0
    count = 1
    count += dfs(g, i + 1, j, n)
    count += dfs(g, i - 1, j, n)
    count += dfs(g, i, j + 1, n)
    count += dfs(g, i, j - 1, n)
    return count


def main():
    n = int(input())

    g = []
    for _ in range(n):
        line = input().split()
        row = []
        for x in line:
            row.append(int(x))
        g.append(row)

    biggest = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                size = dfs(g, i, j, n)
                if size > biggest:
                    biggest = size

    print(biggest)


if __name__ == "__main__":
    main()
