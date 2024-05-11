class BookStore:
    NoOfBook = 0
    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBook = BookStore.NoOfBook + 1

    def Display(self):
        print("Name of Book is ", self.Name)
        print("Author of book is ",self.Author)
        print("Number of books are ",self.NoOfBook)

def main():
    print("Enter book name")
    name = input()
    print("Enter Author of book " , name)
    author = input()
    obj1 = BookStore(name,author)
    obj1.Display()

    print("Enter book name")
    name = input()
    print("Enter Author of book " , name)
    author = input()
    obj2 = BookStore(name,author)
    obj2.Display()

if __name__ == "__main__":
    main()

    