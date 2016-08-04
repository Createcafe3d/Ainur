import argparse
import math


class GCodeWriter:

    def __init__(self, input_seq="", nozzle_diameter=0.4, e_modifier=12.0):
        """
        GCodeWriter constructor
        """
        self.num_input = input_seq
        self.prev_e_value = 0
        input_lines = input_seq.split("\n")
        self.gcode_output = ""
        self.initialize_gcode(nozzle_diameter=nozzle_diameter)
        g1_lines = ""
        for line in input_lines:
            input_members = line.split(",")
            g1_lines += self.construct_g1_line_from_array(input_members, e_modifier) + "\n"
        self.gcode_output += ";Layer count: {}\n;LAYER:0\n".format(len(g1_lines.split('\n'))-1)
        self.gcode_output += "G10\nG0\n;TYPE:\nG11\n" + g1_lines
        print self.gcode_output

    def initialize_gcode(self, nozzle_diameter):
        self.gcode_output += ";FLAVOR:UltiGCode\n;TIME:4198\n;MATERIAL:10958\n;MATERIAL2:0\n"
        self.gcode_output += ";NOZZLE_DIAMETER:{}".format(round(nozzle_diameter, 6))
        self.gcode_output += "\n;NOZZLE_DIAMETER2:{}".format(round(nozzle_diameter, 6))
        self.gcode_output += "\n\n"


    def construct_g1_line_from_array(self, input_array, e_modifier):
        gcode = "G1 "
        coords = ['X', 'Y', 'Z']
        for idx, entry in enumerate(input_array):
            gcode += coords[idx] + entry + " "
        gcode += "E"
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
