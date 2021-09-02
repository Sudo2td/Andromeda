import os

print("""
This file download's the latest version of Andromeda. 
But it create's a new folder with the latest version. 
If you want to update this Andromeda project then I
recommend using Update.py which will update your project.

If you don't want to upgrade or don't like that way then you can 
use this method. 

Requirements:
You need these installed:
Git
""")

input("I have git installed(Press Enter to continue): ")
input("I am ready to download(Press Enter to continue): ")

os.system("git clone https://github.com/Sudo2td/Andromeda")