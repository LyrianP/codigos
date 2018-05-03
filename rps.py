import random

def play():
    p_choice = input("Piedra, papel o tijeras?").capitalize()
    choices = {1 : 'Piedra', 2 : 'Papel', 3 : 'Tijeras'}
    cpu_choice = choices[random.randint(1,3)]
    if p_choice == cpu_choice:
        return print('Empate!')
    if compare(p_choice,cpu_choice):
        return print('Ganas!')
    else:
        return print('Pierdes!')

def compare(playerChoice,cpuChoice):
    results = {('Papel','Piedra') : True,
               ('Papel','Tijeras') : False,
               ('Piedra','Papel') : False,
               ('Piedra','Tijeras') : True,
               ('Tijeras','Papel') : True,
               ('Tijeras','Piedra') : False}
    return results[(playerChoice,cpuChoice)]

def game_start():
    play()

game_start()
