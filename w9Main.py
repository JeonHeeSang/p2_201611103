import matplotlib
import matplotlib.pyplot as plt
def charCount():
    d=dict()
    sentence=raw_input("input word :")
    for c in sentence:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

def countDigitsLetter(word):
    d=dict()
    d={"number":0, "word":0}
    for i in word:
        if i.isdigit()==True:
            d["number"]=d["number"]+1
        elif i.isdigit()==False:
            d["word"]=d["word"]+1
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

myhome=set()
yourhome=set()
myhome={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
yourhome={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook ', 'recorder'}
def Mine():
    print myhome.difference(yourhome)
def Yours():
    print yourhome.difference(myhome)
def Both():
    print myhome.intersection(yourhome)
def All():
    print myhome.union(yourhome)
def Count():
    d=dict()
    for i in myhome:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in yourhome:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print d        
def lab9():
    charCount()
    word=raw_input("input word")
    countDigitsLetter(word)
    Mine()
    Yours()
    Both()
    All()
    Count()
def main():
    lab9()

main()
raw_input("zzzzz:")
