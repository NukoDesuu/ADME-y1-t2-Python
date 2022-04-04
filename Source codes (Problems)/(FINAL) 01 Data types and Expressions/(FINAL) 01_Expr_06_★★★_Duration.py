#Inputting section...
h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())


#Processing section...
hts = 60*60
mts = 60

tot1 = (hts*h1) + (mts*m1) + s1
tot2 = (hts*h2) + (mts*m2) + s2
tdiff = tot2 - tot1

hdiff = tdiff // hts
mdiff = (tdiff % hts) // mts
sdiff = tdiff % mts 

#Preparing output contents...
hdur = (24 + hdiff) % 24
mdur = (60 + mdiff) % 60
sdur = (60 + sdiff) % 60

#Outputting section...
print(str(hdur) + ":" + str(mdur) + ":" + str(sdur))

