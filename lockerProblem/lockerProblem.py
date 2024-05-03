lockers = []

def printList():
    for locker in range(1, 101):
        if lockers[locker] == 1:
            print("Locker " + str(locker) + ": " + str(lockers[locker]))

def swapLocker(locker):
    if lockers[locker] == 0:
        lockers[locker] = 1
    else:
        lockers[locker] = 0

# Only worried about indexes from 1 - 100
for elem in range(101):
    lockers.append(0)

for elem in range(101):
    lockers[elem] = 1

for elem in range(101):
    if elem % 2 == 0:
        lockers[elem] = 0

for student in range(3, 101):
    for elem in range(101):
        if elem % student == 0:
            swapLocker(elem)

printList()

# Print List

