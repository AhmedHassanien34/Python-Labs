#Lab1
'''
s = "hello world hello hi there hi"
result = []
counts = []
words = s.split(" ")
for word in words:
    if word not in result:
        result.append(word)
        counts.append(1)
    else:
        word_index = result.index(word)
        counts[word_index] += 1

for i in range(len(result)):
    print(f"the word {result[i]} repeated {counts[i]}")
'''

#Another Answer
'''
s = "hello world hello hi there hi"
l_word = s.split(" ")
result = {}
for index in range (len(l_word)):
    word = l_word[index]
    if word not in result:
        result[word] = l_word.count(word)
print(result)
'''

#Another Answer
'''
s = "hello world hello hi there hi"
words = s.split(" ")
result = {}
for word in words:
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1
print(result)
'''

#Lab2
'''
Q.5 
implement grouped by owner code that 

*   accept a dictinary containg file owner name for each file name
*   create a dictionary of containing a list of file names for each owner name in any order

for example if you pass 
files = {
'Input.txt': 'Randy',
'Code.py': 'Stan',
'Output.txt': 'Randy'
} 

as input the output should be  {'Stan': ['Code.py'], 'Randy': ['Output.txt', 'Input.txt']} 
'''
'''
files = {'Input.txt': 'Randy','Code.py': 'Stan','Output.txt': 'Randy'} 
books = {}

for file in files:
    name = files[file]
    if name not in books:
        books[name] = [file]
    else:
        books[name].append(file)
print(books)
print(len(books["Randy"]))
'''

#Lab3
'''
def draw_tic_tac_toe_board(board):
    print("*"*13)
    for row in board:
        print(f"{row[0]} * {row[1]} * {row[2]} *")
    print("*"*13)

board = [
    ['_' , '_' , 'O'], 
    ['_' , 'X' , '_'], 
    ['_' , '_' , '_']
]
draw_tic_tac_toe_board(board)
row_pos = int(input("pls enter row pos:"))
col_pos = int(input("pls enter col pos:"))
select = input("select o/x")
board[row_pos][col_pos] = select.upper()
draw_tic_tac_toe_board(board)
'''

#Lab4
'''
def stock_price_summary(price_changes):
    gains = 0
    losses = 0
    for ele in price_changes:
        if ele < 0:
            losses += ele 
        elif ele > 0:
            gains += ele
    return gains ,losses


p = [0.01,0.03,-0.02,-0.14,0,0,0.10,-0.01]
x , y = stock_price_summary(p)
print(x,y)
'''

