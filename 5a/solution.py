#!/usr/bin/env python3

import re


double_letter_matcher = re.compile(r"(.)\1")


def is_nice(name):
    if len([c for c in name if c in 'aeiou']) < 3:
        return False

    if 'ab' in name or 'cd' in name or 'pq' in name or 'xy' in name:
        return False

    return double_letter_matcher.search(name)


def test_is_nice():
    assert is_nice('ugknbfddgicrmopn')
    assert is_nice('aaa')
    assert not is_nice('jchzalrnumimnmhp')
    assert not is_nice('haegwjzuvuyypxyu')
    assert not is_nice('dvszwmarrgswjxmb')


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        nice = [l for l in f if is_nice(l)]
        print(len(nice))
