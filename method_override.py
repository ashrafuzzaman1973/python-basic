class Phone:
    def __init__(self):
        print("I am phone class")

class Sumsung(Phone):
    def __init__(self):
        super().__init__()
        print("I am sumsung class")

s= Sumsung()
