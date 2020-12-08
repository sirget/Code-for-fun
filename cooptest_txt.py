file = open('./test_data.txt')

year = []
type = []
rank = []
name = []
lname = []
datalist = []

for data in file:
    list = data.split(" ")
    datalist.append(list)
    year.append(list[0])
    type.append(list[1])
    rank.append(list[2])
    name.append(list[3])
    list[4] = list[4].rstrip("\n")
    lname.append(list[4])


def showlistfrom(start, end):
    for i in datalist:
        if(i[0] >= start and i[0] <= end):
            print(i)


def sort():
    datalist.sort(key=lambda x: len(x[1]))


def showlist():
    for i in datalist:
        print(i)


# print(datalist)
sort()
showlist()
#showlistfrom("2005", "2009")
