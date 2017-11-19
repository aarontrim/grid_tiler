# grid_tiler
#### Specification
Python 2.7 script that takes an ASCII grid projected in a cartesian coordinate system (eg GDA94) and splits it into x by x tiles without any interpolation as per standard GIS libraries.
Useful for splitting large grids such as DEMs for memory reasons while leaving the value at each projected point exactly the same.

#### Usage
```
python tiler.py gridpath numslices
```
Where gridpath is the path to your .asc file, and numslices in the number of slices **in each direction**. For example a numslices value of 2 will slice it into a 2x2 grid or 4 tiles.