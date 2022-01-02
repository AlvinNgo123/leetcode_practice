#Runtime: O(n) | Space: O(k)
#		 where n is the number of competitions and k is the number of teams	          
def tournament_champ(competitions, results):
    #Create a score dictionary to keep track of the team and their scores as we go through the competition
    #Iterate simultaneously through competitions and results at the same time.
        #Get the winning player and see if he already exists in the score dictionary
            #If yes, just add 3 to its current score in the dictionary
            #If no, make it a new entry in the dictionary with its score being 3
    #At the end, iterature through the score dictionary to find the team with highest score and return it as winner
    scoreDict = {}
    for i in range(len(competitions)):
        winningTeam = None
        if results[i] == 1:
            winningTeam = competitions[i][0]
        else:
            winningTeam = competitions[i][1]
        
        if winningTeam in scoreDict:
            scoreDict[winningTeam] += 3
        else:
            scoreDict[winningTeam] = 3
    
    finalWinner, highScore = None, None 
    for team, score in scoreDict.items():
        if finalWinner is None:
            finalWinner = team
            highScore = score
            continue
        
        if score > highScore:
            score = highScore
            finalWinner = team
    
    return finalWinner 

competition1 = [["Bulls", "Eagles"], ["Bulls", "Bears"], ["Bears", "Eagles"]]
score1 = [0, 0, 0]
print(tournament_champ(competition1, score1))
#Eagles

competition1 = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
score1 = [0, 1, 1]
print(tournament_champ(competition1, score1))
#Java

competition1 = [["Lakers", "Celtics"]]
score1 = [1]
print(tournament_champ(competition1, score1))
#Lakers