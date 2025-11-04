filename = input("Enter filename ( file.txt): ")
with open(filename, "r") as f:
    lines = f.readlines()
for line in lines[-2:]:
    print(line, end="")