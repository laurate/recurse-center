############################################################################################################################################################################

import requests
import random

############################################################################################################################################################################

class bcolors:

    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_PURPLE = '\033[94m'
    LIGHT_PINK = '\033[95m'
    LIGHT_CYAN = '\033[96m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CURSIVE = '\033[3m'
    ENDC = '\033[0m'

def request_poem():

    '''
    Get a random poem and print it
    '''
    # Request a random poem and take the first one
    r = requests.get('https://www.poemist.com/api/v1/randompoems')
    poem = r.json()[0]

    # Print poem in beautiful colors
    colors = [bcolors.LIGHT_RED, bcolors.LIGHT_GREEN, bcolors.LIGHT_YELLOW, bcolors.LIGHT_PURPLE, bcolors.LIGHT_PINK, bcolors.LIGHT_CYAN]
    random_color = random.choice(colors)

    print(f'\n{random_color}{bcolors.BOLD}{poem["title"]}{bcolors.ENDC}\n')
    print(f'{random_color}{poem["content"]}{bcolors.ENDC}')
    print('')
    print(f'\n{random_color}{bcolors.CURSIVE} - By {poem["poet"]["name"]}\n')
    print(f'{poem["poet"]["url"]}{bcolors.ENDC}\n')

############################################################################################################################################################################

if __name__ == '__main__':

    request_poem()

############################################################################################################################################################################