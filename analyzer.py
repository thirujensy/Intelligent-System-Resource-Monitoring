def analyze(metrics):
    score = 100

    if metrics['cpu'] > 80:
        score -= 20

    if metrics['memory'] > 80:
        score -= 20

    if score >= 80:
        return 'HEALTHY'

    elif score >= 50:
        return 'WARNING'

    else:
        return 'CRITICAL'
