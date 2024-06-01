from random import choice
from time import sleep
from os import system

l=[['_' for i in range(3)] for j in range(3)]
#box display
def box(pattern):
    for i in range(3):
        for j in range(3):
            print('|',end='')
            print(pattern[i][j],end='')
        print('|')
        
#for checking row
def check_row(pattern,sign):
   for i in pattern:
       s=set(i)
       if (len(s)==1) and list(s)[0]==sign:
           return True
       else:
           return False
           
#for checking col
def check_col(pattern,sign):
    s=set([pattern[0][0],pattern[1][0],pattern[2][0]])
    if (len(s)==1) and list(s)[0]==sign:
       return True
    else:
       return False
       
#check for draw
def check_draw(pattern):
    for row in pattern:
        if '_' in row:
            return False
    print("It's a Draw!!")
    return True

#for checking diagonals 
def check_diagonal(pattern,sign):
    s=set([pattern[0][0],pattern[1][1],pattern[2][2]])
    s1=set([pattern[0][2],pattern[1][1],pattern[2][0]])
    if ((len(s)==1) and (list(s)[0]==sign)) or ((len(s1)==1) and (list(s1)[0]==sign)) :
        return True
    else:
        return False
           
#game will check all conditions 
def game(row,col,sign,user1,user2):
        global l
        l[row][col]=sign
        if check_row(l,'X') or check_col(l,'X') or check_diagonal(l,'X'):
            print(f'{user1} Won!!')
            return True
        elif check_row(l,'O') or check_col(l,'O') or check_diagonal(l,'O'):
            print(f'{user2} Won!!')
            return True
        elif check_draw(l):
            return True
            
#main loop        
def main() :
    print(f'{"Tic Tac Toe":>30}')
    #ask for which type of game
    ask=input('1:Multiplayer\n2:With Computer\n: ').upper()
    sleep(1)
    system('clear')
    sleep(1)
    #Multiplayer
    if ask=='1':
        u1=input('Enter Player1 Name: ').capitalize()
        u2=input('Enter Player2 Name: ').capitalize()
        sleep(1)
        system('clear')
        sleep(1)
        while True:
            print(f'{"Tic Tac Toe":>30}')
            try:
                #user1
                box(l)
                p1rc=input(f'Enter {u1} RowxCol: ')
                r,c=int(p1rc.split('x')[0]),int(p1rc.split('x')[1])
                if l[r][c] != '_':
                    print("Already used..")
                    continue
                output=game(r,c,'X',u1,u2)
                sleep(0.5)
                system('clear')
                sleep(0.5)
                if output:
                    break
       
                #user2
                print(f'{"Tic Tac Toe":>30}')
                box(l)
                p2rc=input(f'Enter {u2} RowxCol: ')
                r1,c1=int(p2rc.split('x')[0]),int(p2rc.split('x')[1])
                if l[r1][c1] != '_':
                    print("Already used..")
                    continue                     
                output=game(r1,c1,'O',u1,u2)
                sleep(0.5)
                system('clear')
                sleep(0.5)
                
                if output:
                    break                    
            except IndexError :
                print('Invalid Index!!')
                sleep(1.5)
                system('clear')
            except ValueError:
                print('Invalid Input!!')
                sleep(1.5)
                system('clear')
                
    #user VS computer        
    elif ask=='2':
        u1=input('Enter Player Name: ')
        u2='Computer'
        while True:
            print(f'{"Tic Tac Toe":>30}')
            box(l)
            try:
                #user's move
                p1rc=input(f'Enter {u1} RowxCol: ')
                r,c=int(p1rc.split('x')[0]),int(p1rc.split('x')[1])
                p2rc=[[(i,j)for j in range(len(l[0]))] for i in range(len(l))]
                output=game(r,c,'X',u1,u2)                
                if output:
                    break
                #computer's move    
                empty_cells = [(i, j) for i in range(3) for j in range(3) if l[i][j] == '_']
                if not empty_cells:
                    break
                r1, c1 = choice(empty_cells)    
                output=game(r1,c1,'O',u1,u2)
                if output:
                    break
                sleep(0.5)
                system('clear')
                sleep(0.5)
            except IndexError :
                print('Invalid Index!')
                sleep(1.5)
                system('clear')
            except ValueError :
                print('Invalid Input')
                sleep(1.5)
                system('clear')
                
    #Invalid                       
    else:
        print('Invalid Input !!')
        
if __name__=='__main__':
    main()
    while True:
        ask=input('Wanna Play Again [y/n]: ').lower()
        try:
            if ask=='y':
                main()
            elif ask=='n':
                print('Okk!')
                break
            else:
                raise Exception()
        except Exception :
                print('Invalid Input !')
                
           