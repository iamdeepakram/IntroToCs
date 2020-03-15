#Bisection Methond

def squareRootBi(x, epsilon):
    """Assumes x >= 0 and epsilon > 0
    Returns y s.t. y*y is within epsilon 
    of x """

    assert x >= 0 , "x must be non negative , not " + str(x)
    assert epsilon >0, "epsilon must be positive not "+ str(epsilon)

    low = 0
    # high = x # this is bug 
    high = max(x, 1.0)  #this is the fix
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <=100:
        # print('low : ', low, 'high : ', high, 'guess : ', guess)
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print('Bi method Num iterations : ', ctr , 'Estimate : ', guess)
    return guess

# we use this different funtion because of
# Regression Testing : In this we avoid producing more bug by solving one bug in program 

def testBi():
    print('squareRoot(4, 0.0001))')
    squareRootBi(4, 0.0001)
    print('squareRoot(9, 0.0001))')
    squareRootBi(9, 0.0001)
    print('squareRoot(2, 0.0001))')
    squareRootBi(2, 0.0001)
    print('squareRoot(4, 0.0001))')
    squareRootBi(0.25, 0.0001)
    
##--------------------------------------------------##
#Newton Raphsom method 

def squareRootNR(x, epsilon):
    """Assumes x >=0 and epsilon > 0
    Returns y s.t. y*y is within epsilon of x"""
    assert x>=0, "x must be non -negative, not "+str(x)
    assert epsilon>0, "epsilon must be positive, not "+str(epsilon)
    x = float(x)
    guess = x/2.0
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        guess = guess - diff/(2.0 * guess)
        diff = guess**2 - x
        ctr +=1
    
    assert ctr <=100, 'Iteration count exceeded'
    print('NR method . Num. iterations: ', ctr, 'Estimate :',guess)
    return guess
##--------------------------------------------##
# Here we are comparing bi-section and newtown raphson methods
# to find the square root
def compareMethods():
    print('squareRoot(2, 0.01)')
    squareRootBi(2, 0.01)
    squareRootNR(2, 0.01)
    input()
    print('squareRoot(2, 0.0001)')
    squareRootBi(2, 0.0001)
    squareRootNR(2, 0.0001)
    input()
    print('squareRoot(2, 0.000001)')
    squareRootBi(2, 0.000001)
    squareRootNR(2, 0.000001)
    input()
    print('squareRoot(1234567890, 0.0001)')
    squareRootBi(1234567890, 0.0001)
    squareRootNR(1234567890, 0.0001)
    input()
    print('squareRoot(1234567890, 0.0000001)')
    squareRootBi(1234567890, 0.0000001)
    squareRootNR(1234567890, 0.0000001)
    input()


def showLists():

    Techs = ['MIT', 'Cal Tech']
    print(Techs)
    Ivys = ['Harvard', 'Yale', 'Brown']
    print(Ivys)
    Univs = []
    Univs.append(Techs)
    print(Univs)
    Univs.append(Ivys)
    input()
    print(Univs)
    input()
    for e in Univs:
        print(e)
        for c in e: print(c)
    input()
    Univs = Techs + Ivys
    print(Univs)
    input() 
    Ivys.remove('Harvard')
    print(Ivys)