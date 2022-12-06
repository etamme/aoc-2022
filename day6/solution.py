import sys

for line in sys.stdin:
  line = line.strip()
  index=0
  #part 1
  size = 4
  # part 2, change to size=14
  while True:
    if(len(line[index:index+size]) == len(set(line[index:index+size]))):
      print("marker: "+str(index+size))
      break
    else:
      index += 1