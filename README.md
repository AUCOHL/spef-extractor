# SPEF Extractor
A Python library that reads LEF and DEF files, extracts the RC parasitics and generates their corresponding SPEF file.

# Dependencies
* Python 3.6+ with PIP

# Installation
`python3 -m pip install spef-extractor`

# Usage
````
spef_extractor <lef_file_path> <def_file_path> <wire_model which can be L or Pi> <edge_capacitance_factor which is a value between 0 and 1 where the default is 1>
```

For example:

```
python3 main.py osu035.lef rle_rec.def L 1
````


where `osu035.lef` is the provided lef file and `rle_rec.def` is its corresponding def file. Aftwards, we extract the RC parasitics and output them in a SPEF file named `rle_rec.spef` (holds the same name as the def file by default).

# The Development Process
## Parsing
In order to parse the lef and def files, we used [trimcao](https://github.com/trimcao)'s def and lef parser.


## Testing
- Initially, we tested the generated SPEF manually. This was done through checking a number of nets, and comparing the parasitics in the file with the theoretical value.
- Later on, we tested using OpenSTA to verify that the produced SPEF file is syntax error free. OpenSTA was able to successfuly read the SPEF file and produce timing reports based on the parasitics provided.
- Additionally, we used OpenSTA to compare the delays for multiple designs using publicly available reference SPEF files vs. our generated SPEF files.

## Assumptions 
During our development, we had to make some assumptions to for the sake of simplicity:
  1. It is assumed that the values that do not exist in the LEF file are considered to be 0.
  2. We represented each wire segment as a single resistance and a capacitance (In the L model)
  3. We consider the capacitance of a segment to be at the end node of the segment (In the L model)
  4. Testing was done using openSTA that verified our SPEF is syntax error free.

## Limitations
  1. Testing was only done on a handful of designs and further testing might help
  2. Only Pi and L models are available to represent the resistance and capacitance of a segment (even for long wire segments)
  3. We don't handle the RC parasitics of the special nets
  
## Name Remapping
  1. We implemented an algorithm to rename long names.
  2. All nets are renamed to decrease the size of files.
  3. Names were remapped based on the standard remapping scheme of SPEF files.

## Acknowledgement:
  This was initially created for the Digital Design 2 Course CSCE3304 at the American University in Cairo under the supervision of Doctor Mohamed Shalan. Its development was ongoing afterwards as a part of an undergraduate research internship at the American Univeristy in Cairo.

## Original Authors:
  * Ramez Moussa - [Github Profile](https://github.com/ramezmoussa)
  * Hany Moussa - [Github Profile](https://github.com/hanymoussa)

# License
The Apache License, version 2.0. See `License`.
  
