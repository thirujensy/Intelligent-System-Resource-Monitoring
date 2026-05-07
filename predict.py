import random


def predict_status():
    return random.choice([
        'HEALTHY',
        'WARNING',
        'CRITICAL'
    ])
