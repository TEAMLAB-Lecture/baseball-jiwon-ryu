import baseball_game as b

'''
a = '333'
print(b.is_validated_number(a))
print(b.is_digit(a))
print(b.is_between_100_and_999(a))
print(b.is_duplicated_number(a)) ##
'''
ans = ['no', 'NO', 'No', 'nO', 'n', 'N', 'n01']
for a in ans:
    print(b.is_no(a))
