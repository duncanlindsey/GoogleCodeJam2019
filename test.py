import helperFunctions as hp

sample_input = ['5',
                '15342',
                '4',
                '12344',
                '444',
                '100104']

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

        N = int(sample_input[int(2*t)-1]) 
        V = [int(v) for v in sample_input[int(2*t)].split(' ')] 

        #N = int(input()) 
        #V = [int(v) for v in input().split(' ')] 

        write_output(t, solve(V))