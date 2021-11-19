############################################################################################################################################################################

import requests
import random

############################################################################################################################################################################

class bcolors:

    GREY = '\033[90m'
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

def clean_text(text: str) -> str:
    '''
    Clean up special characters in text
    '''
    text = text.replace('&amp;', '&')
    text = text.replace('nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')

    return text

def request_poem():
    '''
    Get a random poem and print it
    '''
    # Request random poems
    r = requests.get('https://www.poemist.com/api/v1/randompoems')
    assert r.status_code == 200, print('Oops, something went wrong, try again in a few seconds!')
    poems = r.json()

    for poem in poems:

        # Print poem in beautiful colors
        colors = [bcolors.LIGHT_RED, bcolors.LIGHT_GREEN, bcolors.LIGHT_YELLOW, bcolors.LIGHT_PURPLE, bcolors.LIGHT_PINK, bcolors.LIGHT_CYAN]
        random_color = random.choice(colors)

        print(f'\n{random_color}{bcolors.BOLD}{clean_text(poem["title"])}{bcolors.ENDC}\n')
        print(f'{random_color}{clean_text(poem["content"])}{bcolors.ENDC}')
        print('')
        print(f'\n{random_color}{bcolors.CURSIVE} - By {poem["poet"]["name"]}\n')
        print(f'{poem["poet"]["url"]}{bcolors.ENDC}\n')

        # Check to print more if available
        if poems.index(poem) != len(poems) - 1:
            response = input(f'{bcolors.GREY}How about another poem? (y/n): {bcolors.ENDC}')
            if response.lower() != 'y':
                break

############################################################################################################################################################################

if __name__ == '__main__':

    request_poem()

############################################################################################################################################################################