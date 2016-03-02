import sys
print("\nPython Jeopardy\n\n")

clue = {"Super Man name" : "Clark Kent","Bruce Whayne":"Batman"}
#display categories
category = ["science","math","sports"]
points = ["10","20","30","40","50"]

first = ["a man who is super","a man who is a bat","a man made of iron","a wonderful woman"]
sec = ["superman","batman","ironman","wonder woman"]
third = ["a ","b ","c "]
fourth = ["1 ","2 ","3 "]

def disPoint(points):
	for i in range(0,3):
		print(points[i]+'\t'+points[i]+'\t'+points[i])	

def diScreen(first):
	for i in range(0,3):
		sys.stdout.write(first[i])
	sys.stdout.write("\n")

def disPick(pick, category):
	for x in range(0,3):
		if(pick == category[x]):
			print(category[x]+" found")
			return x


def catPoint(points):
	pickPoint = input("\nPoints to play for?")
	for i in range(0,3):
		if(pickPoint == points[i]):
			print(points[i]+" to play for")
			return i


#pick clues

#piCategory = input("Pick a cagegory")
def shoClue(gotoClue, first):
		gotoClue=int(gotoClue)
		print(gotoClue)
		print(first[gotoClue])
		ans=input("answer")
		if(ans == sec[gotoClue]):
			print("marvelous !")

#piPoints = input("Pick points")
#display clue
diScreen(category)
#diScreen(first)
disPoint(points)
pickCat = input("\n Choose a category\n")
disPick(pickCat, category)
gotoClue = catPoint(points)
shoClue(gotoClue,first)




print("you did it!! ")
'''
#answer with question format
#pick = input("points")

#compare answer with clue
#if()



#score
#print(state2[2])
'''

