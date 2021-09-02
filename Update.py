import os
import time


print("""
This will Update Andromeda. Note: You do need:

Internet Connection
Git

This might take any amount of time depending on your internet connection and the amount
of versions you need to update
""")

input("Press Enter to Continue: ")
input("This will update THIS PROJECT which might lose some important data which you won't be able to get back: ")
input("are you sure? ")
print("Project will update in 10 seconds, you can close the program if you change your mind")
time.sleep(10)

os.system("git pull")

input("Press Enter to Exit: ")