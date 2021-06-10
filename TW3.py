w1=w2=None
x1list=x2list=None
expectedOp=None
t=None
a=None

def main():
    w1, w2 = -0.2, 0.4
    x1list, x2list = [0,0,1,1], [0,1,0,1]
    expectedOp = [0,1,1,1]
    t = 0
    a = 0.2
    epochs = 0
    actualOp = []
    print("OR Gate:")
    print("Epoch X1 X2 Expected_Y Actual_Y Error  w1  w2")
    while expectedOp!=actualOp:
        epochs+=1
        actualOp = []
        for i in range(4):
            actualOp.append(1 if w1*x1list[i]+w2*x2list[i]>t else 0)
            err = expectedOp[i] - actualOp[i]
            if err:
                w1+= a*x1list[i]*err
                w2+= a*x2list[i]*err
            print(epochs,'   ',x1list[i],'',x2list[i],'',expectedOp[i],'\t      ',actualOp[i],'      ',err,'   ',w1,w2)

    print("------------------------------------------------------------------------")

    w1, w2 = 1.2, 0.6
    x1list, x2list = [0,0,1,1], [0,1,0,1]
    expectedOp = [0,0,0,1]
    t = 1
    a = 0.5
    epochs = 0
    actualOp = []
    print("AND Gate:")
    print("Epoch X1 X2 Expected_Y Actual_Y Error  w1  w2")
    while expectedOp!=actualOp:
        epochs+=1
        actualOp = []
        for i in range(4):
            actualOp.append(1 if w1*x1list[i]+w2*x2list[i]>t else 0)
            err = expectedOp[i] - actualOp[i]
            if err:
                w1+= a*x1list[i]*err
                w2+= a*x2list[i]*err
            print(epochs,'   ',x1list[i],'',x2list[i],'',expectedOp[i],'\t      ',actualOp[i],'      ',err,'   ',w1,w2)

    print("------------------------------------------------------------------------")
    
    w1 = -0.04
    x1list = [0,1]
    expectedOp = [1,0]
    t = -0.1
    a = 0.5
    epochs = 0
    actualOp = []
    print("NOT Gate:")
    print("Epoch X1 Expected_Y Actual_Y Error    w1")
    while expectedOp!=actualOp:
        epochs+=1
        actualOp = []
        for i in range(2):
            actualOp.append(1 if w1*x1list[i]>t else 0)
            err = expectedOp[i] - actualOp[i]
            if err:
                w1+=a*x1list[i]*err
            print(epochs,'   ',x1list[i],'',expectedOp[i],'\t      ',actualOp[i],'      ',err,'   ',w1)
    
if __name__=="__main__":
    main()
