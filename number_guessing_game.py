import random

a = random.randint(1,99)
b = int(input('Guess a no. from 1 to 99'))
tries = 1

while tries <6:
    if a==b:
        print('Congrats, you chose the right number...!')
        break

    else:
        if a<b:
            print('The no. is greater than the actual no.')
            if tries!= 6:
                b = int(input('Guess a no. from 1 to 99'))
                tries+= 1
            else:
                tries+= 1

        else:
            print('The no. is less than the actual no.')
            if tries != 6:
                b = int(input('Guess a no. from 1 to 99'))
                tries += 1
            else:
                tries += 1


if tries==6:
    print("You are out of tries!", a, "is the no.")
else:
    print("The no. of tries were:", tries )