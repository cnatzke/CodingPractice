#The program modifies the beam radius in the run macro for beam radius simulations

import fileinput 
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("file", help="File to be changed")
parser.add_argument("radius",help="Beam Radius in mm")
parser.add_argument("events", help="Number of decay events in millions (10=10e6)", type=int)
args = parser.parse_args()

events=str(int(args.events*1e6))
radius=str(float(args.radius))

#with open(args.file,'r') as file:
#    data=file.readlines()
#
#data[101]="/gps/pos/radius "+radius+" mm\n"
#data[110]="/run/beamOn "+events+"\n"
#
#with open(args.file,'w') as output_file:
#    output_file.writelines(data)
#

for line in fileinput.input([args.file], inplace=True, backup='.bk'):

    if line.strip().startswith('/gps/pos/radius'):
        line ="/gps/pos/radius "+radius+" mm\n"

    if line.strip().startswith('/run/beamOn'):
        line ="/run/beamOn "+events+"\n"
    sys.stdout.write(line)
print("Done")
