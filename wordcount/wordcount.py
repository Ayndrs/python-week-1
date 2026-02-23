#!python
text = open("story.txt", "r") #text is the object not the contents
d = dict() #created in heap to prepare for info
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split()

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, ":", d[key])
