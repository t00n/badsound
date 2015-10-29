from datetime import date
import json
from collections import defaultdict

def expected_score(A, B):
    return 1/(1 + 10**((B-A)/400))

def main(file, start_date, end_date):
    ratings = defaultdict(lambda: 1400)
    with open(file) as f:
        gayson = json.load(f)
    for data in gayson:
        if data['model'] == "badsound.vote":
            music1 = data['fields']['music1']
            music2 = data['fields']['music2']
            winner = data['fields']['winner']
            score1 = expected_score(ratings[music1], ratings[music2])
            score2 = expected_score(ratings[music2], ratings[music1])
            ratings[music1] += 32 * ((music1 == winner) - score1)
            ratings[music2] += 32 * ((music2 == winner) - score2)
    print(ratings)

if __name__ == '__main__':
    main("ranking.json", date(2015,10,28), date(2015,10,28))