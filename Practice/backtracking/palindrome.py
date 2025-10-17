def is_palindrome(p_string):
    return p_string == p_string[::-1]


def partition(s):
    res = []
    part = []

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return

        for j in range(i, len(s)):
            if is_palindrome(s[i : j + 1]):
                part.append(s[i : j + 1])
                dfs(j + 1)
                part.pop()

    dfs(0)
    return res

print(partition("aab"))
