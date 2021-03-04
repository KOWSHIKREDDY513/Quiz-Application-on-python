import Super_User
import json
import random
def Play():
		str=""
		ip = True
		while ip:
			print("Hi....Welocom!")
			print('\nFrom which Topic u want questions ? ')
			print('-----------------------------------------')
			print('1. G & K')
			print('2. Lists')
			print('3. Dictionaries')
			print('4. Tuples and Sets')
			choice = int(input('ENTER YOUR CHOICE: '))
			if choice == 1:
				str=r"C:\Users\KOWSHIK REDDY\Downloads\Python-_MCQ_Quiz-main\Python-_MCQ_Quiz-main\questions.json"
				ip=False
			elif choice == 2:
				str=r"C:\Users\KOWSHIK REDDY\Downloads\Python-_MCQ_Quiz-main\Python-_MCQ_Quiz-main\lists.json"
				ip=False
			elif choice == 3:
				str=r"C:\Users\KOWSHIK REDDY\Downloads\Python-_MCQ_Quiz-main\Python-_MCQ_Quiz-main\dictionaries.json"
				ip=False
			elif choice == 4:
				str=r"C:\Users\KOWSHIK REDDY\Downloads\Python-_MCQ_Quiz-main\Python-_MCQ_Quiz-main\tuples&sets.json"
				ip=False
			else:
				print('WRONG INPUT. ENTER THE CHOICE AGAIN')
				ip=True
		print("\n==========QUIZ START==========")
		score = 0
		with open(str, 'r+',encoding="utf8") as f:
			j = json.load(f)
			for i in range(10):
				no_of_questions = len(j)
				ch = random.randint(0, no_of_questions-1)
				print(f'\nQ{i+1} {j[ch]["question"]}\n')
				for option in j[ch]["options"]:
					print(option)
				answer = input("\nEnter your answer: ")
				if j[ch]["answer"][0] == answer[0].upper():
					print("\nYou are correct")
					score+=1
				else:
					print("\nYou are incorrect")
				del j[ch]
			print(f'\nFINAL SCORE: {score}')
			print("Your final score is {} out of 10. Your percentage is {}".format(score,(score/10)*100))
