line = open("/home/etamme/sandbox/aoc-2022/day6/input.txt", "r").read().strip()
size = 4 # for part 2, change to size=14
for index in range(len(line)):
  if(len(line[index:index+size]) == len(set(line[index:index+size]))):
    print("marker: "+str(index+size))
    break