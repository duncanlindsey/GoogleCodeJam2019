import sys

sample_input = ['5',
                '15342',
                '4',
                '12344',
                '444',
                '100104']

def write_output(t, result):
    print ('Case #%s: %s' % (t, result))
    sys.stdout.flush()

def solve(N):
    aList = list(N)
    bList = ['0' for i in aList]
    for i in range(0, len(aList)):
        if aList[i] == '4':
            aList[i] = '3'
            bList[i] = '1'
    a = int(''.join(aList))
    b = int(''.join(bList))
    return ' '.join([str(a), str(b)])

def run(mode):

    #We collect the first input line consisting of a single integer = T, the total number of test cases
    if mode == 'dev':
        T = int(sample_input[0])
    elif mode == 'prod':
        T = int(input()) 
    else:
        return 'Error: incorrect mode'
     
    #We loop through each test case
    for t in range(1, T+1):
        
        if mode == 'dev':  
            N = sample_input[t]
        elif mode == 'prod':
            N = input()

        write_output(t, solve(N))

run('dev')