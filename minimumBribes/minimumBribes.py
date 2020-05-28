


def minimumBribes(q):
    b = 0
    for p in range(0,len(q)):
        item = q[p]
        if item - p - 1 >= 3:
            print("Too chaotic")
            return
        if p > 0:

            for i in range(max(0,item -2),p):
                if q[i] > item:
                    b += 1
        
    print(b)
    
def main ():
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
main()