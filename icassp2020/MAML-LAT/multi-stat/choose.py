#!/usr/bin/env python3  

settings=['multi3','multi6','other3']
langs = ['kurmanji','swahili','tamil','vietnamese']
langs_set = set(langs)

for setting in settings:
    for lang in langs:
        other_langs = langs_set - set([lang])
        leaderboard = dict()
        for other_lang in other_langs:
            with open(f'{setting}-{other_lang}','r') as fin:
                for line in fin.readlines():
                    step, cer = line.split(' ')
                    if step not in leaderboard:
                        leaderboard[step] = float(cer)
                    else:
                        leaderboard[step] += float(cer)
        for step in leaderboard:
            leaderboard[step] /= len(other_langs)

        print(f"{setting}-{lang}")
        print("Lowest CER: {}, step at {}".format(min(leaderboard.values()),min(leaderboard, key=leaderboard.get)))
        # print("Highest CER: {}, step at {}".format(max(leaderboard.values()),max(leaderboard, key=leaderboard.get)))
        # print(leaderboard)
            
                

