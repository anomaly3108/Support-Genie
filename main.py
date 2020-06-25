import json
import random
import functions
x=input('Enter issue: ') # enter issues details
y=input('Enter roles comma seperated: ').split(',')
issue={'issue':x,'role':y}
mode=int(input('select a mode:\n1. for all available.\n2. for least busy\n3. for random.'))-1 # select mode of selection
print(functions.selection(mode,issue)) # main function
