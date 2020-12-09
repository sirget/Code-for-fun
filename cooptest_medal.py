filename = "./medals.txt"
datalist = []
file = open(filename, "r", encoding="utf8")
medal = {}
medal_list = []
column = []


def read():
    for data in file:
        tmp = data.split(",")
        tmp[3] = tmp[3].rstrip("\n")
        if len(column) == 0:
            column.append(tmp)
        else:
            datalist.append(tmp)
    print("Read Complete")


def closefile():
    file.close()


def printlist():
    if(len(datalist) == 0):
        print("Empty list")
    else:
        for data in datalist:
            print(data)


def totalgoldmedal():
    for data in datalist:
        if data[1] not in medal.keys():
            medal[data[1]] = int(data[2])
        else:
            medal[data[1]] += int(data[2])
    for x, y in medal.items():
        medal_list.append([x, y])
    print(medal_list)


def sortdata(data_in, i, rev):
    data_in.sort(key=lambda x: x[i], reverse=rev)
    print(data_in)


while(True):
    command = input("Command : ")
    if command == "read":
        read()
    if command == "print":
        printlist()
    if command == "exit":
        closefile()
        break
    if command == "total":
        totalgoldmedal()
    if command == "sortmedal":
        sortdata(medal_list, 1, True)
        sortdata(medal_list, 1, False)
