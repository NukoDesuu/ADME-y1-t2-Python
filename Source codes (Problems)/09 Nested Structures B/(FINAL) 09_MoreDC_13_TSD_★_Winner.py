n = int(input())

if n != 0:
    # arranges the victorious and defeated teams
    i = 0
    winners = set()
    losers = set()
    while i < n:
        teams = input().split()
        winners.add(teams[0])
        losers.add(teams[1])
        i += 1
    # gets whole sample and determine which teams have never lost
    all_teams = winners.union(losers)
    victorious = []
    for team in all_teams:
        if team not in losers:
            victorious.append(team)
    # outputs teams with no defeat, alphabetically
    print(sorted(victorious))
else:
    empty = []
    print(empty)