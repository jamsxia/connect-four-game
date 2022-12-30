import tkinter
from tkinter import messagebox, simpledialog
state = dict()       # button->states('X','O'OR ' ')
button = dict()     # position to button
position = dict()  # buttons(widget)->positions
who = 'X'
n=0
m=0
def get_state(b):
    global state
    return state[b]

def set_state(b, letter):
    global state
    state[b] = letter
    b.config(text=letter)
    colors = {'X':'blue', 'O':'red', ' ':'black'}
    b.config(foreground=colors[letter])
    
def initialize():
    global button, state, who,m,n
    who = 'X'
    for i in range(m):
        for j in range(n):
            button[i,j] = tkinter.Button(height=1,width=3,
                                         font=("Helvetica", "24"))
            button[i,j].bind('<ButtonRelease-1>', click)
            button[i,j].grid(row=i, column=j)
            set_state(button[i,j],' ')
            position[button[i,j]]=(i,j);
    b = tkinter.Button(height=1,width=3,text='Reset',
                       command=reset)
    b.grid(sticky=tkinter.EW)
    
def reset():
    global button, who,m,n
    for i in range(m):
        for j in range(n):
            set_state(button[i,j], ' ')
    who = 'X'

def change_turn():
    global who
    if who == 'X':
        who = 'O'
    else:
        who = 'X'
        
def click(event):
    global button, who,position
    b = event.widget
    
    if get_state(b) == ' ':
        i=m-1
        j=position[b][1]
        while(get_state(button[i,j])!=' '):
            i-=1
        set_state(button[i,j], who)
        winner = check_win(i,j)
        if winner != None:
            messagebox.showinfo(winner + ' WINS!', winner + ' WINS!')
            reset()
        else:
            change_turn()

def s(i,j):  # Here just to make the next function a lot smaller
    global button
    return get_state(button[i,j])

def check_win(x,y):
    global m,n,button
    for j in range(n):
        if(j==0 or j==1 or j==2):
            continue
        else:
            if(get_state(button[x,j])==get_state(button[x,j-1])==get_state(button[x,j-2])==get_state(button[x,j-3]) and get_state(button[x,j])!=' 'and j-3<=y<=j):
                return get_state(button[x,j])
    #-------------------------------------horizontal
    for i in range(m):
        if(i==0 or i==1 or i==2):
            continue
        else:
            if(get_state(button[i,y])==get_state(button[i-1,y])==get_state(button[i-2,y])==get_state(button[i-3,y]) and get_state(button[i,y])!=' 'and i-3<=x<=i):
                return get_state(button[i,y])
    #-------------------------------------vertical
    cx=x-min(x,y)
    cy=y-min(x,y)
    while(cx<m-3 and cy<n-3):
        if(get_state(button[cx,cy])==get_state(button[cx+1,cy+1])==get_state(button[cx+2,cy+2])==get_state(button[cx+3,cy+3]) and get_state(button[cx,cy])!=' 'and cx<=x<=cx+3):
            return get_state(button[cx,cy])
        else:
            cx+=1
            cy+=1
    #--------------------------------------------northwest\
    cx=x+min(m-1-x,y)
    cy=y-min(m-1-x,y)
    while(cx>3 and cy<n-4):
        if(get_state(button[cx,cy])==get_state(button[cx-1,cy+1])==get_state(button[cx-2,cy+2])==get_state(button[cx-3,cy+3]) and get_state(button[cx,cy])!=' 'and cx-3<=x<=cx):
            return get_state(button[cx,cy])
        else:
            cx-=1
            cy+=1
    #--------------------------------------------southwest/
    winner="Nobody"
    for i in range (m):
        for j in range(n):
            if(get_state(button[i,j])==' '):
                winner=None
    return winner
    
                
        
        
    
if __name__ == '__main__': 
    root = tkinter.Tk()
    m = simpledialog.askinteger(title='Row?', prompt='r:', initialvalue=6)
    n = simpledialog.askinteger(title='Volume?', prompt='v:', initialvalue=7)
    print('Your size is %d*%d' % (m,n))
    root.title('Connect4')
    root.resizable(0,0)
    initialize()
    tkinter.mainloop()
