grid = [
  ["", "", ""],
  ["", "", ""],
  ["", "", ""]
]

def display_grid():
    for row in grid:
      print("+---+---+---+\n| ", end='')
      for slot in row:
        if slot: # if not empty
          print(slot, end=' | ')
        else:
          print(" ", end=' | ')
      print()
    print("+---+---+---+")

def scan_grid(x, y, player):
  if (grid[-y][0] == grid[-y][1] == grid[-y][2] == player or
      grid[0][x-1] == grid[1][x-1] == grid[2][x-1] == player or
      grid[0][0] == grid[1][1] == grid[2][2] == player or
      grid[0][2] == grid[1][1] == grid[2][0] == player):
      return f"{player} wins!"
  elif 1 == 2:
    """
    TODO Make something to detect a draw
    """
    pass
  else:
    return None

def play(player):
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
          
    x, y = coords.values()
    while True:
      if not grid[-y][x-1]: # Make sure empty
        grid[-y][x-1] = player
        break
      else:
        print("Sorry, you can't play there.")
        
    check = scan_grid(x, y, "X" if player else "O")
    if check: # Check for winner / draw
      print(check)
      exit(1)
    
def main():
    player = True # = X
    while True:
      display_grid()
      play("X" if player else "O")
      player = not player

if __name__ == "__main__":
  main()
