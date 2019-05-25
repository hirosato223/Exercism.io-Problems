def latest(scores):
    return scores[len(scores)-1]

def personal_best(scores):
    best = 0
    for val in scores:
        if val > best:
            best = val
    return best

def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
