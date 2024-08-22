from sys import stdin

# Read the input using stdin
boxes = 1024
cartsize = 5
listboxes = []
totalcarts = 0;
boxes = int(boxes)
checkflag=False;
templist=[]

cartsize = int(cartsize)
# print('testing')
if (boxes % 2 == 0):
    dividedpaRT = boxes / 2;
    listboxes.append(dividedpaRT)
    listboxes.append(dividedpaRT)



else:
    dividedpaRT = (boxes - 1) / 2;
    listboxes.append(dividedpaRT)
    listboxes.append(dividedpaRT + 1)

for item in listboxes:
    templist.append(item)

listboxes=[]
def check():
    listboxes=[]
    for numb in templist:

        if numb <= cartsize:
            listboxes.append(numb)
            # print
        else:
            while numb >cartsize:

                if (numb % 2 == 0):
                    dividedpaRT = numb / 2;
                    listboxes.append(dividedpaRT)
                    listboxes.append(dividedpaRT)


                else:
                    dividedpaRT = (numb - 1) / 2;
                    listboxes.append(dividedpaRT)
                    listboxes.append(dividedpaRT+1)

                numb=numb/2
    pass


print templist
print listboxes
templist=[]
for item in listboxes:
    templist.append(item)

check()

print  templist
print len(listboxes)