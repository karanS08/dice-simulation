import random
min = 1
max = 6
generated_num = random.randint(min, max)
print(generated_num)

while True:
    usr_input = str(input("Do you want to role the dice ?\n y for yes\n n for no \n "))



    if usr_input == 'y':

        print('\n \n \nthe number generated was : ', generated_num)
        print("\n \n \n")
        break
    else:
        break
