def numCheck(key, num):
    if (num == key):
        return True
    else:
        return False
def main():
    correctNum = 6
    userNum = int(input("Enter the first number: "))
    numCheck(correctNum, userNum)
    correctNum2 = 1
    userNum = int(input("Enter the 2nd number: "))
    numCheck(correctNum2, userNum)
main()
#hopefully i can commit from vs studio