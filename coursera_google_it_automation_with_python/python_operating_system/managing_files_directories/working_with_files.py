with open("novel.txt", "w") as file:
    file.write("Hello")

import os
import datetime
# os.remove("novel.txt")

# os.rename("first_draft.txt", "finished_masterpiece.txt")

timestamp = os.path.getmtime("finished_masterpiece.txt")
print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.isfile("finished_masterpiece.txt"))

print(type(os.path.abspath("finished_masterpiece.txt")))
