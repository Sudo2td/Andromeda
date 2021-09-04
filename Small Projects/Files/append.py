print("Append Content To Files")

content = input("Enter Content To Append to A file: ")
path = input("Enter the Path of the file: ")

File = open(str(path), "a")
File.write(str(content))

input("Press Enter to Exit: ")