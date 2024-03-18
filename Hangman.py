import random as r
import os
import time
#to check if word is guessed?
def if_word(word,g_letters):
	for i in word:
		if i not in g_letters:
			return False
	return True
#display word	
def check(word,g_letters):
	show=""
	for i in word:
		if i in g_letters:
			show+=i
		else:
			show+='-'
	return show
#ask if they want to play	
def ask():
	while True:
		time.sleep(4)
		os.system('cls')#cls-for pc clear-for phone
		ask=input("Wanna play again? [y/n]:").lower()
		os.system('cls')#cls-for pc clear-for phone
		if ask=='y':
			print('wait ok!!',end="\r")
			time.sleep(3)
			print("Loading your Game...",end="\r")
			time.sleep(4)		
			main()
		else:
			time.sleep(0.3)
			print('Ok No Problem Buddy')
			break
#for main work	
def main():
	l=["satan",'reddoor',"dark","valak",'asmodeus',"happy","bloomy","great"]
	word=r.choice(l)
	g_letters=''
	chances=len(word)+2
	for i in range(len(word)+2):
		print(f"word:{check(word,g_letters)}  Chances:{chances}\n")
		enter=input('Guess the letter:')
		if len(enter) != 1:	
			print("Enter only one letter")
			time.sleep(2)
			os.system('cls')#cls-for pc clear-for phone
		elif enter.isalpha()==False:
				print("Enter alphabets!\nYou are playing Hangman Buddy")
				time.sleep(2)
				os.system('cls')#cls-for pc clear-for phone
		else:
			chances-=1
			g_letters+=enter
		
		if if_word(word,g_letters):
			print('\nOh you Won!!\nYou are not dumb as i thought..huh!!\nWait for a min')
			break
	else:
		print(f'You ran out of chances!!You Lose\nWord was {word}\nWait for a min')

if __name__=="__main__":
	main()
	ask()
				
	
