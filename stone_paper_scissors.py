import random as r

#for converting 0 to Stone,1 to Paper 2 to Scissor 
def spsc(com):
	if com=="stone" :
		return 0
	elif com=="paper":
		return 1
	else:
		return 2		
		
#for Check
def check(co,use):
	comp=spsc(co)
	user=spsc(use)
	
	if comp==user:
		return "It's a Draw!!"
	elif (comp==2 and user==0) or (comp==0 and user==1) or (comp==1 and user==2):
		return " You Won!! "
	else:
		return " Oh! You Lose!! "


print("""	       Letss Goo!!
	    Choose your move 
	Stone or Paper or Scissor
		""")
for i in range(3):
	computer=r.choice(["stone","paper","scissor"])
	
	user=input("Enter Your Move :")
	
	if user not in ["stone","paper","scissor"]:
		raise TypeError("\nchoose from this'stone','paper','scissor'to play dumb!! ")
		
	print(f"Computer's Move:{computer}\nYour Move:{user}\n")
	print(f"Result: {check(computer,user)}\n")
	if check(computer,user)==" You Won!! ":
		break
	
print("		Game Over")