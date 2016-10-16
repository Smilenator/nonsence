# -*- coding: utf-8 -*-
import sys
from os import listdir
from random import random, choice

class Nonsence(object):

    def __init__(self, deep=1):
        self.deep = deep
        self.input_path = 'input/'
        self.output_path = 'output/'
        self.end_char = '\n'

    def _read_file(self):
        self.mapping = {}
        with open(self.input_path + self.filename, 'r') as input_file:
            count_lines = 0
            for line in input_file:
                count_lines += 1
                for idx, letter in enumerate(line + self.end_char):
                    key = line[max(idx - self.deep, 0):idx]
                    if key not in self.mapping:
                        self.mapping[key] = ''
                    self.mapping[key] += letter
            self.stop_file_chance = 1.0 / count_lines

    def _create_file(self):
        with open(self.output_path + self.filename, 'w+') as output_file:
            create_new_line = 1
            while create_new_line >= self.stop_file_chance:
                line = self._generate_line()
                output_file.write(line)
                create_new_line = random()

    def _generate_line(self):
        line = ''
        current_letter = ''
        while current_letter != self.end_char:
            key = line[-self.deep:]
            if key in self.mapping:
                current_letter = choice(self.mapping[key])
                line += current_letter
        return line

    def run(self):
        for filename in listdir(self.input_path):
            self.filename = filename
            self._read_file()
            self._create_file()

if len(sys.argv) > 1:
    sys.argv[1] = int(sys.argv[1])
args = tuple(sys.argv[1:])
nonsence = Nonsence(*args)
nonsence.run()
print 'Done! See generated files in output/ directory'