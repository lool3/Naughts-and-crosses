grid = [
  [" ", " ", " "],
  [" ", " ", " "],
  [" ", " ", " "]
]

def display_grid():
    for row in grid:
      print("+---+---+---+\n| ", end='')
      for slot in row:
        print(slot, end=' | ')
      print()
    print("+---+---+---+")
    
def get_coords():
    coords = {
      "X":0,
      "Y":0
    }
    for axis in coords: # For X, Y
      while True:
        try:
          coords_input = int(input(f"{axis} coordinate: "))
          if coords_input in range(1,4): # Allow 1, 2 or 3
            coords[axis] = coords_input
            break
          else:
            print("Coordinates not in range")
            continue
        except ValueError:
          print("That's not an integer!")
    return coords
    
def plot_coords():
    x, y = coords.values()
    grid[-y][x-1] = "X" # TODO change X to 'X' or 'O' depending on who's turn
    
display_grid()
coords = get_coords()
plot_coords()
display_grid()
