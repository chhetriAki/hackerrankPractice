
def doWork(a,d):
    if d == len(a):
        return a
    else:
        arr1 = a[0:d]
        arr2= a[d:len(a)]
        return arr2 + arr1


def main ():
    print("Hello...LEt's Start")
    count = int(input("Enter array length: "))
    rotation = int(input("Enter number of rotation: "))
    print("Enter elements (intger numbers) : ")
    arr = []
    for i in range(0,count):
        item = int(input())
        arr.append(item)
    doWork(arr, rotation)

main()