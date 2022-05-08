print("Lets play rock paper and scissor \n\nEnter your choice: ")
i='';
i=input('Press Y for playing the game else press N: ')

while i=='Y' or i=='y':
      a=input('Player 1 : ')
      b=input('\nPlayer 2 : ')
      a=a.lower();
      b=b.lower();
      if a==b:
         print('\nIts a tie')
      elif a=='scissor':
         if(b=='paper'):
            print('\nPlayer 1 is winner')
         else:
            print("\nPlayer 2 is winner")
      elif a=='paper':
         if b=='scissor':
           print("\nPlayer 2 is the winner")
         else:
          print("\nPlayer 1 is the winner")
      elif a=='rock':
         if b=='paper':
           print("\nPlayer 2 is the winner")
         else:
            print("\nPlayer 1 is the winner")
      i=input('\n\nPress Y for playing it again else press N: ')
