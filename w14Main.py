class Dog(object):
    def __init__(self,name):
        self.name=name
    def getname(self):
        print "my dog name is",self.name
    def talk(self):
        print "mung mung"
class ShihTzuDog(Dog):
    def talk(self):
        print "si si"
class Maltese(Dog):
    def talk(self):
        print "wal wal"
def dogsound():
    mydog=Dog('poppy')
    mydog.talk()
    myshitzu=ShiTzuDog('poppy')
    myshitzu.talk()
    mymaltese=MalteseDog('poppy')
    mymaltese.talk()
    
def lab14():
    dogsound()
    
def main():   
    lab14()

if __name__=="__main__":
    main()