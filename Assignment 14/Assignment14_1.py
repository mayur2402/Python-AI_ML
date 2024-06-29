from sys import argv
import pandas as pd
from sklearn import metrics, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def CheckAccuracy(knn,features,play_encoded):
    x_train,x_test,y_train,y_test = train_test_split(features,play_encoded,test_size=0.5) 

    y_pred = knn.predict(x_test)
    accuracy = metrics.accuracy_score(y_test,y_pred)

    print(accuracy)

def TestData(knn,testData):
    predict = knn.predict(testData)
    return predict

def TrainData(csv):
    
    Whether_encoded = csv["Whether"]
    Temperature_encoded = csv["Temperature"]
    play_encoded = csv["Play"]

    features = list(zip(Whether_encoded,Temperature_encoded))
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(features,play_encoded)

    return knn,features,play_encoded

def Manipulatedata(csv):
    pre = preprocessing.LabelEncoder()

    csv["Whether"] = pre.fit_transform(csv["Whether"])
    csv["Temperature"] = pre.fit_transform(csv["Temperature"])
    csv["Play"] = pre.fit_transform(csv["Play"])

    return csv

def ReadCSV(FileName):
    csv = pd.read_csv(FileName)
    return csv

def CheckWhether(whether):
    if(whether.lower() == "sunny"):
        return  0
    elif(whether.lower() == "overcast"):
        return  1
    elif(whether.lower() == "rainy"):
        return  2
    else:
        print("Invalid whether details please enter sunny, overcast or rainy")
        return -1
    
def CheckTemparature(temp):
    if(temp.lower() == "hot"):
        return  0
    elif(temp.lower() == "mild"):
        return  1
    elif(temp.lower() == "cool"):
        return  2
    else:
        print("Invalid temperature details please enter hot, mild or cool")
        return -1

def main():
    print("-----------Play Predictor Classification------------")

    CSV_File_Name = "PlayPredictor.csv"

    csv = ReadCSV(CSV_File_Name)

    csv = Manipulatedata(csv)

    knn,feature,label = TrainData(csv)

    whether = CheckWhether(argv[1])

    if(whether == -1):
        exit()
    temp = CheckTemparature(argv[2])

    if(temp == -1):
        exit()

    output = TestData(knn,[[whether,temp]])

    if(output == 1):
        print("You can play")
    else:
        print("You cannot play")

    CheckAccuracy(knn,feature,label)
    

if __name__ == "__main__":
    main()