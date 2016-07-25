import argparse
import math


class GCodeWriter:

    def __init__(self, input_seq=""):
        self.num_input = input_seq
        input_lines = input_seq.split("\n")
        for line in input_lines:
            input_members = line.split(",")
            print self.construct_gcode_line_from_array(input_members)

    def construct_gcode_line_from_array(self, input_array):
        gcode = "G1 "
        coords = ['X', 'Y', 'Z']
        for idx, entry in enumerate(input_array):
            gcode += coords[idx] + entry + " "
        gcode += "E" + str((math.sqrt(math.pow(float(input_array[0]), 2.0)) +
                           math.sqrt(math.pow(float(input_array[1]), 2.0))) / 3.0)  # FIX E CALCULATION
        return gcode


if __name__ == '__main__':
    mock_input = "0.2,0.3,0.4\n" \
                 "0.6,0.5,0.4"

    writer = GCodeWriter(input_seq=mock_input)
