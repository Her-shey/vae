#mdir = './performance/perfcsv/'+each[:-9]+'xinst.csv'
mdir = './第一號鋼琴協奏曲.柴可夫斯基_xinst.csv'
#test = pm.PrettyMidi(mdir)
xscore = []
with open(mdir,'r') as f:
    templist = f.read().split('\n')
    templist.pop()
    for line in templist:
        xscore.append([float(i) for i in line.split(',')])

print(xscore[0:3])
#raise
'''
[[0,1.0000,1.45,66,80,2.214,tempo1,3.1223,tempo2,duration,timelenth],
[],
[]]
'''
frame = 0.25
t = 0
note_index = 0
c_ins = 0
FLAG = True
result = []
n = 0

while FLAG:
    if xscore[note_index][0] == -3:
        break
    if xscore[note_index][0] != c_ins:
        raise
    InerFLAG = True
    while InerFLAG:
        speed = None
        for j in range(len(xscore[-2])):
            if t<xscore[-2][j]:
                speed = xscore[-1][j-1]
                break
        if speed == None:
            speed = xscore[-1][-1]

        if t>=round(xscore[note_index][1],6) and t<=round(xscore[note_index][2],6):
            #print(xscore[note_index][1])
            

                
                
            result.append([c_ins,t,speed ,xscore[note_index][3],xscore[note_index][4],xscore[note_index][1],xscore[note_index][2]])
            note_index+=1

        elif t<round(xscore[note_index][1],6):
            result.append([c_ins,t,speed,0,0,0,0])
            
            InerFLAG = False
        else:
            note_index+=1
            result.append([c_ins,t,speed,0,0,0,0])
            InerFLAG = False
        n+=1
        if xscore[note_index][0] != c_ins:
            if xscore[note_index][0] == -3:
                FLAG = False
                InerFLAG = False
                break
            else:
                t = 0-frame
                c_ins+=1
                break
    t+=frame
import csv
with open(mdir[:-9]+'binst.csv','w',newline = '') as f:
    writer = csv.writer(f)
    for line in result:
        writer.writerow(line)
