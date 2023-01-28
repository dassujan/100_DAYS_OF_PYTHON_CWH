import os

# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file
os.close(f)

# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)

# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']

# Create a new directory
os.mkdir("newdir")


# # Run the "ls" command and print the output
# output = os.system("ls")
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# # Run the "ls" command and get the output as a file-like object
# f = os.popen("ls")

# # Read the contents of the output
# output = f.read()
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# # Close the file-like object
# f.close()