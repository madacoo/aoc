import knothash


def bits(s):
    "Takes a string of hexadecimal digits and returns a list of bits."
    result = []
    for c in s:
        result += list(bin(int(c, 16))[2:].zfill(4))
    return result


def regionify(i, j, char):
    """Assuming a grid of bits and indices i, j
       mutate grid to represent region with char
       return True if new region found, otherwise False.
    """
    if i < 0 or j < 0 or i > 127 or j > 127: return False
    if grid[i][j] != '1' : return False
    grid[i][j] = char
    regionify(i+1, j,   char)
    regionify(i,   j+1, char)
    regionify(i-1, j,   char)
    regionify(i,   j-1, char)
    return True


def solve(grid):
    squares_used = sum(row.count('1') for row in grid)
    return squares_used


def solve2():
    region_count = 0
    seen_char = '.'
    for i in range(128):
        for j in range(128):
            if regionify(i, j, seen_char):
                region_count += 1
    return region_count
        

key = "vbqugkhl"
grid = [bits(knothash.hash(key + "-{}".format(i)))
        for i in range(128)]
print(solve(grid)) # 8148
print(solve2()) # 1180
