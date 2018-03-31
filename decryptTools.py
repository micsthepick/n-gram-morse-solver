import os

LANG = 'english_' # need _ at end.
NLIMIT = 5
ENDING = 'grams_score.txt'

FOLDER = '\\Scores\\' # need surrounding delimiters

DIR = os.path.dirname(os.path.abspath(__file__))

ngrams = []
for pf in ['mono', 'bi', 'tri', 'quad', 'quint'][:NLIMIT]:
    gfreq = {}
    with open(DIR + FOLDER + LANG + pf + ENDING, 'r') as f:
        lines = f.read().strip().split('\n')
        for line in lines:
            ngram, score = line.strip().split(' ')
            gfreq[ngram] = int(score)
        ngrams.append(gfreq)

def score(raw, n=None):
    string = ''.join(c for c in raw.upper() if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if n == None:
        n = max(2, min(5, len(string)))
    ngraphs = [string[i:i+n] for i in range(len(string) - n + 1)]
    return dscore(ngraphs, n)


def dscore(ngraphs, n):
    score = 0
    if not ngraphs:
        return 0
    counted = 0
    for ngraph in ngraphs:
        try:
            score += ngrams[n-1][ngraph]
            counted += 1
        except KeyError:
            pass
    if not counted:
        return 0
    score /= float(counted * 1000000)
    return score
