import sys

sample_input = ['3',
                '2',
                'SE',
                '5',
                'EESSSESE',
                '6',
                'EESSEESSES']

def write_output(t, result):
    print ('Case #%s: %s' % (t, result))
    sys.stdout.flush()

def solve(N, P):
    #Recognise that the mirror image route to P will, by definition, not use any identical steps
    mList = ['E' if i == 'S' else 'S' for i in list(P)]
    return ''.join(mList)

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
            N = int(sample_input[int(2*t)-1])
            P = sample_input[int(2*t)]
        elif mode == 'prod':
            N = int(input())
            P = input()

        write_output(t, solve(N, P))

run('dev')