import math 
import random 
import csv 

def encode_class(mydata):
    classes = []
    for i in range(len(mydata)):
        if mydata[i][-1] not in classes:
            classes.append(mydata[i][-1])
    
    for i in range(len(classes)):
        for j in range(len(mydata)):
            if mydata[j][-1] == classes[i]:
                mydata[j][-1] = i
    return mydata

def splitting(mydata, ratio):
    train_num = int(len(mydata) * ratio)
    train = []
    test = list(mydata)
    while len(train) < train_num:
        index = random.randrange(len(test))
        train.append(test.pop(index))
    return train, test 

def groupUnderClass(mydata):
    dict = {}
    for i in range(len(mydata)):
        if mydata[i][-1] not in dict:
            dict[mydata[i][-1]] = []
        dict[mydata[i][-1]].append(mydata[i])
    return dict

def mean(numbers):
    return sum(numbers) / float(len(numbers))

def std_dev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

def meanAndStdDev(mydata):
    info = [(mean(attribute), std_dev(attribute)) for attribute in zip(*mydata)]
    del info[-1]
    return info 

def meanAndStdDevForClass(mydata):
    info = {}
    dict = groupUnderClass(mydata)
    for classValue, instances in dict.items():
        info[classValue] = meanAndStdDev(instances)
    return info 

def calculateGaussianProbability(x, mean, stdev):
    expo = math.exp(-(math.pow(x-mean, 2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev))*expo

def calculateClassProbabilites(info, test):
    probabilites = {}
    for classValue, classSummaries in info.items():
        probabilites[classValue] = 1
        for i in range(len(classSummaries)):
            mean, std_dev = classSummaries[i]
            x = test[i]
            probabilites[classValue] *= calculateGaussianProbability(x, mean, std_dev)
    return probabilites

def predict(info, test):
    probabilites = calculateClassProbabilites(info, test)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilites.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel

def getPredictions(info, test):
    predictions = []
    for i in range(len(test)):
        result = predict(info, test[i])
        predictions.append(result)
    return predictions

def accuracy_rate(test, predictions):
    correct = 0
    for i in range(len(test)):
        if test[i][-1] == predictions[i]:
            correct += 1
    return (correct / float(len(test))) * 100.0

if __name__ == '__main__':
    filename = r'C:\Users\nabee\Desktop\lab_4th\Artificial-Intelligence\naive_bayes\Iris.csv'
    mydata = csv.reader(open(filename, "rt"))
    mydata = list(mydata)
    mydata = encode_class(mydata)
    for i in range(len(mydata)):
        mydata[i] = [float(x) for x in mydata[i]]

    ratio = 0.7 
    train_data, test_data = splitting(mydata, ratio)
    print('Total number of examples are: ', len(mydata))
    print('Out of these, training set is: ', len(train_data))
    print('Test set is: ', len(test_data))

    info = meanAndStdDevForClass(train_data)

    predictions = getPredictions(info, test_data)
    accuracy = accuracy_rate(test_data, predictions)
    print("Model's accuracy is: ",accuracy)