targetlist=[]

startingpoints = 10
gamesr = 6

def genscore(gamesr):
    [targetlist.append([gamesr-i,i,0,0]) for i in range(gamesr+1)]

def scorecal(i):
    targetlist[i][2] = targetlist[i][0]*4+targetlist[i][1]*1

def fillscores(gamesr):
    [scorecal(i) for i in range(gamesr+1)]

genscore(gamesr)
fillscores(gamesr)

print(targetlist)









    