# v.0.1 based on youtube; original was .pyde filetype; will convert to javascript v.0.2
w, h = 1000, 1000

hex_size = 10 # size in pixels, for canvas plugin

grid_x_pixels = .9 * w
grid_y_pixels = .9 * h

sep_x = 3 * hex_size
sep_y = .86 * hex_size

grid_x = int(grid_x_pixels / sep_x) + 1
grid_y = int(grid_y_pixels / sep_y) + 1

def draw_hexagon(x, y, side):
  beginShape()
  vertex((x + side * sin(PI/2), y + side * cos(PI/2))) # vertex takes two params: (x, y)
  vertex((x + side * sin(PI/6), y + side * cos(PI/6)))
  vertex((x + side * sin(11 * PI/6), y + side * cos(11 * PI/6)))
  vertex((x + side * sin(3 * PI/2), y + side * cos(3 * PI/2)))
  vertex((x + side * sin(7 * PI/6), y + side * cos(7 * PI/6)))
  vertex((x + side * sin(5 * PI/6), y + side * cos(5 * PI/6))) # 6 calls for six corners of hex (vertices; not sides)
  endShape(CLOSE)

# def setup():
  # Create the Canvas
  