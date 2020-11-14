

def secsort(data, n):
    if(n > 0):
        maxi = fmaxi(data, n)
        tmp = data[maxi]
        data[maxi] = data[n]
        data[n] = tmp
        print(data)
        secsort(data, n-1)


def fmaxi(data, m):
    if(m == 0):
        return m
    maxi = fmaxi(data, m-1)
    if(data[m] > data[maxi]):
        return m
    return maxi


data = [5, 2, 1, 3, 4]
secsort(data, len(data)-1)
