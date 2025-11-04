filename = input("Enter filename (e.g., file.txt): ")
with open(filename, "r") as f:
    text = f.read().lower()
words = text.split()
if words:
    most = max(words, key=words.count)
    print(most, words.count(most))
else:
    print("No words found.")