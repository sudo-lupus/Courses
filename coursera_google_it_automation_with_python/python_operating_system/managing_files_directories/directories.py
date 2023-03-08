import os

#Get current working directory
print(os.getcwd())

os.mkdir("new_dir")
os.rmdir("new_dir")

os.chdir("website")

dir = os.getcwd()
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{name} is a directory")
    else:
        print(f"{name} is a file")