import re
def isPangram(s):
    alphabetList = 'abcdefghijklmnopqrstuvwxyz'
    alphabetCount = 0
    if len(s) < 26:
        print('lenth is short')
        return False
    else:
        s = re.sub('[^a-zA-Z]','',s).lower()
        print(s)
        for i in range(len(alphabetList)):
            if alphabetList[i] in s:
                print(alphabetList[i])
                print("The string is pangram2")
                alphabetCount = alphabetCount + 1
                print(alphabetCount)
                if alphabetCount >= 26:
                    print("The string is pangram")
                    return True