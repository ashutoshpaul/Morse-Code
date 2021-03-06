import os
import winsound , winspeech as utter
from colorama import Fore, Back, Style
from gtts import gTTS
import vlc
import time
import speech_recognition as sr

first_time = 1
sound_choice = 1
rerun=1
rc = ''
unit = 1  # Calculated time in seconds of the International Morse Code

def Headings(option_choosed):
    if option_choosed == 1:
        no1 = '. .. ... E N G L I G H   to   M O R S E ... .. .'
        print(Style.BRIGHT + Fore.MAGENTA + '\033[4m' + ' ' * 80 + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.MAGENTA + '\033[4m' , end ='')
        utter.stop_talking()
        utter.say('English to Morse')
        print('1) ' , end = '')
        print(no1.center(77 , ' '))
        print(Style.RESET_ALL , end = '')
        time.sleep(1.4)
        return
    elif option_choosed == 2:
        no2 = '. .. ... M O R S E   to   E N G L I S H ... .. .'
        print(Style.BRIGHT + Fore.MAGENTA + '\033[4m' + ' ' * 80 + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.MAGENTA + '\033[4m', end='')
        utter.stop_talking()
        utter.say('Morse to english')
        print('2) ', end='')
        print(no2.center(77 , ' '))
        print(Style.RESET_ALL, end='')
        time.sleep(1.4)
        return
    elif option_choosed == 4:
        no4 =   '. .. ... I N S T R U C T I O N S ... .. .'
        print(Style.BRIGHT + Fore.MAGENTA + '\033[4m' + ' ' * 80 + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.MAGENTA , end='')
        utter.stop_talking()
        utter.say('Instructions')
        print('\033[4m' + '4) ', end='')
        print(no4.center(77, ' '))
        print(Style.RESET_ALL, end='')
        time.sleep(1.4)
        return
    elif option_choosed == 5:
        no5 = '. .. ... EXIT ... .. .'
        print(Style.BRIGHT + Fore.RED + '\033[4m' + ' ' * 80 + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED, end='')
        print('\033[4m' + '5) ', end='')
        print(no5.center(77, ' '))
        print(Style.RESET_ALL, end='')


def setting_globals():
    global first_time
    first_time = 0
def set_sound_choice(choice_made):
    global sound_choice
    sound_choice = choice_made
def speech(letter):
    if letter==' ':
        letter='Space'
    else:
        letter=letter.upper()

    utter.say(letter)
    time.sleep(1.3)
def valid(where, inputx='XYZ'):
    if where == 'home':
        flag = True
        while flag == True:
            inputx = input()
            if inputx.isdigit():
                inputx = int(inputx)
                if 1 <= inputx <= 5:
                    flag = False
                    return (inputx)
                else:
                    print(Fore.RED + Style.BRIGHT + 'Enter 1, 2, 3, 4 or 5 :' + Style.RESET_ALL, end='')
                    winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
                    continue     #winsound.SND_ALIAS
            else:
                print(Fore.RED + Style.BRIGHT + 'Invalid Input, Enter again :' + Style.RESET_ALL, end='')
                winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
                continue

    elif where == 'instructions' or where == 'ask' or where == 'sound':
        flag = True
        while flag == True:
            inputx = input()
            if inputx.isdigit():
                inputx = int(inputx)
                if 1 <= inputx <= 2:
                    flag = False
                    return (inputx)
                else:
                    print(Fore.RED + Style.BRIGHT + 'Enter 1 or 2 :' + Style.RESET_ALL, end='')
                    winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
                    continue
            else:
                print(Fore.RED + Style.BRIGHT + 'Invalid Input, Enter again: ' + Style.RESET_ALL, end='')
                winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
                continue

    elif where == 'sound_type':
        flag = True
        while flag == True:
            inputx = input()
            if inputx.isdigit():
                inputx = int(inputx)
                if 1 <= inputx <= 3:
                    flag = False
                    return (inputx)
                else:
                    print(Fore.RED + Style.BRIGHT + 'Enter 1, 2 or 3:' + Style.RESET_ALL, end='')
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    continue
            else:
                print(Fore.RED + Style.BRIGHT + 'Invalid Input, Enter again:' + Style.RESET_ALL, end='')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                continue


    elif where == 'englishtomorse':
        pass
    elif where == 'morsetoenglish':
        pass
