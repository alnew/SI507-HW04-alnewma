def user_input():
    m = input("What is your question")
    return m

magic_q = " "

while magic_q != "quit":
    magic_q = user_input()
    if magic_q[-1] == "?":
        print (“I’m sorry, I can only answer questions.”)
