def minimumSwaps(arr):
    return arr
    
def main():
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)