def instructions():
    #front = chr(1422) + '  '
    front = ''
    man = []
    man.append('\rFew')
    man.append('\rFew Instructions')
    man.append('\rFew Instructions to')
    man.append('\rFew Instructions to be')
    man.append('\rFew Instructions to be kept ')
    man.append('\rFew Instructions to be kept in ')
    man.append('\rFew Instructions to be kept in mind')
    man.append('\rFew Instructions to be kept in mind.')
    man.append('\rFew Instructions to be kept in mind..')
    man.append('\rFew Instructions to be kept in mind...')
    man.append('\rFew Instructions to be kept in mind...')
    man.append('\r')
    man.append('\r' + front + '1)  Leave')
    man.append('\r' + front + '1)  Leave \033[31m\033[1mONE\033[34m\033[1m')
    man.append('\r' + front + '1)  Leave \033[31m\033[1mONE SPACE\033[34m\033[1m')
    man.append('\r' + front + '1)  Leave \033[31m\033[1mONE SPACE\033[34m\033[1m between')
    man.append('\r' + front + '1)  Leave \033[31m\033[1mONE SPACE\033[34m\033[1m between \033[31m\033[1mTWO\033[34m\033[1m')
    man.append('\r' + front + '1)  Leave \033[31m\033[1mONE SPACE\033[34m\033[1m between \033[31m\033[1mTWO LETTERS\033[34m\033[1m.')
    man.append('\r' + front + '1)  Leave \033[31m\033[1mONE SPACE\033[34m\033[1m between \033[31m\033[1mTWO LETTERS\033[34m\033[1m..')
    man.append('\r' + front + '1)  Leave \033[31m\033[1mONE SPACE\033[34m\033[1m between \033[31m\033[1mTWO LETTERS\033[34m\033[1m...')
    man.append('\r' + front + '1)  Leave \033[31m\033[1mONE SPACE\033[34m\033[1m between \033[31m\033[1mTWO LETTERS\033[34m\033[1m...')
    man.append('\n')
    man.append('\r' + front + '')
    man.append('\r' + front + '')
    man.append('\r' + front + '2)  ')
    man.append('\r' + front + '2)  Leave')
    man.append('\r' + front + '2)  Leave \033[31m\033[1mTWO\033[34m\033[1m')
    man.append('\r' + front + '2)  Leave \033[31m\033[1mTWO SPACES\033[34m\033[1m')
    man.append('\r' + front + '2)  Leave \033[31m\033[1mTWO SPACES\033[34m\033[1m  between')
    man.append('\r' + front + '2)  Leave \033[31m\033[1mTWO SPACES\033[34m\033[1m  between \033[31m\033[1mTWO\033[34m\033[1m')
    man.append('\r' + front + '2)  Leave \033[31m\033[1mTWO SPACES\033[34m\033[1m  between \033[31m\033[1mTWO WORDS\033[34m\033[1m.')
    man.append('\r' + front + '2)  Leave \033[31m\033[1mTWO SPACES\033[34m\033[1m  between \033[31m\033[1mTWO WORDS\033[34m\033[1m..')
    man.append('\r' + front + '2)  Leave \033[31m\033[1mTWO SPACES\033[34m\033[1m  between \033[31m\033[1mTWO WORDS\033[34m\033[1m...')
    man.append('\r' + front + '2)  Leave \033[31m\033[1mTWO SPACES\033[34m\033[1m  between \033[31m\033[1mTWO WORDS\033[34m\033[1m...')
    man.append('\n')
    man.append('\rYou')
    man.append('\rYou are')
    man.append('\rYou are good')
    man.append('\rYou are good to')
    man.append('\rYou are good to go')
    man.append('\rYou are good to go ?')
    man.append('\rYou are good to go ?')
    man.append('\r')

    print(Fore.BLUE + Style.BRIGHT )
    #voice code goes down

    counter=1
    for hi in man:
        if counter==1:
            utter.say('Few Instructions to. be kept in mind...')
            #time.sleep(3)
        elif counter == 13:
            utter.say('Leave one. space between two letters...')
            #time.sleep(3)
        elif counter == 23:
            utter.say('And...')
            #time.sleep(3)
        elif counter == 26:
            utter.say('Leave two. spaces between two words...')
            #time.sleep(3)
        elif counter == 36:
            utter.say('You. are good to go...')
            #time.sleep(3)


        print(hi, end='')
        time.sleep(0.5)
        counter+=1
