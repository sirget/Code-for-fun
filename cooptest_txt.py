file = open('./test_data.txt')


datalist = []

for data in file:
    list = data.split(" ")
    datalist.append(list)
    list[4] = list[4].rstrip("\n")


def showlistfrom(start, end):
    for i in datalist:
        if(i[0] >= start and i[0] <= end):
            print(i)


def sortbylen():
    datalist.sort(key=lambda x: len(x[3]))


def showlist():
    for i in datalist:
        print(i)


# print(datalist)
sortbylen()
showlist()
#showlistfrom("2005", "2009")
