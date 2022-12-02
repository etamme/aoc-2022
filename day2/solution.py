import sys
# part 1
shapes = {"A": 1, "X": 1, "B": 2, "Y":2, "C": 3, "Z": 3}
pointmap = {"AX": 3, "AY": 6, "AZ": 0, "BX": 0, "BY": 3, "BZ": 6, "CX": 6, "CY": 0, "CZ": 3}

points = 0
part2points = 0
for line in sys.stdin:
  line = line.strip()
  if(line):
    P1,P2 = line.split()
    points += shapes[P2] + pointmap[P1+P2]
    
# part 2
    move = ["X","Y","Z"]
    if(P2=="Z"):
      P2 = move[(shapes[P1],0) [shapes[P1] >2]]
    elif P2=="Y":
      P2 = move[shapes[P1]-1]
    elif P2=="X":
      P2 = move[(shapes[P1]-2,2) [shapes[P1]-2 <0]]
    part2points += shapes[P2] + pointmap[P1+P2]
# output
print("part1 points:"+str(points))
print("part2 points:"+str(part2points))
