import sys, string

sample_input = ['2',
                '103 31',
                '217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053',
                '10000 25',
                '3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543']

def write_output(t, result):
    print ('Case #%s: %s' % (t, result))
    sys.stdout.flush()

def prime_factors(M, N):
    i = 2
    while i <= N and i <= M**(1/2):
        if M % i == 0:
            return (i, int(M/i))
        if i > 2:
            i += 2
        else:
            i += 1
    return (0, M)

def solve(NL, P):
    N = int(NL.split(' ')[0])
    pList = [int(i) for i in P.split(' ')]
    rList = [[] for i in pList]

    #Get our first prime factors from the smallest product to minimise the effort
    a, b = prime_factors(min(pList), N)
    primes = [a, b]

    #Test remaining products with identified primes to find new primes until all alphabet found.
    #Whilst we doing it, might as well store the prime factors of each product in plaintext order.
    counter = 0
    while len(primes) < 26:
        a = primes[counter]
        for i in range(len(pList)):
            if rList[i] == [] and pList[i] % a == 0:
                b = int(pList[i] / a)
                rList[i] = [a, b]
                if not b in primes:
                    primes.append(b)
        counter += 1
    letters = list(string.ascii_uppercase)
    primes.sort()
    dictionary = dict(zip(primes, letters))

    #Convert prime factors list into list of primes in plaintext order
    messEnc = []
    if rList[0][0] in rList[1]: #special treatment for extracting the first prime
        messEnc.append(rList[0][1])
    else:
        messEnc.append(rList[0][0])

    for i in range(len(rList)): #extract remaining primes
        if rList[i][0] == messEnc[-1]:
            messEnc.append(rList[i][1])
        else:
            messEnc.append(rList[i][0])

    #Use the dictionary to translate the encrypted message
    message = ''
    for code in messEnc:
        message += dictionary[code]

    return message

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
            NL = sample_input[int(2*t)-1]
            P = sample_input[int(2*t)]
        elif mode == 'prod':
            NL = input()
            P = input()

        write_output(t, solve(NL, P))

run('dev')