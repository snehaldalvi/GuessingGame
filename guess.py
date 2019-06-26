#using Recursion
def fun():
	secret_num=15
	user_num=-1
	try_count=1
	while(secret_num!=user_num):
		print("%d try:"%try_count)
		user_num=int(input("enter a number:"))
		if(user_num<secret_num):
			print("smaller")
			fun()
		elif(user_num>secret_num):
			print("greater")
			fun()
		elif(user_num==secret_num):
			print("you guessed it right!")

		try_count=try_count+1
		print("you have attempted",try_count,"times")
fun()

#for word 
word="life"
predict=""
predict_count=0
predict_limit=4
out_of_limit=False
while((predict!=word)and not(out_of_limit)):
    if (predict_count<predict_limit):
        guess=input('Enter your predicted word:')
        predict=predict+1
    else:
        out_of_limit=True
if(out_of_limit):
    print("out of limit,you loose!!!")
print("You won !")

