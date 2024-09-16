'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''
import json
from packaging import parse_packaging, calc_total_units, get_unit

rfile = open("data/packaging.txt", "r")
wfile = open("data/packaging.json", "w")
packages = []
for line in rfile:
    line = line.strip()
    package = parse_packaging(line)
    total_units = calc_total_units(package)
    unit = get_unit(package)
    print(line.strip()," => total units: ", total_units, unit)
    packages.append(package)
    
json.dump(packages, wfile, indent=4)