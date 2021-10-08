# need to count number of neighbouring different cells in rows and columns
import operator

# oneliner
def islandPerimeterOneLine(grid):
    return sum(sum(map(operator.ne, [0] + row, row + [0])) for row in grid + list(map(list, zip(grid))))


# clarifying multiliners
def num_of_diff_neighbour_cells_in_a_row(row):
    return sum(map(operator.ne, [0] + row, row + [0]))

def islandPerimeter(grid):
    grid_rows = grid
    grid_cols = list(map(list, zip(grid_rows)))
    num_diff_neigh_cells_in_grid_rows = sum(num_of_diff_neighbour_cells_in_a_row(row) for row in grid_rows + grid_cols)
    return num_diff_neigh_cells_in_grid_rows

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

assert islandPerimeter(grid) == 16
assert islandPerimeterOneLine(grid) == 16
# based on https://leetcode.com/problems/island-perimeter/discuss/95007/Short-Python