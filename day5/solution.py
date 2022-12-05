import sys

stacks=[['H','T','Z','D'],
        ['Q','R','W','T','G','C','S'],
        ['P','B','F','Q','N','R','C','H'],
        ['L','C','N','F','H','Z'],
        ['G','L','F','Q','S'],
        ['V','P','W','Z','B','R','C','S'],
        ['Z','F','J'],
        ['D','L','V','Z','R','H','Q'],
        ['B','H','G','N','F','Z','L','D']]


""" for line in sys.stdin:
  line = line.strip()
  line_list = line.split(' ')
  box_count = int(line_list[1])
  from_stack = int(line_list[3])-1
  to_stack = int(line_list[5])-1

  for i in range(box_count):
    box=stacks[from_stack].pop()
    stacks[to_stack].append(box)

message=[]
for stack in stacks:
  message.append(stack[-1])
print(''.join(message)) """


for line in sys.stdin:
  line = line.strip()
  line_list = line.split(' ')
  box_count = int(line_list[1])
  from_stack = int(line_list[3])-1
  to_stack = int(line_list[5])-1
  boxes=stacks[from_stack][-box_count:]
  del stacks[from_stack][-box_count:]
  for box in boxes:
    stacks[to_stack].append(box)

message=[]
for stack in stacks:
  message.append(stack[-1])
print(''.join(message))

