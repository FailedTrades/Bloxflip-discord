import webbrowser
import os
import time
web = 'https://github.com/FailedTrades/Discord-APP'
while True:
    os.system('cls')
    print("It seems that you are having issues!\nWould u like to install the application? (.exe File)\n\nY/N\n\nThe app has all the requirements installed and wont have import issues.")
    yn = input("> ")
    if yn.lower() == 'y':
        webbrowser.open(web)
        exit()
    elif yn.lower() == 'n':
        exit()
    elif 'n' in yn.lower():
        os.system('cls')
        print('Did you mean "y"?')
        time.sleep(3)
    elif 'y' in yn.lower():
        os.system('cls')
        print('Did you mean "y"?')
        time.sleep(3)

    
