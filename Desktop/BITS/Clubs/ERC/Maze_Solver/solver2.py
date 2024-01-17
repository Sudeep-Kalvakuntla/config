import math

class node:
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.gval=0
        self.hval=0
        self.obs=False
        self.parent=0
        self.goal=False

nodes= [[node(i,j) for j in range(10)] for i in range(10)]
nodes[9][9].goal=True
open=[]
closed=[]
nodes[0][0].hval=127.27
solved=False
open.append(nodes[0][0])

def pickcurrent():
    c=math.inf
    for a in open:
        b=a.gval+a.hval
        if b<c:
            c=b
            w=a
    return w;

def findneighbours(h):
    x=h.row
    y=h.col
    nearby=[]
    if x!=0 and y!=0 and x!=9 and y!=9:
        nearby.append(nodes[y+1][x+1])
        nearby.append(nodes[y][x+1])
        nearby.append(nodes[y+1][x])
        nearby.append(nodes[y-1][x + 1])
        nearby.append(nodes[y + 1][x-1])
        nearby.append(nodes[y - 1][x -1])
        nearby.append(nodes[y][x - 1])
        nearby.append(nodes[y - 1][x])
    # little work left to check edge case will do later
    return nearby

def findgval(o,p):
    if o.row==p.row:
        j=p.gval+10
    elif o.col==p.col:
        j= p.gval + 10
    else:
        j=p.gval+14.14
    return j

def findhval(o):
    a=o.row
    b=o.col
    h=math.sqrt((9-a)*(9-a)+(9-b)(9-b))*10
    return h

while solved==False:
    current=pickcurrent()
    open.remove(current)
    closed.append(current)
    if current.goal==True:
        solved=True
        break
    neighbours=findneighbours(current)
    for d in neighbours:
        if d.obs==True or d in closed:
            continue
        if findgval(d,current)<d.gval or d not in open:
            d.gval=findgval(d,current)
            d.hval=findhval(d)
            d.parent=current
        if d not in open:
            open.append(d)

path=[nodes[9][9]]
k=False

while k== False:
    a=path.pop()
    b=a.parent
    path.append(a)
    path.append(b)
    if b==nodes[0][0]:
        k=True
