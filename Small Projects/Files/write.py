print("Write Content To Files")
print("This will Delete all existing content on the file.")

content = input("Enter Content To Writw to A file: ")
path = input("Enter the Path of the file: ")

File = open(str(path), "w")
File.write(str(content))

input("Press Enter to Exit: ")