def menu():
    op0 = '\033[4m\033[1m'+Back.LIGHTYELLOW_EX+'TABLE OF CONTENTS'+Back.LIGHTYELLOW_EX
    op1 = '1. English -> Morse'
    op2 = '2. Morse -> English'
    op3 = '3. See Morse Code'
    op4 = '4. Instructions (for converting Morse to English)'
    op5 = '5. Exit'

    print(Back.LIGHTYELLOW_EX + '                                '+Back.LIGHTYELLOW_EX+'\033[4m\033[1mTABLE OF CONTENTS' +Back.LIGHTYELLOW_EX + '                               ' + '\033[0m')

    #print(Back.LIGHTYELLOW_EX + '\033[1m' + op0.ljust(70, ' ') + '\033[0m')
    print(Back.LIGHTYELLOW_EX + '\033[1m' + op1.ljust(80, ' ') + '\033[0m')
    print(Back.LIGHTYELLOW_EX + '\033[1m' + op2.ljust(80, ' ') + '\033[0m')
    print(Back.LIGHTYELLOW_EX + '\033[1m' + op3.ljust(80, ' ') + '\033[0m')
    print(Back.LIGHTYELLOW_EX + '\033[1m' + op4.ljust(80, ' ') + '\033[0m')
    print(Back.LIGHTYELLOW_EX + Fore.BLUE +'\033[1m' + op5.ljust(80, ' ') + '\033[0m')
    print(Style.RESET_ALL, end='')
    time.sleep(0.4)
    print(Fore.GREEN + Style.BRIGHT + '\rEnter your choice:' + Style.RESET_ALL, end='')
    utter.say('Enter your choice from above table of contents')
    time.sleep(3)
def home():
    CopyRight = chr(169)
    mcode = '-- --- .-. ... .    M O R S E   C O D E    -.-. --- -.. .'
    print(Back.RED + Fore.WHITE + '\033[1m' + '-' * 80 + '\033[0m')
    print(Back.CYAN + Fore.BLUE + Style.BRIGHT + mcode.center(80, ' ') + '\033[0m')
    print(Back.RED + Fore.WHITE+'\033[1m',end='')
    print('---------------------------------------' + CopyRight + 'All Rights Reserved By ' +Fore.LIGHTWHITE_EX + Back.RED +Style.BRIGHT + 'Ashutosh Paul' + Fore.WHITE + Style.BRIGHT + Back.RED + '----'+Style.RESET_ALL)
    print(Style.RESET_ALL + '\033[0m', end='')
def morsetoenglish():
    pass
def englishtomorse():
    pass
