from sklearn import tree

def main():
    print("Demonstration of machine learning")

    Features = [[35,1],[47,1],[48,1],[90,0],[92,0]]

    Label = [1,1,1,0,0]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features,Label)


    print(obj.predict([[35,0]]))
    print(obj.predict([[43,0]]))
    
if __name__ == "__main__":
    main()