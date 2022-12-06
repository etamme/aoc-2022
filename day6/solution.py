import sys
for line in sys.stdin:
  line = line.strip()
  # for part 2, change to size=14
  size = 4
  for index in range(len(line)):
    if(len(line[index:index+size]) == len(set(line[index:index+size]))):
      print("marker: "+str(index+size))
      break