# All the Dynamic Programming problems here are examples of https://www.youtube.com/watch?v=oBt53YbR9Kk


def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


def gridTraveller(n, m, memo={}):
    key = str(n)+','+str(m)
    if key in memo:
        return memo[key]
    if (n == 1 and m == 1):
        return 1
    if (n == 0 or m == 0):
        return 0
    memo[key] = gridTraveller(n-1, m) + gridTraveller(n, m-1)
    return memo[key]


def canSum(targetSum: int, numbers: list, memo={}) -> bool:
    if (targetSum in memo):
        return memo[targetSum]
    if (targetSum == 0):
        return True
    if (targetSum < 0):
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers) == True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


def howSum(targetSum: int, numbers: list, memo={}) -> list:
    if (targetSum in memo):
        return memo[targetSum]
    if (targetSum == 0):
        return []
    if (targetSum < 0):
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if (remainderResult != None):
            # (*)Spread Operator in Python, the syntax translates to a list of elements of 'remainderResult' along with num
            memo[targetSum] = [*remainderResult, num]
            return memo[targetSum]

    memo[targetSum] = None
    return None


def canConstruct(target, wordBank, memo={}) -> bool:
    if (target in memo):
        return memo[target]
    if (target == ""):
        return True
    for word in wordBank:
        if (target.find(word) == 0):                            #Don't use target.index() because it throws an exception if the substring is not found
            suffix = target[len(word):]
            memo[suffix] = canConstruct(suffix, wordBank, memo)
            if memo[suffix] == True:
                return True
    return False
