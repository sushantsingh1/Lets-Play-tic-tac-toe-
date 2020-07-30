#!/usr/bin/env python
# coding: utf-8

# In[ ]:


board = {
    '11': ' ', '12': ' ', '13': ' ',
    '21': ' ', '22': ' ', '23': ' ',
    '31': ' ', '32': ' ', '33': ' '
}
player = 1
total_moves = 0
end_check = 0
def check():
    if board['11'] == 'X' and board['12'] == 'X' and board['13'] == 'X':
        print('player one won')
        return 1
    if board['21'] == 'X' and board['22'] == 'X' and board['23'] == 'X':
        print('player one won')
        return 1
    if board['31'] == 'X' and board['32'] == 'X' and board['33'] == 'X':
        print('player one won')
        return 1
    if board['11'] == 'X' and board['21'] == 'X' and board['31'] == 'X':
        print('player one won')
        return 1
    if board['12'] == 'X' and board['22'] == 'X' and board['32'] == 'X':
        print('player one won')
        return 1
    if board['13'] == 'X' and board['23'] == 'X' and board['33'] == 'X':
        print('player one won')
        return 1
    if board['11'] == 'x' and board['22'] == 'X' and board['33'] == 'X':
        print('player one won')
        return 1
    if board['11'] == '0' and board['12'] == '0' and board['13'] == '0':
        print('player two won')
        return 1
    if board['21'] == '0' and board['22'] == '0' and board['23'] == '0':
        print('player two won')
        return 1
    if board['31'] == '0' and board['32'] == '0' and board['33'] == '0':
        print('player two won')
        return 1
    if board['11'] == '0' and board['21'] == '0' and board['31'] == '0':
        print('player two won')
        return 1
    if board['12'] == '0' and board['22'] == '0' and board['32'] == '0':
        print('player two won')
        return 1
    if board['13'] == '0' and board['23'] == '0' and board['33'] == '0':
        print('player two won')
        return 1
    if board['11'] == '0' and board['22'] == '0' and board['33'] == '0':
        print('player two won')
        return 1
    return 0
print('11|12|13')
print('- +- +-')
print('21|22|23')
print('_ +_ +_')
print('31|32|33')
print("*********************************")
while True:
    print(board['11'] + '|' + board['12'] + '|' + board['13'])
    print('_+_+_')
    print(board['21'] + '|' + board['22'] + '|' + board['23'])
    print('_+_+_')
    print(board['31'] + '|' + board['32'] + '|' + board['33'])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:
        if player == 1:
            p1_input = input('player one')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                 board[p1_input.upper()] = 'X'
                 player = 2
                 break
            else:
                print('Invalid input')
        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                 board[p2_input.upper()] = '0'
                 player = 1
                 break
            else:
                print('Invalid input')
    total_moves += 1
    print('*************************')
    print()


# In[ ]:





# In[ ]:




