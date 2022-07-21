import ast
import os
import datetime
import shutil
import random2
import random
import time
import urllib
import ipinfo
import requests
import speedtest
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
from datetime import datetime
from datetime import date

########################################################################################################################
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
time_now = (current_time)
today = date.today()
########################################################################################################################
rand_number = random.randint(1, 99999)
########################################################################################################################
main_path = 'D:/Program Files (x86)/Cryptical/log'
is_main_path = os.path.isdir(main_path)
if is_main_path == True:
    path = f'D:/Program Files (x86)/Cryptical/log/Log--{today}'
    isFile = os.path.isdir(path)
    if isFile == True:
        f = open(f'D:/Program Files (x86)/Cryptical/log/Log--{today}/Log--{time_now}--{rand_number}.txt', 'w+')
        f.write(f'{time_now}--Creating Log Folders...!\n')
        f.write(f'{time_now}--Success!!\n')
    else:
        os.mkdir(f'D:/Program Files (x86)/Cryptical/log/Log--{today}')
        f = open(f'log/Log--{today}/Log--{time_now}--{rand_number}.txt', 'w+')
        f.write(f'{time_now}--Creating Log Folders...!\n')
        f.write(f'{time_now}--Success!!\n')
else:
    os.mkdir('D:/Program Files (x86)/Cryptical')
    os.mkdir('D:/Program Files (x86)/Cryptical/log')
    os.mkdir(f'D:/Program Files (x86)/Cryptical/log/Log--{today}')
    f = open(f'D:/Program Files (x86)/Cryptical/log/Log--{today}/Log--{time_now}--{rand_number}.txt', 'w+')
    f.write(f'{time_now}--Creating Log Folders...!\n')
    f.write(f'{time_now}--Success!!\n')
########################################################################################################################
google_url = "https://google.com"
print("Connecting To The Server...\n")
f.write(f'{time_now}--Started!\n')
f.write(f'{time_now}--Connecting To The Server...\n')
try:
    response = requests.get(google_url)
    time.sleep(.4)
    print('Connected To The Server!\n')

except requests.exceptions.ConnectionError:
    nointernet = 1
    print("Couldn't Connect To The Server!\n")
    f.write(f"{time_now}--Couldn't Connect To The Server!\n")

try:
    import time

    f.write(f"{time_now}--Module Check PASS\n")
except ImportError:
    f.write(f"{time_now}--Time Module Not Found!\n")
    input(
        "Module time not installed, to install run 'pip install time' or \npress enter to install modules\n")
    if nointernet == 1:
        input('You need an internet connection to install\n')
        f.write(f"{time_now}--Couldn't Connect To The Internet!\n")
        exit()

    else:
        os.system('pip install time')
        f.write(f"{time_now}--Time Module installed succesfully\n")
try:
    import random2

    f.write(f"{time_now}--Module Check PASS\n")
except ImportError:
    f.write(f"{time_now}--random2 Module Not Found!\n")
    input(
        "Module random2 not installed, to install run 'pip install random2 or'\nPress enter to install modules\n")
    if nointernet == 1:
        input('You need an internet connection to install\n')
        f.write(f"{time_now}--Couldn't Connect To The Internet!\n")
        exit()

    else:
        os.system('pip install random2')
        f.write(f"{time_now}--Random2 Module Installed Successfully\n")

########################################################################################################################
account_create = 'no'
idk = "** Invalid Command **"

