n = int(input())

i = 0
ID_locations_db = dict()
while i < n:
    comp = input().split(":")
    ID = comp[0]
    location = comp[1][1:]
    ID_locations_db[ID] = location.split(", ")
    i += 1

keyID = input()
keyID_locations = ID_locations_db[keyID]
ID_location_db = ID_locations_db.pop(keyID)
matches = list()

for db_ID, db_locations in ID_locations_db.items():
    for each_location in db_locations:
        for key_location in keyID_locations:
            if key_location == each_location and db_ID not in matches:
                matches.append(db_ID)

if len(matches) == 0:
    print("Not Found")
else:
    print("\n".join(matches))