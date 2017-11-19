import os
import sys
from ascgrid import grid as AscGrid

def main():
	if len(sys.argv) != 3:
		print "Usage: python tiler.py gridpath numslices"
		exit(1)

	gridpath = sys.argv[1]
	if not os.path.exists(gridPath):
		print "%s does not exist!" % gridPath
		exit(2)
	gridpath_noextension = gridpath[:gridpath.rfind('.')]

	try:
		split = int(sys.argv[2])
	except ValueError:
		print "%s is not a valid integer" % sys.argv[2]
		exit(3)

	print "Reading in grid"
	grid = AscGrid('murrumbidgee2009_11.asc')	


	# set the number of cols/rows of all but the last grid to the integer division
	# of the existing grid by the split
	ncols = grid.ncols / split
	nrows = grid.nrows / split

	print "Writing tiled grids"
	for i in xrange(split):
		for j in xrange(split):
			gridi = i
			gridj = (split - 1 - j) #reverse the index of j as ASCII grids are read bottom to top by GIS programs

			# initialise sub-grid with size
			thisGrid = AscGrid(None)
			thisGrid.ncols = ncols
			thisGrid.nrows = nrows
			# set its origin based cartesian coordinates
			thisGrid.xllcorner = grid.xllcorner + gridi * ncols * grid.cellsize
			thisGrid.yllcorner = grid.yllcorner + gridj * nrows * grid.cellsize
			# copy the common data
			thisGrid.cellsize = grid.cellsize
			thisGrid.nodata = grid.nodata
			# extra attribute for internal use only to speed up calculation of extents, not used by GIS programs
			thisGrid.yurcorner = thisGrid.yllcorner + (thisGrid.nrows * thisGrid.cellsize)
			# take the slice of the grid for this sub-grid
			thisGrid.grid = grid.grid[j * nrows:(j+1) * nrows, i * ncols: (i+1) * ncols]
			thisGrid.write("{}_{}{}.asc".format(gridpath_noextension, i, j))

if __name__ == "__main__":
	main()