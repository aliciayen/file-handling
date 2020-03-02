# Alicia Yen

import sys


def stats(filename):
    with open(filename) as stat_file:
        content = stat_file.read()

    char_count = len(content)
    word_count = len(content.split())
    line_count = len(content.splitlines())
    longest_line = max(len(l) for l in content.splitlines())

    return char_count, word_count, line_count, longest_line


if __name__ == "__main__":
    filename = sys.argv[1]
    c, w, l, ll = stats(filename)
    print("Characters: {}".format(c))
    print("Words: {}".format(w))
    print("Lines: {}".format(l))
    print("Longest line: {}".format(ll))
