#!/usr/bin/env python3

import re
import pytest


class Lights(object):
    X_COUNT = 1000
    Y_COUNT = 1000

    def __init__(self, initial=0):
        self.lights = [[initial for i in range(self.X_COUNT)] for j in range(self.Y_COUNT)]

    def turn_on(self, start_x, start_y, end_x, end_y):
        self.turn(start_x, start_y, end_x, end_y, 1)

    def turn_off(self, start_x, start_y, end_x, end_y):
        self.turn(start_x, start_y, end_x, end_y, -1)

    def turn(self, start_x, start_y, end_x, end_y, value):
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                self.lights[x][y] = max(self.lights[x][y] + value, 0)

    def toggle(self, start_x, start_y, end_x, end_y):
        self.turn(start_x, start_y, end_x, end_y, 2)

    def brightness(self):
        result = 0

        for x in range(self.X_COUNT):
            for y in range(self.Y_COUNT):
                result += self.lights[x][y]
        
        return result


class Instruction(object):
    parser = re.compile('')

    def __init__(self, instruction):
        parsed = re.search(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', instruction, re.IGNORECASE)

        self.command = parsed.group(1)
        self.start_x = int(parsed.group(2))
        self.start_y = int(parsed.group(3))
        self.end_x = int(parsed.group(4))
        self.end_y = int(parsed.group(5))

    def run(self, lights):
        if self.command == 'turn on':
            lights.turn_on(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.command == 'turn off':
            lights.turn_off(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.command == 'toggle':
            lights.toggle(self.start_x, self.start_y, self.end_x, self.end_y)



double_letter_matcher = re.compile(r"(.)\1")


if __name__ == "__main__":
    lights = Lights()

    with open("input.txt", "r") as f:
        for line in f:
            instruction = Instruction(line)
            instruction.run(lights)
    
    print(lights.brightness())


@pytest.mark.parametrize("instruction, command, start_x, start_y, end_x, end_y", [
    ('turn on 454,398 through 844,448', 'turn on', 454, 398, 844, 448),
    ('turn off 145,40 through 370,997', 'turn off', 145, 40, 370, 997),
    ('toggle 294,259 through 474,326', 'toggle', 294, 259, 474, 326),
])
def test_parse_instructions(mocker, instruction, command, start_x, start_y, end_x, end_y):
    i = Instruction(instruction)
    
    assert i.command == command
    assert i.start_x == start_x
    assert i.start_y == start_y
    assert i.end_x == end_x
    assert i.end_y == end_y

    m = mocker.Mock()

    i.run(m)

    if command == 'turn on':
        m.turn_on.assert_called_once_with(start_x, start_y, end_x, end_y)
    elif command == 'turn off':
        m.turn_off.assert_called_once_with(start_x, start_y, end_x, end_y)
    elif command == 'toggle':
        m.toggle.assert_called_once_with(start_x, start_y, end_x, end_y)


@pytest.mark.parametrize("start_x, start_y, end_x, end_y, init_brightness, end_brightness", [
    (0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 1, 1_000_001),
    (0, 0, 0, 0, 2, 2_000_001),
    (0, 0, 0, 499, 0, 500),
    (0, 0, 0, 499, 1, 1_000_500),
    (0, 0, 0, 499, 2, 2_000_500),
    (500, 500, 599, 599, 0, 10_000),
    (500, 500, 599, 599, 1, 1_010_000),
    (500, 500, 599, 599, 2, 2_010_000),
])
def test_turn_on(start_x, start_y, end_x, end_y, init_brightness, end_brightness):
    l = Lights(init_brightness)
    
    l.turn_on(start_x, start_y, end_x, end_y)

    assert l.brightness() == end_brightness


@pytest.mark.parametrize("start_x, start_y, end_x, end_y, init_brightness, end_brightness", [
    (0, 0, 999, 999, 0, 0),
    (0, 0, 999, 999, 1, 0),
    (0, 0, 999, 999, 2, 1_000_000),
    (0, 0, 0, 499, 0, 0),
    (0, 0, 0, 499, 1, 1_000_000 - 500),
    (0, 0, 0, 499, 2, 2_000_000 - 500),
    (500, 500, 599, 599, 0, 0),
    (500, 500, 599, 599, 1, 1_000_000 - 10_000),
    (500, 500, 599, 599, 2, 2_000_000 - 10_000),
])
def test_turn_off(start_x, start_y, end_x, end_y, init_brightness, end_brightness):
    l = Lights(init_brightness)
    
    l.turn_off(start_x, start_y, end_x, end_y)

    assert l.brightness() == end_brightness


@pytest.mark.parametrize("start_x, start_y, end_x, end_y, init_brightness, end_brightness", [
    (0, 0, 999, 999, 0, 2_000_000),
    (0, 0, 999, 999, 1, 3_000_000),
    (0, 0, 999, 999, 2, 4_000_000),
    (0, 0, 0, 499, 0, 1000),
    (0, 0, 0, 499, 1, 1_001_000),
    (0, 0, 0, 499, 2, 2_001_000),
    (500, 500, 599, 599, 0, 20_000),
    (500, 500, 599, 599, 1, 1_020_000),
    (500, 500, 599, 599, 2, 2_020_000),
])
def test_toggle(start_x, start_y, end_x, end_y, init_brightness, end_brightness):
    l = Lights(init_brightness)
    
    l.toggle(start_x, start_y, end_x, end_y)

    assert l.brightness() == end_brightness
