from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def main():

    iris = load_iris()

    Features = iris.data
    Labels = iris.target

    data_train,data_test,target_train,target_test = train_test_split(Features,Labels,test_size = 0.5)

    print(len(data_train))
    print(len(data_test))
    
    obj = tree.DecisionTreeClassifier()

    obj.fit(data_train,target_train)

    ret = obj.predict(data_test)

    print(ret)
    print(target_test)

    Accuracy = accuracy_score(target_test,ret)

    print(Accuracy * 100)

if __name__ == "__main__":
    main()