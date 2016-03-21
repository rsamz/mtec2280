import time, sys, os
x=0
cat1='sports'
level = '300'
clue ={'100':{'super name':"superman",'4-letter words':"burns with a flame",'sport':'jack johnson was first black champ'},
			'200':{'super name':"batman",'4-letter word':'term for a bunch of wolves or cards','sport':'tiger plays this at pebble beach'},
			'300':{'super name':"iron man",'4-letter word':'a place for the spine, or reverse side of a sign','sport':'pete rose should be in hall of fame'},
			'400':{'super name':"capt america",'4-letter word':'opposite hand of right','sport':'jordan sells shoes for to play this'}}

ans ={'100':{'super name':"clark kent",'4-letter words':'fire','sport':'boxing'},
			'200':{'super name':"bruce wayne",'4-letter word':'pack','sport':'golf'},
			'300':{'super name':"bruce banner",'4-letter word':'back','sport':'baseball'},
			'400':{'super name':"stave cross",'4-letter word':'left','sport':'basketball'}}			

score = {'100':{'super name':100,'4-letter word':100,'sport':100},
			'200':{'super name':200,'4-letter word':200,'sport':200},
			'300':{'super name':300,'4-letter word':300,'sport':300},
			'400':{'super name':400,'4-letter word':400,'sport':400}}			

myScore = 0
myPoint = 0
reps = 0
category = ["super name","4-letter word","sport"]
#def disPick(pick, category):#------pick=user input category is title name---------
while(reps < 3):
	print("\n//-------------------cagegories----------------")
#	x=0
#	while(x < 3):
#		sys.stdout.write(category[x]+"\t\t")
#		x+=1
#	print("\n\n//------------------------------------------")
	print(score['100'])
	print(score['200'])
	print(score['300'])
	cat1 = raw_input("pick a category?")
	level = raw_input("choose point amount?") 
	myPoint = 	score[level][cat1]
	while(myPoint == 0):
		print("//-----previously used, pick another ---------------")
		cat1 = raw_input("pick a category?")
		level = raw_input("choose point amount?") 
		myPoint = 	score[level][cat1]

	sys.stdout.write("\n")
	print('category = '+cat1 +'\t' +'points = ' + level)
	print('\nthe clue:   '+clue[level][cat1])
	storedAns = ans[level][cat1]
	time.sleep(3)
	myAns = raw_input("\n your answer:  ") 
	if(myAns == storedAns):
		print('\nwhat is,  '+storedAns)
		print("CORRECT !\n")
		myScore = myScore + myPoint
		score[level][cat1] = 0
		time.sleep(1)
	else:
		print('\nno the correct answer is '+storedAns)
		myScore -= myPoint
		score[level][cat1] = 0
	print('total points so far = ',myScore)
	reps += 1
	time.sleep(3)


#for row in clue:
#		print row
#print(showBoard[level])