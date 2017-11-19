import numpy as np

class grid:
	def __init__(self, fpath):
		if fpath is not None:
			with open(fpath, "r") as f:
				self.ncols = int(f.readline().strip().split()[1])
				self.nrows = int(f.readline().strip().split()[1])
				self.xllcorner = float(f.readline().strip().split()[1])
				self.yllcorner = float(f.readline().strip().split()[1])
				self.cellsize = float(f.readline().strip().split()[1])
				self.nodata = float(f.readline().strip().split()[1])
				self.yurcorner = self.yllcorner + (self.nrows * self.cellsize)

				self.grid = np.loadtxt(f)
		else:
			self.ncols = 0
			self.nrows = 0
			self.xllcorner = 0.0
			self.yllcorner = 0.0
			self.cellsize = 0.0
			self.nodata = 0.0
			self.yurcorner = 0.0

			self.grid = None

	def __str__(self):
		return "cols: %s\nrows: %s\nxllcorner: %s\nyllcorner: %s\ncellsize: %s\nnodata: %s\ngrid: %s" % (self.ncols, self.nrows, self.xllcorner, self.yllcorner, self.cellsize, self.nodata, self.grid.shape)

	def write(self, outputPath):
		with open(outputPath, "w") as f:
			f.write("NCOLS %s\nNROWS %s\nXLLCORNER %s\nYLLCORNER %s\nCELLSIZE %s\nNODATA_VALUE %s\n" % 
				(self.ncols, self.nrows, self.xllcorner, self.yllcorner, self.cellsize, self.nodata))
			np.savetxt(f, self.grid, fmt="%f")
			
	def inspect(self, x, y):
		xIndex = int(round((x - self.xllcorner) / self.cellsize, 0))
		yIndex = int(round((self.yurcorner - y) / self.cellsize, 0))
		return self.grid[yIndex, xIndex]

# if __name__ == "__main__":
# 	print "reading grid"
# 	myGrid = grid(r"N:/TUFLOW/117071/check/HayToBalranald_01/HayToBalranald_01_DEM_Z.asc")

# 	x = 208656.214983
# 	y = 6160964.91988
# 	val = 65.803
# 	print myGrid

# 	print "inspecting grid"
# 	print myGrid.inspect(x, y)