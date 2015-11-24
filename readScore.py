# readScore.py
# This tests which scores from testscores.txt are correct and which are incorrect.
# Daniel McMurray
# Dr. Daniel Neumann
# CIS 125
# Collaborated with Evan Sauers and Jacob Wright


from BowlingGame import Game

# Read testscores file
testScores = open("testscores.txt")
scoreList = []

# Analyze the file
for line in testScores:
    #Strip the lines, and strip the numbers
    line = line.strip()
    scoresList = line.split(",")
    scoresList = [int(e) for e in scoresList]
    totalScore = scoresList.pop()
    
    g = Game()
    
    # Pins
    for pins in scoresList:
        g.roll(pins)
    score = g.score()
    
    # Print the scores
    print("Your score is {}, but the original score is {}." .format(score, totalScore))
    if score == totalScore:
        print("The score is correct.")
    else:
        print("The score is incorrect, the score should be ", score)
        
testScores.close()

