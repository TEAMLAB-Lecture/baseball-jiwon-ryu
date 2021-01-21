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
    for digit in user_input_number:
        if digit in random_number:
            if user_input_number.find(digit) == random_number.find(digit):
                result[0] += 1 # strikes
            else:
                result[1] += 1 # balls


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
    user_continue = True
    print("Play Baseball")
    while user_continue:                                                # 게임을 시작하거나 이어서 하는 조건
        user_input = 999

        random_number = str(get_not_duplicated_three_digit_number())    # 중복되지 않는 수를 가진 임의의 3자리수를 반환
        print("Random Number is : ", random_number)
    
        strike = None
        while strike != 3:                                              # 게임이 시작할때는 3 strikes가 아니므로 게임시작 / 3 strikes 나오면 게임종료
            user_input = input("Input guess number: ")
            if user_input == '0':                                       # 0을 입력하면 게임 종료
                print("Thank you for using this program")
                print("End of the Game")
                user_continue = False
                break
            if not is_validated_number(user_input):                     # wrong input 판단되면 다시 물어보는 로직
                print("Wrong Input, Input again")
                continue
            result = get_strikes_or_ball(user_input, random_number)     # 결과 로직
            strike, ball = result
            print(f"Strikes: {strike}, Balls: {ball}")                  # 결과 출력
        
        while strike == 3:                                              # 게임 종료 후 다시 진행하는지 묻는 loop / wrong input이면 다시 물어본다
            answer = input("You won the game ! One more? (Y/N)")
            if is_yes(answer):
                user_continue = True
                break
            elif is_no(answer):
                print("Thank you for using this program")
                print("End of the Game")
                user_continue = False
                break
            else:
                print("Wrong Input, Input again")                       # wrong input 이면 continue를 실행해서 while 첫줄로 돌아간다 
                continue
                      
    print('Thank you for using the program')
    print('End of the Game')


    # 숫자 입력과 판단 반복 (strike 3 될때까지)
    # strike == 3 -> 진행 의사 묻기 -> 게임 재실행 or out


    

if __name__ == "__main__":
    main()