while True:
    login = input("\n\n~ Create an Account - 0\n~ Login - 1\n~ Exit - X\n : ")
    f.write(f"{time_now}--Login Menu Displayed!\n")
    if login.lower() == '0':
        create_username = input("\n\n\n~ Enter Your Username : ")
        f.write(f"{time_now}--Username - {create_username}\n")
        create_password = input("\n~ Enter Your Password : ")
        f.write(f"{time_now}--Password - {create_password}\n")
        ########################################################################################################################
        stored_username = create_username
        f.write(f"{time_now}--Username Stored Successfully!\n")
        stored_password = create_password
        f.write(f"{time_now}--Password Stored Successfully!\n")
        ########################################################################################################################
        account_create = 'yes'
        f.write(f"{time_now}--Account Created 'Changing account created to 'yes''\n")
        f.write(f"{time_now}--Updating the server!\n")
        f.write(f"{time_now}--Updated to the server successfully!\n")
    ########################################################################################################################
    elif login.lower() == '1':
        while True:
            if account_create == 'no':
                print("\n\n** Create an Account Before Login **\n\n")
                f.write(f"{time_now}--account create = 'no'\n")
                f.write(f"{time_now}--Account not found in the server!\n")
                f.write(f"{time_now}--Please Create an account before login!!\n")
                time.sleep(2.3)
                break
                f.write(f"{time_now}--Re logging!\n")

            else:
                login_username = input("\n\n~ Enter Your Username : ")
                f.write(f"{time_now}--Checking username!\n")
                f.write(f"{time_now}--Valid Username!\n")
                login_password = input("\n~ Enter Your Password : ")

                if login_password == stored_password:
                    f.write(f"{time_now}--Checking Password!\n")
                    f.write(f"{time_now}--Valid Password for the Username {stored_username}!\n")
                    f.write(f"{time_now}--Authentication to the server is success!\n")
                    while True:
                        print(f'\n\nWelcome {login_username}!\n')
                        f.write(f"{time_now}--Displaying Welcome Menu!\n")
                        menu = input(
                            '---Info---\n\n~ 1. Reset Password - 1\n~ 2. Change Username - 2\n~ 3. System Information - 3\n\n---Entertainment Zone---\n\n~ 4. Tic Tac Toe - 4\n~ 5. Rock Paper Scissors - 5\n~ 6. Calculator - 6\n~ 7. Speed Test - 7\n~ 8. Exit - x\n : ')
                        if menu.lower() == '1':
                            f.write(f"{time_now}--Password Reset Input Detected!\n")
                            print("\n** We Need To verify Before Changing Your Password **\n\n")
                            f.write(f"{time_now}--Verifying User\n")
                            while True:
                                num = random2.randint(0, 101)
                                print("Your Password Changing Code is ", num)
                                f.write(f"{time_now}--Password reset code is {num}\n")
                                verification = int(input("~ Enter Your Password Changing Code : "))

                                if verification == num:
                                    print("\n\nSuccessfully Verified !\n")
                                    f.write(f"{time_now}--Successfully Verified The user\n")
                                    time.sleep(1.5)
                                    new_password = input("~ Enter Your New Password :")
                                    stored_password = new_password
                                    f.write(f"{time_now}--New Password us {new_password}\n")
                                    print("Password Changing Successfully !")
                                    f.write(f"{time_now}--Uploading changes to the server!\n")
                                    print("Logging Out!...\n\n\n\n\n\n\n")
                                    f.write(f"{time_now}--Uploaded Successfully!!\n")
                                    f.write(f"{time_now}--Login Out!!!\n")
                                    break
                        ########################################################################################################################
                        elif menu.lower() == '2':
                            f.write(f"{time_now}--Username Change Input Detected!\n")
                            new_username = input('\n\n~ Enter Your New Username : ')
                            f.write(f"{time_now}--New Username is {new_username}\n")
                            print(f'\nYour New Username is {new_username}!')
                            stored_username = new_username
                            f.write(f"{time_now}--Uploading Changes TO the Server!\n")
                            f.write(f"{time_now}--Uploaded Successfully!!\n")
                        ########################################################################################################################
                        elif menu.lower() == '3':
                            f.write(f"{time_now}--System information Input Detected!\n")


                            def connect(host='http://google.com'):
                                f.write(f"{time_now}--Verifying Internet Connection!\n")
                                try:
                                    urllib.request.urlopen(host)  # Python 3.x
                                    return True
                                except:
                                    return False


                            if connect():
                                f.write(f"{time_now}--Connected to the server successfully\n")
                                r = requests.get('https://api64.ipify.org')
                                f.write(f"{time_now}--Requesting IP Info!\n")
                                ip = r.text

                                access_token = '70218b99c8ea9f'
                                f.write(f"{time_now}--Authenticating with the TOKEN\n")
                                handler = ipinfo.getHandler(access_token)
                                f.write(f"{time_now}--Access Denied!!!\n")
                                f.write(f"{time_now}--Retrying!\n")
                                f.write(f"{time_now}--Connected to the Server successfully!\n")
                                details = handler.getDetails(ip)
                                f.write(f"{time_now}--printing IP Info\n")

                                from datetime import datetime

                                now = datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                f.write(f"{time_now}--getting time\n")
                                time = (current_time)
                                f.write(f"{time_now}--Requesting from 'time.com' API\n")
                                f.write(f"{time_now}--Got Information Successfully\n")

                                ip_all = details.ip
                                country = details.country
                                postal = details.postal
                                region = details.region
                                org = details.org
                                city = details.city
                                timezone = details.timezone
                                cords = details.loc

                                all_details = f"IP - {ip_all}\nInternet Provider - {org}\nTime Zone - {timezone}\nCountry - {country}\nRegion - {region}\nCity - {city}\nPostal Code - {postal}\nCoordinates - {cords}\n\n\n"
                                print("--Network Info--")
                                f.write(f"{time_now}--Printing all IP Information!!")
                                print(all_details)
                            else:
                                print("\n---You Need An Internet Connection For Get The Internet Info!---\n")
                                f.write(f"{time_now}--No Internet connection\n")

                            print("--Local Info--\n")
                            print("Name - ", stored_username)
                            print("Password - ", stored_password)
                            os_type = os.name
                            cpu_count = os.cpu_count()
                            system_owner = os.getlogin()
                            print("--OS Info--\n")
                            print(f'OS Type - {os_type}')
                            f.write(f"{time_now}--OS Type - {os_type}\n")
                            print(f'CPU Count - {cpu_count}')
                            f.write(f"{time_now}--CPU Count - {cpu_count}\n")
                            print(f'System Username - {system_owner}')
                            f.write(f"{time_now}--\System Username - {system_owner}\n")
                            f.write(f"{time_now}--Printing local info\n")
                            print("\n---More Information Coming Soon.---\n\n")
                            f.write(f"{time_now}--More Information coming soon\n")

                        elif menu.lower() == '4':
                            f.write(f"{time_now}--Tic Tac Toe Input Detected!\n")
                            sign = 0
                            board = [[" " for x in range(3)] for y in range(3)]


                            def winner(b, l):
                                return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
                                        (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
                                        (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
                                        (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
                                        (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
                                        (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
                                        (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
                                        (b[0][2] == l and b[1][1] == l and b[2][0] == l))


                            def get_text(i, j, gb, l1, l2):
                                global sign
                                if board[i][j] == ' ':
                                    if sign % 2 == 0:
                                        l1.config(state=DISABLED)
                                        l2.config(state=ACTIVE)
                                        board[i][j] = "X"
                                    else:
                                        l2.config(state=DISABLED)
                                        l1.config(state=ACTIVE)
                                        board[i][j] = "O"
                                    sign += 1
                                    button[i][j].config(text=board[i][j])
                                if winner(board, "X"):
                                    gb.destroy()
                                    box = messagebox.showinfo("Winner", "Player 1 won the match")
                                    f.write(f"{time_now}--Player 1 WON The match\n")
                                elif winner(board, "O"):
                                    gb.destroy()
                                    box = messagebox.showinfo("Winner", "Player 2 won the match")
                                    f.write(f"{time_now}--Player 2 WON The match\n")
                                elif (isfull()):
                                    gb.destroy()
                                    box = messagebox.showinfo("Tie Game", "Tie Game")
                                    f.write(f"{time_now}--Tie game!\n")


                            def isfree(i, j):
                                return board[i][j] == " "


                            def isfull():
                                flag = True
                                for i in board:
                                    if (i.count(' ') > 0):
                                        flag = False
                                return flag


                            def gameboard_pl(game_board, l1, l2):
                                global button
                                button = []
                                for i in range(3):
                                    m = 3 + i
                                    button.append(i)
                                    button[i] = []
                                    for j in range(3):
                                        n = j
                                        button[i].append(j)
                                        get_t = partial(get_text, i, j, game_board, l1, l2)
                                        button[i][j] = Button(
                                            game_board, bd=5, command=get_t, height=4, width=8)
                                        button[i][j].grid(row=m, column=n)
                                game_board.mainloop()


                            def pc():
                                possiblemove = []
                                for i in range(len(board)):
                                    for j in range(len(board[i])):
                                        if board[i][j] == ' ':
                                            possiblemove.append([i, j])
                                move = []
                                if possiblemove == []:
                                    return
                                else:
                                    for let in ['O', 'X']:
                                        for i in possiblemove:
                                            boardcopy = deepcopy(board)
                                            boardcopy[i[0]][i[1]] = let
                                            if winner(boardcopy, let):
                                                return i
                                    corner = []
                                    for i in possiblemove:
                                        if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                                            corner.append(i)
                                    if len(corner) > 0:
                                        move = random.randint(0, len(corner) - 1)
                                        return corner[move]
                                    edge = []
                                    for i in possiblemove:
                                        if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                                            edge.append(i)
                                    if len(edge) > 0:
                                        move = random.randint(0, len(edge) - 1)
                                        return edge[move]


                            def get_text_pc(i, j, gb, l1, l2):
                                global sign
                                if board[i][j] == ' ':
                                    if sign % 2 == 0:
                                        l1.config(state=DISABLED)
                                        l2.config(state=ACTIVE)
                                        board[i][j] = "X"
                                    else:
                                        button[i][j].config(state=ACTIVE)
                                        l2.config(state=DISABLED)
                                        l1.config(state=ACTIVE)
                                        board[i][j] = "O"
                                    sign += 1
                                    button[i][j].config(text=board[i][j])
                                x = True
                                if winner(board, "X"):
                                    gb.destroy()
                                    x = False
                                    box = messagebox.showinfo("Winner", f"{stored_username} won the match")
                                    f.write(f"{time_now}--{stored_username} Won The Match\n")
                                elif winner(board, "O"):
                                    gb.destroy()
                                    x = False
                                    box = messagebox.showinfo("Winner", "Computer won the match")
                                    f.write(f"{time_now}--Computer WON the match\n")
                                elif (isfull()):
                                    gb.destroy()
                                    x = False
                                    box = messagebox.showinfo("Tie Game", "Tie Game")
                                    f.write(f"{time_now}--Tie game!\n")
                                if (x):
                                    if sign % 2 != 0:
                                        move = pc()
                                        button[move[0]][move[1]].config(state=DISABLED)
                                        get_text_pc(move[0], move[1], gb, l1, l2)


                            def gameboard_pc(game_board, l1, l2):
                                global button
                                button = []
                                for i in range(3):
                                    m = 3 + i
                                    button.append(i)
                                    button[i] = []
                                    for j in range(3):
                                        n = j
                                        button[i].append(j)
                                        get_t = partial(get_text_pc, i, j, game_board, l1, l2)
                                        button[i][j] = Button(
                                            game_board, bd=5, command=get_t, height=4, width=8)
                                        button[i][j].grid(row=m, column=n)
                                game_board.mainloop()


                            def withpc(game_board):
                                game_board.destroy()
                                game_board = Tk()
                                game_board.title("Tic Tac Toe")
                                l1 = Button(game_board, text="Player : X", width=10)
                                l1.grid(row=1, column=1)
                                l2 = Button(game_board, text="Computer : O",
                                            width=10, state=DISABLED)

                                l2.grid(row=2, column=1)
                                gameboard_pc(game_board, l1, l2)


                            def withplayer(game_board):
                                game_board.destroy()
                                game_board = Tk()
                                game_board.title("Tic Tac Toe")
                                l1 = Button(game_board, text="Player 1 : X", width=10)

                                l1.grid(row=1, column=1)
                                l2 = Button(game_board, text="Player 2 : O",
                                            width=10, state=DISABLED)

                                l2.grid(row=2, column=1)
                                gameboard_pl(game_board, l1, l2)


                            def play():
                                menu = Tk()
                                menu.geometry("250x250")
                                menu.title("Tic Tac Toe")
                                wpc = partial(withpc, menu)
                                wpl = partial(withplayer, menu)

                                head = Button(menu, text="---Welcome to tic-tac-toe---",
                                              activeforeground='red',
                                              activebackground="yellow", bg="red",
                                              fg="yellow", width=500, font='summer', bd=5)

                                B1 = Button(menu, text="Single Player", command=wpc,
                                            activeforeground='red',
                                            activebackground="yellow", bg="red",
                                            fg="yellow", width=500, font='summer', bd=5)

                                B2 = Button(menu, text="Multi Player", command=wpl, activeforeground='red',
                                            activebackground="yellow", bg="red", fg="yellow",
                                            width=500, font='summer', bd=5)

                                B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                                            activebackground="yellow", bg="red", fg="yellow",
                                            width=500, font='summer', bd=5)
                                head.pack(side='top')
                                B1.pack(side='top')
                                B2.pack(side='top')
                                B3.pack(side='top')
                                menu.mainloop()


                            if __name__ == '__main__':
                                play()
                        ########################################################################################################################
                        elif menu.lower() == '5':
                            f.write(f"{time_now}--Rock Paper Scissor Input Detected!\n")
                            import random
                            import tkinter as tk
                            from PIL import Image, ImageTk

                            window = tk.Tk()
                            window.geometry("300x500")
                            window.title("Rock Paper Scissor Matheesha ")

                            image = Image.open('files/rps.jpg')
                            f.write(f"{time_now}--Importing Images!\n")
                            image.thumbnail((300, 300), Image.ANTIALIAS)
                            photo = ImageTk.PhotoImage(image)
                            label_image = tk.Label(image=photo)
                            label_image.grid(column=15, row=0)
                            f.write(f"{time_now}--Game is Lock and Loaded\n")

                            USER_SCORE = 0
                            COMP_SCORE = 0
                            USER_CHOICE = ""
                            COMP_CHOICE = ""


                            def choice_to_number(choice):
                                rps = {'scissor': 0, 'paper': 1, 'rock': 2}
                                return rps[choice]


                            def number_to_choice(number):
                                rps = {0: 'scissor', 1: 'paper', 2: 'rock'}
                                return rps[number]


                            def random_computer_choice():
                                return random.choice(['scissor', 'paper', 'rock'])


                            def result(human_choice, comp_choice):
                                global USER_SCORE
                                global COMP_SCORE

                                user = choice_to_number(human_choice)
                                comp = choice_to_number(comp_choice)

                                if (user == comp):
                                    print("Tie")
                                    f.write(f"{time_now}--Tie!!\n")
                                elif ((user - comp) % 3 == 1):
                                    print("Sorry !! Computer win")
                                    f.write(f"{time_now}--Computer Won!!\n")
                                    USER_SCORE += 1
                                else:
                                    print("Congarts !! You win")
                                    f.write(f"{time_now}--{stored_username} Won!!\n")
                                    COMP_SCORE += 1

                                # Text
                                text_area = tk.Text(master=window, height=12, width=30)
                                text_area.grid(column=15, row=4)
                                answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c}  \n\n made by Matheesha Pathirana ".format(
                                    uc=USER_CHOICE, cc=COMP_CHOICE, u=USER_SCORE, c=COMP_SCORE,
                                    font=('arial', 24, 'bold'))
                                text_area.insert(tk.END, answer)


                            # Event Handling
                            def rock():
                                global USER_CHOICE
                                global COMP_CHOICE

                                USER_CHOICE = 'rock'
                                COMP_CHOICE = random_computer_choice()
                                result(USER_CHOICE, COMP_CHOICE)


                            def paper():
                                global USER_CHOICE
                                global COMP_CHOICE

                                USER_CHOICE = 'paper'
                                COMP_CHOICE = random_computer_choice()
                                result(USER_CHOICE, COMP_CHOICE)


                            def scissor():
                                global USER_CHOICE
                                global COMP_CHOICE

                                USER_CHOICE = 'scissor'
                                COMP_CHOICE = random_computer_choice()
                                result(USER_CHOICE, COMP_CHOICE)


                            # buttons
                            button1 = tk.Button(text="       Scissor         ", bg="red", command=scissor, height=1,
                                                width=8, font=('arial', 15, 'bold'))
                            button1.grid(column=15, row=1)
                            button2 = tk.Button(text="        Paper          ", bg="pink", command=paper, height=1,
                                                width=8,
                                                font=('arial', 15, 'bold'))
                            button2.grid(column=15, row=2)
                            button3 = tk.Button(text="         Rock          ", bg="yellow", command=rock, height=1,
                                                width=8, font=('arial', 15, 'bold'))
                            button3.grid(column=15, row=3)

                            window.mainloop()
                        ########################################################################################################################
                        elif menu.lower() == '6':
                            f.write(f"{time_now}--Calculator Input Detected!\n")
                            f.write(f"{time_now}--Loading Math Module and TK Module!\n")
                            f.write(f"{time_now}--Loaded Successfully!\n")
                            from tkinter import *

                            expression = ""


                            def press(num):
                                global expression
                                expression = expression + str(num)
                                equation.set(expression)


                            def equalpress():
                                try:
                                    global expression
                                    total = str(ast.literal_eval(expression))
                                    equation.set(total)
                                    expression = ""
                                except:
                                    equation.set(" error ")
                                    f.write(f"{time_now}--Error\n")
                                    expression = ""


                            def clear():
                                global expression
                                expression = ""
                                equation.set("")


                            if __name__ == "__main__":
                                gui = Tk()
                                gui.configure(background="light green")
                                gui.title("Calculator")
                                gui.geometry("270x150")
                                equation = StringVar()
                                expression_field = Entry(gui, textvariable=equation)
                                expression_field.grid(columnspan=4, ipadx=70)

                                button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                                                 command=lambda: press(1), height=1, width=7)
                                button1.grid(row=2, column=0)

                                button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                                                 command=lambda: press(2), height=1, width=7)
                                button2.grid(row=2, column=1)

                                button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                                                 command=lambda: press(3), height=1, width=7)
                                button3.grid(row=2, column=2)

                                button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                                                 command=lambda: press(4), height=1, width=7)
                                button4.grid(row=3, column=0)

                                button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                                                 command=lambda: press(5), height=1, width=7)
                                button5.grid(row=3, column=1)

                                button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                                                 command=lambda: press(6), height=1, width=7)
                                button6.grid(row=3, column=2)

                                button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                                                 command=lambda: press(7), height=1, width=7)
                                button7.grid(row=4, column=0)

                                button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                                                 command=lambda: press(8), height=1, width=7)
                                button8.grid(row=4, column=1)

                                button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                                                 command=lambda: press(9), height=1, width=7)
                                button9.grid(row=4, column=2)

                                button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                                                 command=lambda: press(0), height=1, width=7)
                                button0.grid(row=5, column=0)

                                plus = Button(gui, text=' + ', fg='black', bg='red',
                                              command=lambda: press("+"), height=1, width=7)
                                plus.grid(row=2, column=3)

                                minus = Button(gui, text=' - ', fg='black', bg='red',
                                               command=lambda: press("-"), height=1, width=7)
                                minus.grid(row=3, column=3)

                                multiply = Button(gui, text=' * ', fg='black', bg='red',
                                                  command=lambda: press("*"), height=1, width=7)
                                multiply.grid(row=4, column=3)

                                divide = Button(gui, text=' / ', fg='black', bg='red',
                                                command=lambda: press("/"), height=1, width=7)
                                divide.grid(row=5, column=3)

                                equal = Button(gui, text=' = ', fg='black', bg='red',
                                               command=equalpress, height=1, width=7)
                                equal.grid(row=5, column=2)

                                clear = Button(gui, text='Clear', fg='black', bg='red',
                                               command=clear, height=1, width=7)
                                clear.grid(row=5, column='1')

                                Decimal = Button(gui, text='.', fg='black', bg='red',
                                                 command=lambda: press('.'), height=1, width=7)
                                Decimal.grid(row=6, column=0)

                                gui.mainloop()
                        ########################################################################################################################
                        elif menu.lower() == '7':
                            print("Coming Soon...")
                        elif menu.lower() == 'x':
                            exit()
                        ########################################################################################################################
                        else:
                            print(idk)
                ########################################################################################################################
                else:
                    print(f"** Invalid Password for the Username '{login_username}'\n\n\n\n\n\n\n\n")
                    f.write(f"{time_now}--Invalid Password For the username {login_username}\n")


    ########################################################################################################################
    elif login.lower() == 'x':
        f.write(f"{time_now}--Exiting!!!  "
                "bye\n")
        exit()
    ########################################################################################################################
    else:
        print(f'\n\n{idk}\n\n')
        f.write(f"{time_now}--Invalid Command!\n")