# See Morse
def see_Morse():
    utter.stop_talking()
    utter.say('International Morse Code')
    print(Style.BRIGHT + Fore.MAGENTA + '\033[4m' + ' ' * 80 + Style.RESET_ALL)
    imc = '. .. ... INTERNATIONAL MORSE CODE ... .. .'
    print(Style.BRIGHT + Fore.MAGENTA + '\033[4m' + '3)' , end = '')
    print(imc.center(78, ' ') + Style.RESET_ALL)
    A = '.-'
    B = '-...'
    C = '-.-.'
    D = '-..'
    E = '.'
    F = '..-.'
    G = '--.'
    H = '....'
    I = '..'
    J = '.---'
    K = '-.-'
    L = '.-..'
    M = '--'
    N = '-.'
    O = '---'
    P = '.--.'
    Q = '--.-'
    R = '.-.'
    S = '...'
    T = '-'
    U = '..-'
    V = '...-'
    W = '.--'
    X = '-..-'
    Y = '-.--'
    Z = '--..'
    d1 = '.----'
    d2 = '..---'
    d3 = '...--'
    d4 = '....-'
    d5 = '.....'
    d6 = '-....'
    d7 = '--...'
    d8 = '---..'
    d9 = '----.'
    d0 = '-----'
    bar = chr(166)
    tab1 = '\t\t  ' + bar + '\t     '
    tab2 = '\t  ' + bar + '      '
    flower = chr(1422)
    start = ' ' + flower + '   '
    six_spaces = '     '
    print()  # For a line space below the heading
    row_0 = start + 'A:\t' + A + tab1 + 'J:\t' + J + tab2 + 'S:\t' + S + tab1 + '1:\t' + d1 + six_spaces + flower
    row_1 = start + 'B:\t' + B + tab2 + 'K:\t' + K + tab1 + 'T:\t' + T + tab1 + '2:\t' + d2 + six_spaces + flower
    row_2 = start + 'C:\t' + C + tab2 + 'L:\t' + L + tab2 + 'U:\t' + U + tab1 + '3:\t' + d3 + six_spaces + flower
    row_3 = start + 'D:\t' + D + tab1 + 'M:\t' + M + tab1 + 'V:\t' + V + tab2 + '4:\t' + d4 + six_spaces + flower
    row_4 = start + 'E:\t' + E + tab1 + 'N:\t' + N + tab1 + 'W:\t' + W + tab1 + '5:\t' + d5 + six_spaces + flower
    row_5 = start + 'F:\t' + F + tab2 + 'O:\t' + O + tab1 + 'X:\t' + X + tab2 + '6:\t' + d6 + six_spaces + flower
    row_6 = start + 'G:\t' + G + tab1 + 'P:\t' + P + tab2 + 'Y:\t' + Y + tab2 + '7:\t' + d7 + six_spaces + flower
    row_7 = start + 'H:\t' + H + tab2 + 'Q:\t' + Q + tab2 + 'Z:\t' + Z + tab2 + '8:\t' + d8 + six_spaces + flower
    row_8 = start + 'I:\t' + I + tab1 + 'R:\t' + R + tab1 + '0:\t' + d0 + tab2 + '9:\t' + d9 + six_spaces + flower
    print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT, end='')
    print(row_0.ljust(70, ' ') + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + Back.BLUE + Style.BRIGHT, end='')
    print(row_1.ljust(69, ' ') + Style.RESET_ALL)
    print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT, end='')
    print(row_2.ljust(71, ' ') + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + Back.BLUE + Style.BRIGHT, end='')
    print(row_3.ljust(70, ' ') + Style.RESET_ALL)
    print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT, end='')
    print(row_4.ljust(68, ' ') + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + Back.BLUE + Style.BRIGHT, end='')
    print(row_5.ljust(71, ' ') + Style.RESET_ALL)
    print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT, end='')
    print(row_6.ljust(71, ' ') + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + Back.BLUE + Style.BRIGHT, end='')
    print(row_7.ljust(71, ' ') + Style.RESET_ALL)
    print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT, end='')
    print(row_8.ljust(71, ' ') + Style.RESET_ALL)

    print(Fore.MAGENTA + '\033[4m', end='')
    print(''.ljust(80, ' '), end='\n\n')

    time.sleep(3)

#Loading String
def Loading():
    print('\rLoading', end='')
    time.sleep(0.7)
    utter.say('Welcome to Morse Code Program')


    print('\rLoading.', end='')
    time.sleep(1)
    print('\rLoading..', end='')
    time.sleep(1)
    print('\rLoading...', end='')
    time.sleep(2)
    print('\r', end='')

def Exit():
    Headings(5)
    print(Fore.BLUE + Style.BRIGHT + '\n\n\nHave a nice day ?')
    print(Fore.BLUE + Style.BRIGHT + 'Happy Learning!\n\n\n\n\n\n\n\n')
    print(Fore.RED + '\033[4m' , end = '')
    print(''.ljust(80 , ' '))
    print(Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + 'Systems are terminating...' + Style.RESET_ALL)
    utter.stop_talking()
    utter.say('Have a nice Day, Happy Learning!')
    time.sleep(3.5)
    exit()

