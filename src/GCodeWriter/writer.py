import argparse
import math


class GCodeWriter:

    def __init__(self, input_seq="", nozzle_diameter=0.4, e_modifier=12.0):
        self.num_input = input_seq
        self.prev_e_value = 0
        input_lines = input_seq.split("\n")
        for line in input_lines:
            input_members = line.split(",")
            print self.construct_g1_line_from_array(input_members, e_modifier)

    def construct_g1_line_from_array(self, input_array, e_modifier):
        gcode = "G1 "
        coords = ['X', 'Y', 'Z']
        for idx, entry in enumerate(input_array):
            gcode += coords[idx] + entry + " "
        gcode += "E" # FIX E CALCULATIONi
        ans = (math.sqrt(math.pow(float(input_array[0]), 2) + math.pow(float(input_array[1]), 2)))
        ans = ans / e_modifier
        ans = round(ans, 5)
        gcode += str(ans + self.prev_e_value)
        self.prev_e_value += (ans + self.prev_e_value)
        return gcode


if __name__ == '__main__':
    mock_input = "0.2,0.3,0.4\n" \
                 "0.6,0.5,0.4"
    nozzle_diameter = 0.4 # in mm
    e_mod = 12.0

    writer = GCodeWriter(input_seq=mock_input, nozzle_diameter=nozzle_diameter, e_modifier=e_mod)
