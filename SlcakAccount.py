from slacker import Slacker

def SlackAccount():
    f = open('token', 'r')
    token = f.read().replace('\n', '')
    slack = Slacker(token)
    return slack