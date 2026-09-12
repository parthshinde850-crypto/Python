import random

def game():
    print("You are playing the game...")
    score = random.randint(1,62)
    #fetch the hiscore
    with open ("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore) #f.read() make string so we convert to int
        else:
            hiscore = 0

    print(f"Your score : {score}")
    if (score>hiscore):
        #write this hiscore to the file
        with open ("hiscore.txt" , "w") as f:
            f.write(str(score)) #write str to avoid error

    return score


game()