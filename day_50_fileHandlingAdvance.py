# Day 50
# file handling advanced.

# readline()
# f = open('requirement.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     val1 = int(line.split(",")[0])
#     val2 = int(line.split(",")[1])
#     val3 = int(line.split(",")[2])
#     print(f"value {i}: {val1}")
#     print(f"value {i}: {val2}")
#     print(f"value {i}: {val3}")
    # print(line)

# writeline()
f = open('text.txt', 'w')
line = ['Ironman', 'loki', 'thor', 'black widows', 'natasha']
for i in line:
    f.write(i + "\n")
f.close()