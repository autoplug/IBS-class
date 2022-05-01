import random


file = open("english.txt", "r")
file = file.readlines()

lines = []
for line in file:
    line = line.replace("\n", "").strip()
    if line:
        lines.append(line)

file = open("dictionary.csv", "r")
file = file.readlines()
dictionary = []

for line in file:
    line = line.replace("\n", "").strip()
    if line:
        dictionary.append(line)


while True:
    rand = random.randint(0, len(lines))
    rand -= rand % 2
    rand += 1
    print(lines[rand])
    q = input("")
    print(lines[rand-1])
    q += input("-------------------------------------")

    word = dictionary[random.randint(0, len(dictionary))]
    word = word.split(",")
    print(f"[{word[0]}]")
    input()
    print(word[1])
    q = input("-------------------------------------")
    if q == "q":
        break
