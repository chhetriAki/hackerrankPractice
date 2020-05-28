


def parliamentParties(votes):
    totalVotes = len(votes)
    voteDict = {}
    finalList = []

    for i in range(0,totalVotes):
        key = votes[i]
        if key in voteDict.keys():
            voteDict[str(key)]= voteDict[key] + 1
        else:
            voteDict[str(key)] = 1
    
    
    for key, item in voteDict.items():
        print(str(key) + " ---- " + str(item))
        percentVote = (item/totalVotes)*100
        if percentVote >= 5:
            finalList.append(key)
    finalList.sort()
    print(finalList)
    
def main ():
    votes_count = int(input().strip())

    votes = []

    for _ in range(votes_count):
        votes_item = input()
        votes.append(votes_item)

    result = parliamentParties(votes)

main()