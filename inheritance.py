class Phone:
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")

class Sumsung(Phone):
    def photo(self):
        print("You can take photo")

s= Sumsung()
s.call()
s.message()
s.photo()
print(issubclass(Sumsung,Phone))