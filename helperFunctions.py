import sys

def IsApproximatelyEqual(x, y, epsilon = 1e-6):
    """Returns True if y is within relative or absolute 'epsilon' of x.

    By default, 'epsilon' is 1e-6.
    """
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return (-epsilon <= (x - y) / x <= epsilon or -epsilon <= (x - y) / y <= epsilon)

def encrypt(sourceText, dictionary):
    sourceList = list(sourceText)
    encryptDictionary = {value: key for key, value in dictionary.items()}
    primeList = [encryptDictionary[i] for i in sourceList]
    productList = []
    for i in range(len(primeList)-1):
        productList.append(int(primeList[i]*primeList[i+1]))
    return ' '.join([str(i) for i in productList])

cypher = encrypt('BABABACDEFGHIJKLMNOPQRSTUVWXYZ', {3: 'A', 5: 'B', 7: 'C', 11: 'D', 13: 'E', 17: 'F', 19: 'G', 23: 'H', 29: 'I', 31: 'J', 37: 'K', 41: 'L', 43: 'M', 47: 'N', 53: 'O', 59: 'P', 61: 'Q', 67: 'R', 71: 'S', 73: 'T', 79: 'U', 83: 'V', 89: 'W', 97: 'X', 101: 'Y', 103: 'Z'})
print (cypher)