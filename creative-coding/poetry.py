############################################################################################################################################################################

import requests

############################################################################################################################################################################

class bcolors:
    ROSE = '\033[95m'
    SOFT_BLUE = '\033[94m'
    LIGHT_BLUE = '\033[96m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_RED = '\033[91m'
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

    # Print poem beautifully
    print(f'\n{bcolors.BOLD}{poem["title"]}{bcolors.ENDC}\n')

    # TODO -> random pastel colors for poem
    print(poem['content'])

    print('')
    print(f'\n{bcolors.CURSIVE} - By {poem["poet"]["name"]}\n')
    print(f'{poem["poet"]["url"]}{bcolors.ENDC}\n')


############################################################################################################################################################################

if __name__ == '__main__':

    request_poem()

############################################################################################################################################################################