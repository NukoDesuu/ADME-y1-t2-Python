n = int(input())

cmds = []

for i in range(n):
    cmds.append(input())

tn,qn,oi,tstn = 0,0,-1,0
tst,dt_list,qn_list,out_list = [],[],[],[]

for c in cmds:
    cmdl = c.split()
    out = 0

    cmd = cmdl[0]
    if len(cmdl) > 1:
        arg = int(cmdl[1])

    if cmd == "reset":
        tn = arg #current "ticket" nunber (what no. will NEW customer get)
        qn = arg #current "queue" (who is the NEXT queue)
    
    elif cmd == "new":
        tst.append(arg) #note down the time of ticket
        qn_list.append(tn) #add current no. on the list
        out = "ticket " + str(tn) #outputs obtained "ticket"
        tn += 1 #shift to next "ticket" number

    elif cmd == "next":
        out = "call " + str(qn) #call customer of the "current queue"
        oi += 1 #shifting of time stamp index
        qn += 1 #then, shift "current queue" to the next one

    elif cmd == "order":
        dt = arg - tst[oi] #find difference of time of the inputted value and latest called time (of order index)
        dt_list.append(dt) #add difference into the running list
        out = "qtime " + str(qn_list[oi]) + " " + str(dt) #outputs the waiting time of the mentioned queue
    
    elif cmd == "avg_qtime":
        csum = 0
        terms = 0
        for q in dt_list:
            csum += q
            terms += 1
        avgqt = csum / terms
        out = "avg_qtime " + str(avgqt)
    
    if out != 0:
        out_list.append(out)

for o in out_list:
    print(o)