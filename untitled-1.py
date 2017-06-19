import time
import random
import sys
Password= 'password'
while True:
    password= input('ENTER PASSWORD:')
    if password == Password:
        time.sleep(0.5)
        print('VERIFYING')
        for i in range(4):
            time.sleep(.3)
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(.8)
        print ('\nWELCOME BACK!')
        break
    print ('TRY AGAIN')
time.sleep(.6)
answer = input('\nDo you want to play a game? : ')
if answer == 'yes' or 'Yes' or 'Y' or 'y' or 'YES':
    print("Let's Start")
    print ('Please type Your name!: ')
    name = input()
    time.sleep(.6)
    print ('Hello ' +str( name))
    time.sleep(.7)   
max = 12
min = 1
x_count=0
y_count=0
def displayIntro():     
    x = random.randint(min,max)
    y = random.randint(min,max)   
    print('\n\n*****NEW ROUND*****')
    time.sleep(.5)
    print("\n\nThe computer's number is... "+str(y))
    time.sleep(1)
    input("\nPress 'Enter' to roll the die...")            
    time.sleep(1.2)
    print('\nYour number is... ' +str(x))    
    if (x > y):
        time.sleep(.5)
        print("\nYOUR NUMBER WAS HIGHER THAN THE COMPUTER'S! YOU WIN!")
        global x_count
        x_count = x_count + 1       
    if (x < y):
        time.sleep(1)
        print ("\nTHE COMPUTER'S NUMBER WAS HIGHER THAN YOURS! YOU LOSE!")
        global y_count
        y_count = y_count + 1   
    print('Your score is... ' +str(x_count))
    print('PC score is... '+str(y_count))
playagain = 'yes'
while playagain == 'yes': 
    displayIntro()
    playagain = input('\n\nDo you want to play again? (yes or no)')