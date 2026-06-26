class Book:
    def __init__(self,title,author,is_unavailable):
        self.title=title
        self.author=author
        self.is_unavailable=is_unavailable
    def checkout(self):
        self.is_unavailable=True
    def return_book(self):
        self.is_unavailable=False
    def status(self):
        if self.is_unavailable==True:
            print("unavailable")
        else:print("available")
'''
- Class: Book
- attributes: title, author, is_available
- methods:
    checkout()   → marks book as unavailable
    return_book() → marks book as available
    status()     → prints if book is available or not
'''