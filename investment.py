start = 100000

for i in range(10*12*2):
    invest = start/4
    end = invest*1.05
    start = invest*3 + end
    print(start)
