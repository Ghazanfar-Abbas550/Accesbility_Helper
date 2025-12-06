import os

for f in os.listdir("templates"):
    print("Checking:", f)
    path = os.path.join("templates", f)
    with open(path, "rb") as fp:
        head = fp.read(4)
    print("First bytes:", head)
