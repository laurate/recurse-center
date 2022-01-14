############################################################################################################################################################################

import random

############################################################################################################################################################################

abstract_prompts = [
    'lush green',
    'dreams',
    'the sound of silence',
    'from where I stand',
    'comedy',
    'country life',
    'city life',
    'sweet & sour',
    'travels to far-away places',
    'today I learned',
    'light and shadow',
    'puzzling',
    'tech support',
]

concrete_prompts = [
    'animals',
    'flashlight',
    'baggage',
    'fruit',
    'writing utensils',
    'telephone',
    'camera',
    'going to the movies',
    'roller coaster',
]

used_prompts = [
    'warmth',
    'winter wonderland',
    'poetry / literature',
    'transportation',
    'friends & family',
    'an abundance of grey',
    'nostalgia',
    'new beginnings',
    'sparkling',
    'today I learned',
    'tech support',
]

############################################################################################################################################################################

def get_new_prompts() -> None:

    new_abstract_prompt = False
    while new_abstract_prompt == False:
        abstract_prompt = random.choice(abstract_prompts)
        if abstract_prompt not in used_prompts:
            new_abstract_prompt = True

    new_concrete_prompt = False
    while new_concrete_prompt == False:
        concrete_prompt = random.choice(concrete_prompts)
        if concrete_prompt not in used_prompts:
            new_concrete_prompt = True

    print(f'''\nToday's Prompts:\n* {abstract_prompt}\n* {concrete_prompt}\nSee you again at [time]\n''')

############################################################################################################################################################################

if __name__ == '__main__':

    get_new_prompts()

############################################################################################################################################################################