import sys

def write_output(output):
    print (output)
    sys.stdout.flush()

def read_response():
    return input()

def first_bucket_size(N, B):
    #Calculate optimum first bucket size from choices. 16 guarantees completion within 5 steps.
    sizeList = [2,4,8,16]
    for size in sizeList:
        if B < size < N:
            bSize = size
    return bSize
    
def next_bucket_size(N, prevSpec): #RETIRE?
    #Set bucket size to half the previously used bucket size
    prevBSize = prevSpec[0][0]
    return int(prevBSize/2)

def bucket_spec(N, bSize):
    #Build the bucket spec for the next query. If there is a remainder, add an odd sized bucket on the end.
    spec = [[bSize, bSize] for i in range(int(N/bSize))]
    if N % bSize != 0:
        spec += [[N % bSize, N % bSize]]
    return spec

def build_query(N, spec):
    #Builds a series of 1s and 0s according to bucket spec
    query = ''
    code = ('1', '0')
    for i in range(len(spec)):
        for j in range(spec[i][0]):
            query += code[i % 2]
    return query

def check_spec(N, spec):
    bSize = spec[0][0]
    if len(spec) == N and bSize == 1:
        return True
    else:
        return bSize

def process(N, spec, prevSpec):
    #resList = list(response)
    #for i in range(len(bSizeList)):


    pass

def run(mode):

    #We collect the first input line consisting of a single integer = T, the total number of test cases
    T = int(input()) 
     
    #We loop through each test case
    for t in range(1, T+1):

        N, B, F = list(input()) #Retrieve test hyperparameters

        nodes = [i for i in range(N)]
        
        count = 1 #To check how many tests we have made
        solved = False

        #while count <= F:
            
            #results, query = solve(N, B, F, )
            #write_query(solve(N, B, F))

#run('dev')
