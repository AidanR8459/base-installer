import shutil
import os
import subprocess

# *Replace <path> with correct path
# **Replace <text> with correct text
# Still need to add correct logs



# Write

# file=open(path, "w")
# file.write(text)


# Add

# file=open(path, "a")
# file.write('\n'+text)


# Delete

# if os.path.exists(path):
#    os.remove(path)


# Check / MkDir

# if fp==1:
#   # For Files
#   if os.path.isfile(path)==True:
#       # Insert Required Command Here
#   else:
#       # Insert Required Command Here
#   if fp==2:
#       # For Directories
#       os.path.isdir(path)
#       if os.path.isdir(path)==False:
#           # Insert Required Command Here
#       else:
#           Mkdir()


# Rmdir

# If treedir == 1, not a Tree Directory. If treedir == 2, Tree Directory.

# treedir=int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
# if treedir==1:
#   os.rmdir(path)
# if treedir==2:
#   shutil.rmtree(path)



# Defining Required Functions

def OpenFile():
        try:
            os.startfile(path)
        except:
            # Insert Required Command Here


def Mkdir():
    os.makedirs(path)

