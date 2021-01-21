# -*- coding: utf-8 -*-

import random


def get_random_number():
    return random.randrange(100, 1000)


def is_digit(user_input_number: str):
    try:
        int(user_input_number)
        return True
    except ValueError:
        return False


def is_between_100_and_999(user_input_number: str):
    if int(user_input_number) >= 100 and int(user_input_number) < 1000:
        return True
    else:
        return False
        

def is_duplicated_number(three_digit: str):
    if len(list(set(list(three_digit)))) == len(list(three_digit)):
        return False
    else:
        return True


def is_validated_number(user_input_number: str):
    if is_digit(user_input_number) == True:
        if is_between_100_and_999(user_input_number) == True:
            if is_duplicated_number(user_input_number) == False:
                return True
    return False


def get_not_duplicated_three_digit_number():
    random_number_result = get_random_number()
    while is_duplicated_number(str(random_number_result)) == True:
        random_number_result = get_random_number()
    return random_number_result # int


def get_strikes_or_ball(user_input_number: str, random_number: str):
    result = [0, 0] # strikes, balls
    # for digit in user_input_number:
    #     if digit in random_number:
    #         if user_input_number.find(digit) == random_number.find(digit):
    #             result[0] += 1 # strikes
    #         else:
    #             result[1] += 1 # balls
    for i in range(len(user_input_number)):
        if user_input_number[i] == random_number[i]:
            result[0] += 1
        elif user_input_number[i] in random_number:
            result[1] += 1
    return result


def is_yes(one_more_input: str): # in으로 고쳐도 될듯
    if one_more_input.upper() == 'Y' or one_more_input.upper() == 'YES':
        return True
    else:
        return False


def is_no(one_more_input):
    if one_more_input.upper() == 'N' or one_more_input.upper() == 'NO':
        return True
    else:
        return False


def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    user_input = 999
    
    strikes = 0
    while strikes != 3:
        user_input = input('Input guess number : ')
        while is_validated_number(user_input) == False:
            if user_input == '0':
                print("Thank you for using this program")
                print("End of the Game")
                return
            print('Wrong Input, Input again')
            user_input = input('Input guess number : ')

        strikes, balls = get_strikes_or_ball(user_input, random_number)
        print(f'Strikes : {strikes} , Balls : {balls}')

    if strikes == 3:
        response = input('You win, one more(Y/N)?')
        while is_yes(response) == False and is_no(response) == False:
            print('Wrong Input')
            response = input('You win, one more(Y/N)?')

        if is_yes(response) == True:
            main()
        else:
            print("Thank you for using this program")
            print("End of the Game")
            return
    

if __name__ == "__main__":
    main()
