from slacker import Slacker
f = open('token', 'r')
token = f.read().replace('\n', '')
slack = Slacker(token)
print(token)
slack.chat.post_message('#joontarotbot_test', 'for test')