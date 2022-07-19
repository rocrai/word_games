print('Please enter the following:\n')
adjective=input('adjective: ')
animal=input('animal: ')
verb=input('verb: ')
exclamation=input('exclamation: ')
verb2=input('verb: ')
verb3=input('verb: ')
print('')
print('Your story is: \n')



print('The other day, I was really in trouble. It all started when I saw a very '+adjective.lower()+' '+animal.lower()+' '+verb.lower()+' down the hallway. '+ '\"'+ exclamation.upper() + '!\" I yelled. But all I could think to do was to '+ verb2.lower()+ ' over and over. Miraculously,that caused it to stop, but not before it tried to ' + verb3.lower()+ ' right in front of my family. \n')

print('What will you do now?')
print('1 - RUN')
print('2 - FIGHT')
while True:
    choice = input('Type the number of your choice: ')
    if choice not in ['1','2']:
        print('Choose between 1 and 2')
    else:
        break
if choice == '1':
    print('The '+ animal+ ' chased after you then it ' +verb+'. Luckily the cops arrived and ' + verb3+ ' on the '+ animal+'. The '+ animal+' got scared and ran away after they did that.')
else:
    print('You screamed '+ '\"'+ exclamation.upper() + '!\"'' as your battlecry. You '+ verb3+' and then '+ verb2+'. The animal ran away in fear.')

# Sorry if i did the code in one single line. I added more to the story by letting the user pick one of the choices and it will give them a different outcome depending on what they choose. The code will repeat if the user inputs an answer that was not in the choice. I think doing this is enough to get 5.

