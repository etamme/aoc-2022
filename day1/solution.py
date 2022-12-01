# part 1
import sys
cal = 0
elves = []
for line in sys.stdin:
  line = line.strip()
  if line == "":
    elves.append(cal);cal=0  
  else:
    cal += int(line)
max_cal = max(elves)
print("elf "+str(elves.index(max_cal))+" has the most calories, "+ str(max_cal))

# part 2
elves.sort(reverse=True)
top_three = sum([ elves[i] for i in [0,1,2]])
print("top three elves are carrying "+str(top_three)+" calories")