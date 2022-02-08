targetlist=[]
rewards = [4, 12, 24, 36, 45, 51, 60, 67, 72, 76]
endscore = []

spts = int(input('Enter the number of points you have ?'))
gamesr = int(input('how many games do you have remaining ?'))

def genscore(gamesr,spts):
    [targetlist.append([gamesr-i,i,0,0]) for i in range(gamesr+1)]
    fillscores(gamesr, spts)

def fillscores(gamesr, spts):
    [scorecal(i, spts) for i in range(gamesr+1)]

def scorecal(i, spts):
    targetlist[i][2] = targetlist[i][0]*4+targetlist[i][1]*1
    targetlist[i][3] = targetlist[i][2] + spts

def champscal(gamesr,spts,rewards):


    genscore(gamesr,spts)
    [endscore.append(targetlist[i][3]) for i in range(gamesr+1)]

    match = list(set(rewards) & set(endscore))

    if len(match) == 0:
        print(f' You cannot reach target points')

    else:
        i = endscore.index(max(match))
        print(f'Max score posibble = {max(match)} with {targetlist[i][0]} wins and {targetlist[i][1]} losses')

champscal(gamesr,spts,rewards)





    


#genscore(gamesr)
#fillscores(gamesr)

#print(targetlist)









    