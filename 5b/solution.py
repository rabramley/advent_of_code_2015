#!/usr/bin/env python3

import re


pair_repeat_matcher = re.compile(r"(..).*\1")
repeat_with_one_inbetween_matcher = re.compile(r"(.)[^\1]\1")


def is_nice(name):
    if not pair_repeat_matcher.search(name):
        return False
    if not repeat_with_one_inbetween_matcher.search(name):
        return False
    return True


def test_is_nice():
    assert is_nice('qtqt')
    assert is_nice('qjhvhtzxzqqjkmpb')
    assert is_nice('xxyxx')
    assert not is_nice('uurcxstgmygtbstg')
    assert not is_nice('ieodomkazucvgmuy')
    assert not is_nice('aaaba')


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        nice = [l for l in f if is_nice(l)]
        print(len(nice))
