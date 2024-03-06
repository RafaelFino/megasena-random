import random
import json

choices = []
stats = {}

for i in range(0, 60):
    choices.append(i+1)
    stats[i+1] = ''

#selection: numbers with more chances to be selected
selected = [3, 10, 21, 18, 3, 51, 42, 10, 20, 8, 12, 37, 42, 11, 22, 5, 16, 21, 18, 13, 10, 30, 3, 51, 3, 13, 26, 28, 36, 38, 41, 7, 12, 16, 25, 34, 42, 58, 5, 6, 19, 21, 33, 45, 57, 10, 15, 24, 9, 21, 55, 57, 11, 20, 28, 23, 46, 14, 59, 2, 4, 7, 12, 
31, 10 ]

#Remove duplicates numbers from selected
selected = list(dict.fromkeys(selected))
priority = 1

for p in range(0, priority):
    for i in range(0, len(selected)):
        num = selected[i]
        if num > 0 and num <= 60:
            choices.append(num)

#Games
games = [
 #   [10,1], [9, 2], [8,6], [7,10]
 [6, 20]
]

for size in games:    
    random.shuffle(choices)
    for n in range(0, size[1]):
        ret = {}
        while len(ret) < size[0]:
            pos = random.randint(0, len(choices)-1)
            item = choices[pos]
            stats[item] = stats[item] + '#'
     
            if item not in ret:
                ret[item] = 1
            else:
                ret[item] = ret[item] + 1            
        
        sorted = list(ret.keys())
        sorted.sort()
        print(("Jogo [%d] -> %s") % (len(sorted), sorted))

#print("Stats: %s" % json.dumps(stats, indent=2))  