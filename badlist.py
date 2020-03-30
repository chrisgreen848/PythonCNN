import os


mypath = "C:/Users/chris/"
file = mypath+ "instances_train2017.json"
badList = "C:/Users/chris/bad.txt"
folder = 'D:/textfiles/'

print("Starting now")
bad = []
it = 0
badFile = open(badList, "r")
for line in badFile:
    it += 1
    linesplit = line.split("/")
    temp = ""
    for i in range(len(linesplit)):
        temp= linesplit[i]
    temp = temp.split(".")
    bad.append(temp[0])

print("Bad list size is : ", len(bad))
check = 0
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".txt"):
             #print(os.path.join(root, file))
             splitfile = file.split(".")
             for i in range(len(bad)):
                 if splitfile[0] in bad[i]:
                     print("Img id matches : ", file)
                     check +=1
                     break

print("Found : ", check)
