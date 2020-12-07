import json

#file = open('./data_train.json', encoding="utf8")
file = open('./data_train_test.json', encoding="utf8")
data = json.loads(file.read())


def sortFunction(value):
    return value['IdTrain']


sorted_data = sorted(data, key=sortFunction)
for i in sorted_data:
    print(i)
