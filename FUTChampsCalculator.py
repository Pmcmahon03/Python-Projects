futmatrix = []
rewards = [4, 12, 24, 36, 45, 51, 60, 67, 72, 76]
endscore = []

spts = int(input('Enter the number of points you have ?'))
gamesr = int(input('how many games do you have remaining ?'))

def genmatrix(gamesr,spts):
    [futmatrix.append([gamesr-i,i,0,0]) for i in range(gamesr+1)] # adds W L cols
    [scorecal(i, spts) for i in range(gamesr+1)] #

def scorecal(i, spts): # adds w*4 + l*1 col  
    futmatrix[i][2] = futmatrix[i][0]*4+futmatrix[i][1]*1
    futmatrix[i][3] = futmatrix[i][2] + spts

def champscal(gamesr,spts,rewards):
   
    genmatrix(gamesr,spts)
    [endscore.append(futmatrix[i][3]) for i in range(gamesr+1)]

    match = list(set(rewards) & set(endscore))

    if len(match) == 0:
        print(f'Your best score is {max(endscore)} your best reward is {max([i  for i in rewards if i < max(endscore)])}')
        #

    else:
        i = endscore.index(max(match))
        print(f'Your max score = {max(endscore)} and your max rewards = {max(match)} with {futmatrix[i][0]} wins and {futmatrix[i][1]} losses')

champscal(gamesr,spts,rewards)





    


#genscore(gamesr)
#fillscores(gamesr)

#print(targetlist)









    