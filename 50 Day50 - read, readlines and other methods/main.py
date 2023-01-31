'''readlines() method: The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.
The readlines() method reads all the lines of the file and returns them as a list of strings. '''

# f = open('file.txt', 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break

f = open('myfile.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in Maths is: {m1*2}")
    print(f"Marks of student {i} in English is: {m2*2}")
    print(f"Marks of student {i} in SST is: {m3*2}")
    print(line)


'''writelines() method: The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple. '''

# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()
