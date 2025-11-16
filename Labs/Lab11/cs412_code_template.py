"""
name: Cameron Hakenson
"""


def main():

    n = int(input())

    adj = [[] for _ in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        vertex_id = line[0]
        neighbors = line[1:] if len(line) > 1 else []
        adj[vertex_id] = neighbors

    proposed_set = list(map(int, input().split()))

    is_independent = True
    for i in range(len(proposed_set)):
        for j in range(i + 1, len(proposed_set)):
            v1 = proposed_set[i]
            v2 = proposed_set[j]
            if v2 in adj[v1] or v1 in adj[v2]:
                is_independent = False
                break
        if not is_independent:
            break

    print("TRUE" if is_independent else "FALSE")


if __name__ == "__main__":
    main()
