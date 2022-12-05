import sys
# part 1
def getval(x):
  return (ord(x)-96, ord(x)-38) [x.isupper()]

def part1():
  total = 0
  c1,c2 = {},{}
  for line in sys.stdin:
    line = line.strip()
    line_as_list = list(line)
    c1,c2 = line_as_list[:len(line_as_list)//2],line_as_list[len(line_as_list)//2:]
    total += getval(str(next(iter(set(c1) & set(c2)))))
  return str(total)

def part2():
  total,i = 0,0
  lines = []
  for line in sys.stdin:
    lines.append(list(line.strip()))
    if(len(lines)==3):
      line_as_list = list(line)
      total += getval(str(next(iter(set(lines[0]) & set(lines[1]) & set(lines[2])))))
      lines=[]
  return str(total)

# output
#print("sum of priorities:"+part1())
print("badge priorities:"+part2())

