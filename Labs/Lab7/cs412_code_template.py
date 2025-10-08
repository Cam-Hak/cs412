"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def wfs(s):
    pass


def main():
    stops = {}
    num_segments = int(input())
    for _ in range(num_segments):
        stop = input()
        stop_split = stop.split(" ")
        stops[stop_split[0]] = stop_split[1]


if __name__ == "__main__":
    main()
