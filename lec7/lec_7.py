#-----------------------------------------#
# Lists
Ivys = ['yale', -1, 'princeton']


#--------------------------------------------#
# Dictionaries
### Mutable | heterogeneous | not ordered |  generalized indexing 
### < key, value >

def showDicts():
    #europian to french
    EtoF = {'one': 'un', 'soccer' : 'football', 'never':'jamais'}
    print(EtoF['soccer'])
    input()
    # print(EtoF[0])
    print(EtoF)
    input()
    # number to strings
    NtoS = {1:'one', 2:'two', 'one':1, 'two':2}
    print(NtoS)
    print(NtoS.keys())
    input()
    print(NtoS.keys)
    input()
    del NtoS['one']
    print(NtoS)
    input()



import math
#Get base
inputOK = False
while not inputOK:
    base = input('Enter base: ')
    # print('-----')
    # print(type(float(base)))
    # print('-----//')
    # print(type(1.0))
    # print('-----//---')
    if type(float(base)) == type(1.0): 
        # print('1-----')
        inputOK = True
        # print('2-----')
    else: 
        print('Error. Base must be floating point number.')
#Get Height 
inputOK = False
while not inputOK:
    height = input('Enter height: ')
    if type(float(height)) == type(1.0): 
        inputOK = True
    else: 
        print('Error. Height must be floating point number.')
hyp = math.sqrt(float(base)*float(base) + float(height)*float(height))
print( 'Base: '+str(base)+',height: '+str(height)+', hyp: '+str(hyp)) 
