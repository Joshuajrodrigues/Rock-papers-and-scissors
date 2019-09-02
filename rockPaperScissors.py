#! /usr/bin/python3
import random

pscore=0
cscore=0
player='player'
while player!='e':
    
    player = input("'r'- Rock, 'p'- Paper and 's'-Scissor. Press e to Exit\n Input: ")

    computer =random.randint(0,2)
    if computer == 0:

        comp='r'
    
    elif computer == 1:

        comp='p'

    else:

        comp='s'

    if player != 'e':
        

        print(str(player) +' vs '+str(comp))

    if player == comp:
        print("DRAW!\nscore "+str(pscore)+'-'+str(cscore))

    elif player=='r' and comp =='p':
        print('Computer wins!')
        cscore =cscore+1
        print('Score:' +str(pscore)+'-'+str(cscore))
    elif player=='r' and comp =='s':
        print('Player wins!')
        pscore=pscore+1
        print('Score:' +str(pscore)+'-'+str(cscore))

    elif player=='p' and comp =='s':
        print('Computer wins!')
        cscore =cscore+1
        print('Score:' +str(pscore)+str(cscore))
    elif player=='s' and comp =='p':
        print('Player wins!')
        pscore=pscore+1
        print('Score:' +str(pscore)+'-'+str(cscore))

    elif player=='s' and comp =='r':
        print('Computer wins!')
        cscore =cscore+1
        print('Score:' +str(pscore)+'-'+str(cscore))
    elif player=='p' and comp =='r':
        print('Player wins!')
        pscore=pscore+1
        print('Score:' +str(pscore)+'-'+str(cscore))

    else:
        print('Exit')

