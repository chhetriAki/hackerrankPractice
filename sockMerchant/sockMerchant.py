
def doWork(n, pairList):
    pairList.sort()
    print(pairList)
    pairCount = 0
    prevNum = False
    for i in range(0,n):
        if prevNum == False:
            prevNum = pairList[i]
        else:
            if(prevNum == pairList[i]):
                pairCount = pairCount + 1
                prevNum = False
            else:
                prevNum = pairList[i]
    print(pairCount)


def main ():
    print("Hello...LEt's Start")
    count = int(input("Enter array length: "))
    print("Enter elements (intger numbers) : ")
    pairList = []
    for i in range(0,count):
        item = int(input())
        pairList.append(item)
    doWork(count , pairList)

main()