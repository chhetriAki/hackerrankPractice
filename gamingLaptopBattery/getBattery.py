def getBattery(events):
    # Write your code here
    currentCharge = 50
    for i in range(0,len(events)):
        currentCharge = currentCharge + events[i]
        if currentCharge > 100:
            currentCharge = 100
    
    return currentCharge

if __name__ == '__main__':

    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    result = getBattery(events)
    print(result)