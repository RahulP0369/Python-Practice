class BookStore:

    NoOfBooks = 0
    
    def __init__(self,a,b):
        self.Name = a
        self.Author = b
        BookStore.NoOfBooks +=1
    
    def Display(self):
        print("Book is: ", self.Name)
        print("Author is: ",self.Author)
        print("No of books",BookStore.NoOfBooks)

def main():

    obj1 = BookStore("Linux System Programming","Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()