from random import randrange


def user_input():
    m = input("What is your question")
    return m

responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely","Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again","Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

rand_resp_ind = randrange(0,len(responses))
rand_resp = responses[rand_resp_ind]
magic_q = " "

while magic_q != "quit":
    magic_q = user_input()
    if magic_q[-1] == "?":
        print (“I’m sorry, I can only answer questions.”)
