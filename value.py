import copy
x = 82.0
delta = 0
array = [['y','y','y','y','y','y'],
        ['y','y','y',x,'y','y'],
        ['y',0, 0, 0, 0,'y'],
        ['y',0, -x, 'y', 0,'y'],
        ['y',0, 0, 0, 0,'y'],
        ['y','y','y','y','y','y']]

def display(board):
    for i in range(1,5):
        print
        for j in range(1,5):
            print "",
            if type(board[i][j]) is float:
                print ("%.2f" %board[i][j]),
            else:
                print board[i][j],
        print
    print
for k in range(1,1000):
    temp = copy.deepcopy(array)
    flag = True
    for i in range(1,5):
        for j in range(1,5):
    #        print
            print "Cell:",i,j
    #        print
            if temp[i][j]==x or temp[i][j]==-x or temp[i][j]=='y':
                continue
            e = temp[i][j+1]
            w = temp[i][j-1]
            n = temp[i+1][j]
            s = temp[i-1][j]
            if temp[i][j+1]=='y':
                e = temp[i][j]
            if temp[i][j-1]=='y':
                w = temp[i][j]
            if temp[i+1][j]=='y':
                n = temp[i][j]
            if temp[i-1][j]=='y':
                s = temp[i][j]
            E = 0.8*e + 0.1*n + 0.1*s
            W = 0.8*w + 0.1*n + 0.1*s
            N = 0.8*n + 0.1*e + 0.1*w
            S = 0.8*s + 0.1*e + 0.1*w
            print "North->","0.8 *",n,"+","0.1*",e,"+","0.1*",w,"=",N
            print "South->","0.8 *",s,"+","0.1*",e,"+","0.1*",w,"=",S
            print "East->","0.8 *",e,"+","0.1*",n,"+","0.1*",s,"=",E
            print "West->","0.8 *",w,"+","0.1*",n,"+","0.1*",s,"=",W
            print
            array[i][j] = -0.05*x + max(E,W,N,S)
    #        print "Utility:",array[i][j]
    #        print "Difference:",abs(array[i][j]-temp[i][j])
    #        print
            if abs(array[i][j]-temp[i][j])>delta :
                flag = False
    print "Iteration:",k
    display(array)
    if flag:
        print "Number of Iterations:",k
        break
