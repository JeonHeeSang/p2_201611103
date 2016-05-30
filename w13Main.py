import os
def gm():
    try:
        fin1=open('python.txt', 'a')
        fin2=open('jhs.txt', 'r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e
def lab13():
    gm()
def main():
    lab13()
    input()
if __name__=="__main__":
    main()        