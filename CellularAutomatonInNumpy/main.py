import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
""" 
get_shifted_grid is a function to get the grid, but shifted with looping borders. 
E.g:
	[[0,1,2],
	 [3,4,5]]

	with (row_shift=1, col_shift=0) would return:
	[[1,2,0],
	 [4,5,3]] """
def get_shifted_grid(grid,row_shift,col_shift):
	left = grid[:,:col_shift]
	right = grid[:,col_shift:]
	row_shifted_grid = np.concatenate([right,left],axis=1)
	up = row_shifted_grid[:row_shift]
	down = row_shifted_grid[row_shift:]
	fully_shifted_grid = np.concatenate([down,up],axis=0)
	return fully_shifted_grid
""" 
step is a function to update the grid with a specified rule. First, the values of neighbouring pixels are collected."""
def step (grid):
	left = get_shifted_grid(grid,0,-1)
	upper_left = get_shifted_grid(grid,-1,-1)
	up = get_shifted_grid(grid,-1,0)
	upper_right = get_shifted_grid(grid,-1,1)
	right = get_shifted_grid(grid,0,1)
	lower_right = get_shifted_grid(grid,1,1)
	down = get_shifted_grid(grid,1,0)
	lower_left = get_shifted_grid(grid,1,-1)

	new_grid = (left == 0) * (upper_right == 1)
	return new_grid

"""
Here the general parameters are set: The size of the grid, the number of iterations"""

steps = 200
grid_rows = 200
grid_cols = 100

grid = np.random.randint(0,2,(grid_rows,grid_cols)) # Creating grid with values either 0 or 1

px = 1/plt.rcParams['figure.dpi'] # get the width of the screen inch in pixels, as plt.figure() takes size in inches.
fig = plt.figure(figsize=(grid_cols*px,grid_rows*px))
ims = []
for i in range(steps):
	grid = step(grid) # up0ate the grid, according to the rule in the step function.
	ims.append([plt.imshow(grid, cmap="gray",aspect="equal", interpolation="none", animated=True, vmin=0,vmax=1)])	
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,repeat_delay=1000)
plt.axis('off')	
writergif = animation.PillowWriter(fps=10) 
ani.save("CellularAutomaton.gif", writer=writergif)


