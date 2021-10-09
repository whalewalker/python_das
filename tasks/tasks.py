def is_unique(data: str) -> bool:
    return len(set(list(data))) == len(data)


def is_permutation(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    count = 0
    for index in range(0, len(str1)):
        if str1[index] in str2:
            count += 1
    return count == len(str2)


def urlify(data: str) -> str:
    charArr = data.split(' ')
    url = ""
    for index in range(0, len(charArr)):
        url += charArr[index] + "%20"

    return url[0: len(url) - 3]


def permutationPalindrome(data: str) -> bool:
    charSet = set()
    string = data.replace(' ', '')
    for index in range(0, len(data)):
        if string[index] in charSet:
            charSet.remove(string[index])
        else:
            charSet.add(string[index])

    return len(charSet) <= 1


def oneAway(str1: str, str2: str) -> bool:
    if insert(str1, str2):
        return True
    elif replace(str1, str2):
        return True
    else:
        return False


def insert(str1: str, str2: str) -> bool:
    is_valid = False
    if len(str1) > len(str2) or len(str2) > len(str1):
        smallestStr = str2
        largestStr = str1

        if len(str1) < len(str2):
            smallestStr = str1

        if len(str2) > len(str1):
            largestStr = str2

        for index in range(0, len(largestStr)):
            if largestStr[index] not in smallestStr:
                is_valid = True

        return is_valid


def replace(str1: str, str2: str) -> bool:
    count = 0
    smallestStr = str2
    largestStr = str1

    if len(str1) < len(str2):
        smallestStr = str1

    if len(str2) > len(str1):
        largestStr = str2

    for index in range(0, len(largestStr)):
        if largestStr[index] not in smallestStr:
            count += 1

    return count == 1


def compression(data: str) -> str:
    compressedString = ""
    count = 1

    for index in range(1, len(data)):
        if data[index - 1] == data[index]:
            count += 1
        else:
            compressedString += data[index - 1] + str(count)
            count = 1

    compressedString += data[len(data) - 1] + str(count)
    return data if len(data) < len(compressedString) else compressedString
