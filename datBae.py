import sys

def write_output(output):
    print (output)
    sys.stdout.flush()

def read_response():
    return input()

def first_bucket_size(N, B):
    #Calculate optimum first bucket size from choices. 16 guarantees completion within 5 steps.
    bSize = 2
    sizeList = [4,8,16]
    for size in sizeList:
        if size < N:
            if N / size > 2 and size > B:
                bSize = size
                break
            bSize = size
    return bSize

def build_spec(N, bSize, prevSpec):
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
    maxSize = max([i[0] for i in spec])
    if len(spec) == N and maxSize == 1:
        return 1
    else:
        return maxSize

def process(response, spec, prevSpec):
    resList = [int(i) for i in list(response)]

    #Split the response into buckets according to known response numbers from previous run
    #First run will have N-B values (1 segment)
    bucketList = []
    for parent in prevSpec:
        signals = parent[2]
        if signals == 0:
            bucket = []
        if len(resList) == signals:
            bucket = resList
            resList = []
        else:
            bucket = resList[:signals]
            resList = resList[signals:]
        bucketList.append(bucket)

    #Walk stepwise through buckets updating the spec with working machines if identified
    counter = 0
    for bucket in bucketList:
        counterStart = counter
        code = (1,0)
        if len(bucket) == 0:
            counter += 2 #Skip 2 new buckets.
        else:
            for value in bucket:
                if value == code[counter % 2]:
                    spec[counter][1] -= 1
                else:
                    counter += 1
                    spec[counter][1] -= 1
            if counter < counterStart + 2:
                counter = counterStart + 2

    #Append signals (working machines) to each spec
    for i in range(len(spec)):
        spec[i] = [spec[i][0], spec[i][1], spec[i][0]-spec[i][1]]
    
    return spec

def build_result(N, finalSpec):
    results = []
    for i in range(len(finalSpec)):
        if finalSpec[i][1] == 1:
            results.append(i)
    return ' '.join([str(i) for i in results])

def run():

    #We collect the first input line consisting of a single integer = T, the total number of test cases
    T = int(input()) 
     
    #We loop through each test case
    for t in range(1, T+1):

        N, B, F = [int(i) for i in list(input().split(' '))] #Retrieve test hyperparameters
        runSize = first_bucket_size(N, B)
        runPrevSpec = [[N, B, int(N-B)]]
        runResult = ''
        solved = False

        while not solved:
            
            runSpec = build_spec(N, runSize, runPrevSpec)
            runQuery = build_query(N, runSpec)

            print (runQuery)
            response = input()
            if int(response) == -1: #Exit the program if a failed.
                break

            runSpec = process(response, runSpec, runPrevSpec)
            runCheck = check_spec(N, runSpec)
            if runCheck == 1:
                runResult = build_result(N, runSpec)
                solved = True
            else:
                runSize = int(runCheck/2)
                runPrevSpec = runSpec

        if solved:
            write_output(runResult)
            success = int(input())
            if success == -1: #exit code if test failed
                break
        else:
            break #To extend the break from within the while

run()