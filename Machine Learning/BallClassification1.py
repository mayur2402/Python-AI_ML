from sklearn import tree

def MarvellousClassifier(wieght,surface):
    Features = [[35,1],[47,1],[48,1],[90,0],[92,0]]

    Label = [1,1,1,0,0]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features,Label)


    ret = obj.predict([[wieght,surface]])

    if(ret == 1):
        print("Your Object looks like tennis ball")
    else:
        print("Your object looks like cricket ball")

def main():
    print("Demonstration of machine learning")

    print("Enter Weight of ball")
    weight = int(input())

    print("Enter type of surface rough/smooth")
    surface = input()

    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("Enter valid surface")
        exit()

    MarvellousClassifier(weight,surface)
    
if __name__ == "__main__":
    main()