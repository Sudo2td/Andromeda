print("Read Files")

path = print("Please Enter the Path of a file: ")

File = open(str(path), "r")
data = File.read()

print(data)
input("Press Enter to Exit")