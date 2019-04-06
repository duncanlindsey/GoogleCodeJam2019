import sys, string

sample_input = ['4',
                '103 31',
                '217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053',
                '10000 25',
                '3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543',
                '103 29',
                '15 15 15 15 15 35 77 143 221 323 437 667 899 1147 1517 1763 2021 2491 3127 3599 4087 4757 5183 5767 6557 7387 8633 9797 10403',
                '103 29',
                '15 15 15 15 15 21 77 143 221 323 437 667 899 1147 1517 1763 2021 2491 3127 3599 4087 4757 5183 5767 6557 7387 8633 9797 10403']

def write_output(t, result):
    print ('Case #%s: %s' % (t, result))
    sys.stdout.flush()

def encrypt(sourceText, dictionary):
    sourceList = list(sourceText)
    encryptDictionary = {value: key for key, value in dictionary.items()}
    primeList = [encryptDictionary[i] for i in sourceList]
    productList = []
    for i in range(len(primeList)-1):
        productList.append(int(primeList[i]*primeList[i+1]))
    return ' '.join(productList)

def prime_factors(M, N):
    i = 2
    while i <= N and i <= M**(1/2): #No prime > N, and each product M must have at least 1 prime factor <= the sqrt(M)
        if M % i == 0:
            return i
        if i > 2:
            i += 2
        else:
            i += 1
    return 'Error - no prime factor found!'

def solve(NL, P):
    N = int(NL.split(' ')[0])
    pList = [int(i) for i in P.split(' ')]
    rList = [[] for i in pList]

    #Get our first prime factor from the smallest product to minimise the effort
    a = prime_factors(min(pList), N)
    primes = [a]

    #Test remaining products with identified primes to find new primes until all primes (alphabet) found.
    #Whilst we doing it, might as well store the prime factors of each product in plaintext order.
    counter = 0
    while len(primes) < 26:
        a = primes[counter]
        for i in range(len(pList)):
            if pList[i] % a == 0:
                b = int(pList[i] / a)
                rList[i] = [a, b]
                if not b in primes:
                    primes.append(b)
        counter += 1
    primes.sort()
    dictionary = dict(zip(primes, list(string.ascii_uppercase)))
    #print (dictionary)

    #Double check that rList has been completed
    for i in range(len(pList)):
        if rList[i] == []:
            #print ('Identified an incomplete element in rList')
            for prime in primes:
                if pList[i] % prime == 0:
                    rList[i] = [prime, int(pList[i] / prime)]
                    break

    #Prepare list of primes cyphertext
    messEnc = [0 for i in range(len(pList)+1)]

    #Find deterministic values first
    for i in range(len(pList)-1):
        firstP = rList[i][0] in rList[i+1]
        secondP = rList[i][1] in rList[i+1]
        if firstP and secondP: #not deterministic (can't determine the order of primes)
            pass
        else: #deterministic (the unique common prime must be positioned between the products)
            if firstP:
                messEnc[i+1] = rList[i][0]
            elif secondP:
                messEnc[i+1] = rList[i][1]
            
    #print ('Deterministic prime factors located. %s holes remaining' % messEnc.count(0))

    #Run through filling holes, using deterministically solved primes
    while min(messEnc) == 0: #whilst there are still unsolved primes
        for i in range(len(pList)):
            factors = rList[i]
            if messEnc[i] == 0 and messEnc[i+1] == 0: #can't solve this time, wait for 1 prime
                pass
            elif messEnc[i] == 0:
                factors.remove(messEnc[i+1])
                messEnc[i] = factors[0]
            elif messEnc[i+1] == 0:
                factors.remove(messEnc[i])
                messEnc[i+1] = factors[0]
        #print ('Passed through filling holes. %s holes remaining.' % messEnc.count(0))

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