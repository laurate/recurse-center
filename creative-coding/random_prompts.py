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
    'very random',
    'in full bloom',
    'electricity',
]

concrete_prompts = [
    'animals',
    'the (flash)light at the end of the tunnel',
    'baggage',
    'fruit',
    'writing utensils',
    'telephone',
    'camera',
    'going to the movies',
    'roller coaster',
    'noise',
    'a warm summer night',
    'rainy day',
    'public transport',
    'pillars',
    'drinking tea',
    'my favorite programming language',
    'picture books',
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
    'lush green',
    'rainy day',
    'the (flash)light at the end of the tunnel',
    'electricity',
]

############################################################################################################################################################################

def get_new_prompts() -> None:

    # check if we used up all the prompts
    used_all_abstract = all(prompt in used_prompts for prompt in abstract_prompts)
    used_all_concrete = all(prompt in used_prompts for prompt in concrete_prompts)

    assert not (used_all_abstract or used_all_concrete), f'Prompts are all used up (abstract: {used_all_abstract} / concrete: {used_all_concrete}), maybe come up with some new ones?'

    # get new prompts
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