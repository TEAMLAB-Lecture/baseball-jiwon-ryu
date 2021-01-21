# -*- coding: utf-8 -*-

import random


def get_random_number():
    return random.randrange(100, 1000)


def is_digit(user_input_number: str):
    if user_input_number.isdigit() == True:
        return True
    else:
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
    play = True
    print('Play Baseball')
    while play:
        
        user_input = 999
        random_number = str(get_not_duplicated_three_digit_number())
        print('Random Number is : ', random_number)
        
        strikes = 0
        while strikes != 3:
            user_input = input('Input guess number : ')
            while is_validated_number(user_input) == False:
                if user_input == '0':
                    play = False
                    break
                print('Wrong Input, Input again')
                user_input = input('Input guess number : ')
            if play == False:
                break
            strikes, balls = get_strikes_or_ball(user_input, random_number)
            print(f'Strikes : {strikes} , Balls : {balls}')
        if play == False:
            break
        response = input('You win, one more(Y/N)?')
        while True:
            if is_yes(response):
                break
            elif is_no(response):
                play = False
                break
            else:
                print('Wrong Input')
                response = input('You win, one more(Y/N)?')
                      
    print('Thank you for using the program')
    print('End of the Game')


    # 숫자 입력과 판단 반복 (strike 3 될때까지)
    # strike == 3 -> 진행 의사 묻기 -> 게임 재실행 or out


    

if __name__ == "__main__":
    main()
