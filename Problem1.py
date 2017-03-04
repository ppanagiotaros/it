userinput = int(raw_input("Pick a number, 1-1000, my guy:"))

from random import randrange

answer= randrange(1,1000)

while(userinput != answer):

	if(userinput > answer):
		print("whoa, whoa... too high, my guy. hey, i am a poet and i didn't even know it")
		userinput = int(raw_input("Better Choose another Number..."))

	if(userinput < answer):
		print("dont sell yourself short, my guy...")
		userinput = int(raw_input("Better Choose another Number..."))

	if (userinput == answer):
		print("you did it, my guy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		print(answer)

