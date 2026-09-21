class String:
    def getString(self):
        self.text=input("Enter a string: ")
    def printString(self):
        print(self.text.upper())

s=String()
s.getString()
s.printString()