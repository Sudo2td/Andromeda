import os
modules = ["youtube-dl", "pafy"]
print("""
This file will simply install ever pip package needed to use Andromeda
""")
input("Press Enter to Continue: ")
for module in modules:
   os.system(f"pip install {module}")
input("Press Enter to Exit: ")
