from collections import namedtuple

lines = []
with open("input17.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)

Cube = namedtuple("Cube", "x y z w")

start_grid = {}
for idx, i in enumerate(lines):
    for jdx, j in enumerate(i):
        start_grid[Cube(x=jdx, y=idx, z=0, w=0)] = 1 if j == "#" else 0


def get_neighbours(cube, dim):
    r = [-1, 0, 1]
    neighbours = []
    for dx in r:
        for dy in r:
            for dz in r:
                if dim == 4:
                    for dw in r:
                        neighbours.append(Cube(cube.x + dx, cube.y + dy, cube.z + dz, cube.w + dw))
                else:
                    neighbours.append(Cube(cube.x + dx, cube.y + dy, cube.z + dz, 0))

    neighbours.remove(cube)
    return neighbours


def calculate_active_cubes(grid, dim):
    for _ in range(6):
        for cube in list(grid):
            for neighbour in get_neighbours(cube, dim):
                grid.setdefault(neighbour, 0)

        new_grid = {}
        for cube, val in grid.items():
            active_neighbours = sum([grid.get(neighbour, 0) for neighbour in get_neighbours(cube, dim)])
            new_grid[cube] = 1 if (active_neighbours == 2 and val == 1) or active_neighbours == 3 else 0
        grid = new_grid

    print(sum(x for x in grid.values()))


calculate_active_cubes(start_grid, 3)
calculate_active_cubes(start_grid, 4)