#From Here
Loading()
home()
menu()
def main():
    front = chr(187)
    rc=''
    flag, i = True, 1
    i = valid('home')
    utter.stop_talking()
    if i == 1:
        Headings(1)
        utter.stop_talking()
        utter.say('Enter in english.')
        print(Fore.BLUE + Style.BRIGHT + '\rEnter in English:' + Style.RESET_ALL)
        print(Fore.BLUE + front + Style.RESET_ALL , end=' ')

        #Voice Input is written below
        '''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say Somehting:')
            audio = r.listen(source)
    
        sp=r.recognize_google(audio)
        time.sleep(0.5)
        '''
        sp = input()
        sp = sp.strip()  # Remove first and last spaces if present
        sp = sp.lower()
        print(sp)
        sp = sp.replace('a', '.- ')  # str.replace(old,new)
        sp = sp.replace('b', '-... ')
        sp = sp.replace('c', '-.-. ')
        sp = sp.replace('d', '-.. ')
        sp = sp.replace('e', '. ')
        sp = sp.replace('f', '..-. ')
        sp = sp.replace('g', '--. ')
        sp = sp.replace('h', '.... ')
        sp = sp.replace('i', '.. ')
        sp = sp.replace('j', '.--- ')
        sp = sp.replace('k', '-.- ')
        sp = sp.replace('l', '.-.. ')
        sp = sp.replace('m', '-- ')
        sp = sp.replace('n', '-. ')
        sp = sp.replace('o', '--- ')
        sp = sp.replace('p', '.--. ')
        sp = sp.replace('q', '--.- ')
        sp = sp.replace('r', '.-. ')
        sp = sp.replace('s', '... ')
        sp = sp.replace('t', '- ')
        sp = sp.replace('u', '..- ')
        sp = sp.replace('v', '...- ')
        sp = sp.replace('w', '.-- ')
        sp = sp.replace('x', '-..- ')
        sp = sp.replace('y', '-.-- ')
        sp = sp.replace('z', '--.. ')
        sp = sp.replace('1', '.---- ')
        sp = sp.replace('2', '..--- ')
        sp = sp.replace('3', '...-- ')
        sp = sp.replace('4', '....- ')
        sp = sp.replace('5', '..... ')
        sp = sp.replace('6', '-.... ')
        sp = sp.replace('7', '--... ')
        sp = sp.replace('8', '---.. ')
        sp = sp.replace('9', '----. ')
        sp = sp.replace('0', '----- ')
        print('\033[1m' + sp + '\033[0m')
        sp = 'oo-' + sp[0:]

        print(Fore.GREEN + '\033[1m' + 'With Sound' + '\033[0m')

        a = 0

        # sp=sp.replace('  ','  ')    #For correcting run time errors

        #Trial Basis
        '''
        print('\r'+Fore.MAGENTA+'\033[3m'+'Trialling.'+'\033[0m'+Style.RESET_ALL,end='')
        winsound.Beep(1800, unit * 1000)
        print('\r' + Fore.MAGENTA + '\033[3m' + 'Trialling..' + '\033[0m' + Style.RESET_ALL, end='')
        winsound.Beep(1800, unit * 1000)
        print('\r' + Fore.MAGENTA + '\033[3m' + 'Trialling...' + '\033[0m' + Style.RESET_ALL, end='')
        winsound.Beep(1800, unit * 5000)
        '''
        #print('\r' + '\033[5m' + Fore.MAGENTA + '\033[5m'+'Trialling...\033[5m' + '\033[5m'  , end='')
        #winsound.Beep(1800, unit * 1000)
        #winsound.Beep(1800, unit * 1000)
        print(Fore.MAGENTA, end='')
        blink_time = 1
        dot = 1
        while blink_time <= 8:
            if blink_time == 8:
                print('\rDone' , end = '')
            else:
                if blink_time == 1:
                    winsound.Beep(1800, 130)
                if dot == 0:
                    print('\rTrialling', end='')
                    dot += 1
                elif dot == 1:
                    print('\rTrialling.', end='')
                    dot += 1
                elif dot == 2:
                    print('\rTrialling..', end='')
                    dot += 1
                elif dot == 3:
                    print('\rTrialling...', end='')
                    dot = 0
            time.sleep(0.31)
            blink_time += 1
        print('\r', end='')


        print('\033[0m' + Style.RESET_ALL,end='')

        while a < len(sp):

            if a >= 3:
                rc = rc[:len(rc)] + sp[a]
                b = a
                if b == len(sp) - 1:
                    break

                print('\r' + rc[:len(rc)] + '\b' + Back.LIGHTYELLOW_EX + '\033[1m' + sp[a] + '\033[0m' + Style.RESET_ALL + sp[
                                                                                                                         b + 1:],
                    end='')
                # pr=rc[:len(rc)] + '\b' + Back.LIGHTYELLOW_EX + '\033[1m' + sp[a] + '\033[0m' + Style.RESET_ALL

            if sp[a] == ' ':
                time.sleep(unit * 2)

            elif sp[a] == '.':
                winsound.Beep(1800, unit * 1000)
            elif sp[a] == '-':
                if a != 2:
                    winsound.Beep(1800, unit * 3 * 1000)  # 1 Dash=3 Dots||3 Units

            a += 1
        print('\r'+sp[3:])

        print(Fore.MAGENTA + '\033[4m', end='')
        print(''.ljust(80, ' '), end='\n\n')


    elif i == 2:  # Morse to English

        # .- ... .... ..- - --- ... ....  .--. .- ..- .-..
        Headings(2)
        flag = True
        pos = -1
        spx = ''
        while flag == True:
            utter.stop_talking()
            utter.say('Enter your Morse Code below')
            print(Fore.BLUE + Style.BRIGHT + '\rEnter your Morse Code:' + Style.RESET_ALL)
            print(Fore.BLUE + front + Style.RESET_ALL , end = ' ')
            #Above it
            #print(Fore.BLUE + Style.BRIGHT +'\rEnter your Morse:' + Style.RESET_ALL)

            spx = str(input())

            for check in spx:
                pos += 1
                if check == '.' or check == '-' or check == ' ':
                    if pos == len(spx) - 1:
                        flag = False
                else:
                    flag = True

        spx = spx.split(' ')
        eng = ''  # Variable to store english
        for px in spx:
            p = str(px)
            if p == '.-':
                eng = eng[:len(eng)] + 'a'
            elif p == '-...':
                eng = eng[:len(eng)] + 'b'
            elif p == '-.-.':
                eng = eng[:len(eng)] + 'c'
            elif p == '-..':
                eng = eng[:len(eng)] + 'd'
            elif p == '.':
                eng = eng[:len(eng)] + 'e'
            elif p == '..-.':
                eng = eng[:len(eng)] + 'f'
            elif p == '--.':
                eng = eng[:len(eng)] + 'g'
            elif p == '....':
                eng = eng[:len(eng)] + 'h'
            elif p == '..':
                eng = eng[:len(eng)] + 'i'
            elif p == '.---':
                eng = eng[:len(eng)] + 'j'
            elif p == '-.-':
                eng = eng[:len(eng)] + 'k'
            elif p == '.-..':
                eng = eng[:len(eng)] + 'l'
            elif p == '--':
                eng = eng[:len(eng)] + 'm'
            elif p == '-.':
                eng = eng[:len(eng)] + 'n'
            elif p == '---':
                eng = eng[:len(eng)] + 'o'
            elif p == '.--.':
                eng = eng[:len(eng)] + 'p'
            elif p == '--.-':
                eng = eng[:len(eng)] + 'q'
            elif p == '.-.':
                eng = eng[:len(eng)] + 'r'
            elif p == '...':
                eng = eng[:len(eng)] + 's'
            elif p == '-':
                eng = eng[:len(eng)] + 't'
            elif p == '..-':
                eng = eng[:len(eng)] + 'u'
            elif p == '...-':
                eng = eng[:len(eng)] + 'v'
            elif p == '.--':
                eng = eng[:len(eng)] + 'w'
            elif p == '-..-':
                eng = eng[:len(eng)] + 'x'
            elif p == '-.--':
                eng = eng[:len(eng)] + 'y'
            elif p == '--..':
                eng = eng[:len(eng)] + 'z'
            elif p == '.----':
                eng = eng[:len(eng)] + '1'
            elif p == '..---':
                eng = eng[:len(eng)] + '2'
            elif p == '...--':
                eng = eng[:len(eng)] + '3'
            elif p == '....-':
                eng = eng[:len(eng)] + '4'
            elif p == '.....':
                eng = eng[:len(eng)] + '5'
            elif p == '-....':
                eng = eng[:len(eng)] + '6'
            elif p == '--...':
                eng = eng[:len(eng)] + '7'
            elif p == '---..':
                eng = eng[:len(eng)] + '8'
            elif p == '----.':
                eng = eng[:len(eng)] + '9'
            elif p == '-----':
                eng = eng[:len(eng)] + '0'
            else:
                eng = eng[:len(eng)] + ' '

        if first_time == 1:
            print('\033[1m' + eng + '\033[0m')

        end = eng[:len(eng)] + ' '  # For printing logic

        while first_time == 1:
            utter.stop_talking()
            utter.say('Would you like to listen sound?')
            print(Style.BRIGHT+Fore.BLUE+'Would you like to listen sound?'+Style.RESET_ALL)
            time.sleep(2)
            utter.say('If yes then enter 1 or else enter 2')
            print(Fore.LIGHTBLUE_EX+'<Enter 1 for YES and 2 for NO>'+Style.RESET_ALL)
            print(Style.BRIGHT + Fore.BLUE + front + ' ' + Style.RESET_ALL, end = '')
            sound=valid('sound')
            if sound == 1:
                set_sound_choice(1)
            elif sound == 2:
                set_sound_choice(3)  #Sound is disabled
                setting_globals()

            setting_globals()

        if sound_choice == 1:
            utter.stop_talking()
            print(Style.BRIGHT + end + Style.RESET_ALL)
            print(Style.BRIGHT + Fore.GREEN + 'With Sound' + Style.RESET_ALL)
            w = 0
            while w < len(eng):
                # if w==len(eng)-1:
                # break
                print('\r' + eng[:w] + '\033[1m' + Back.LIGHTYELLOW_EX + eng[
                    w] + Style.RESET_ALL + '\033[0m' + eng[w + 1:], end='')
                try:
                    speech(eng[w])
                except:
                    print('Error Occured!')
                    exit()
                finally:
                    w += 1

            print('\r' + eng[:len(eng)])

        elif sound_choice == 2:
            eng_words = eng.split(' ')
            w = 0
            while w < len(eng_words):
                print('\r', end='')
                for done in eng_words[:w]:
                    print(done, end=' ')

                print(Style.BRIGHT + Back.LIGHTYELLOW_EX + eng_words[w] + Style.RESET_ALL, end=' ')

                for last_rem in eng_words[w + 1:]:
                    print(last_rem, end=' ')

                utter.say(eng_words[w])
                time.sleep(1.5)

                w += 1

            print('\r' + eng)

        print(Fore.MAGENTA + '\033[4m', end='')
        print(''.ljust(80, ' '), end='\n\n')


    elif i == 3:
        see_Morse()
    elif i == 4:
        Headings(4)
        instructions()
        print(Fore.MAGENTA + '\033[4m', end='')
        print(''.ljust(80, ' '), end='\n\n')

    elif i == 5:
        Exit()


if __name__=='__main__':
    main()
    rerun=1
    front = chr(187)
    while True:
        utter.stop_talking()
        utter.say('Do you wish to continue?')
        print(Style.RESET_ALL, end='')
        print(Style.BRIGHT + Fore.BLUE + 'Do you wish to continue?' + Style.RESET_ALL)
        time.sleep(2)
        utter.stop_talking()
        utter.say('Enter 1 for yes and 2 for shutting down the program.')
        print(Fore.LIGHTBLUE_EX + '<Enter 1 for yes and 2 for Shuting down the program>' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.BLUE + front + Style.RESET_ALL , end=' ')
        choice=valid('ask')
        if choice==1:
            utter.stop_talking()
            utter.say('Enter your choice from above table of contents')
            print(Fore.GREEN + Style.BRIGHT + '\rEnter your choice:' + Style.RESET_ALL, end='')
            main()
        else:   #i.e; Option 2
            Exit()


