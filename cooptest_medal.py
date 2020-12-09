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
    print(column)


def closefile():
    file.close()


def add(y, c, q, s):
    datalist.append([y, c, q, s])


def remove():
    index = 0
    for i in datalist:
        if i[1] == "Thailand":
            datalist.pop(index)
        index += 1


def rewrtie():
    wr = open("./rewrite.txt", "w")
    wr.write(column[0][0] + " " + column[0][1] + " " +
             column[0][2] + " " + column[0][3] + "\n")
    for data in datalist:
        wr.write(data[0] + " " + data[1] + " " +
                 data[2] + " " + data[3] + "\n")
    wr.close()


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
    if command == "re":
        rewrtie()
    if command == "move":
        remove()
