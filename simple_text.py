"""
Genetic algorithm for generating desired text using randomly generated strings of lowercase, uppercase and space character.
Program works by generating population of random words length of the text,
and then evolving best generations until finding desired text.
"""

import random

text = "Simple Text Algorithm"
population = 100
mutation = .01
current = []  # [(fitness, char array)]


def create_selection_pool():
    """
    Creates selection pool based on fitness of the elements
    """
    selection_pool = current[:]
    for i in current:
        for j in range(i[0]):
            selection_pool.append(i)
    return selection_pool


def select(selection_pool):
    """
    Selects two elements from selection pool
    :param selection_pool: Pool from which to select elements
    :return: Two selected elements
    """
    first = selection_pool[random.randint(0, len(selection_pool)-1)][1]
    second = selection_pool[random.randint(0, len(selection_pool)-1)][1]
    return first, second


def crossover(parent1, parent2):
    """
    Crosses elements of two parents
    :param parent1: First parent from which to take elements
    :param parent2: Second parent from which to take elements
    :return: Child of two parents
    """
    midpoint = int(len(text)/2)
    return parent1[:midpoint] + parent2[midpoint:]


def mutate(starting):
    """
    Mutates element from starting
    :param starting: Element on which to apply mutation
    :return: Mutated element
    """
    for i in range(len(starting)):
        if random.random() <= mutation:
            starting[i] = random_character()
    return starting


def evolve():
    """
    Evolves new generations from current one
    """
    global current
    new_population = []
    pool = create_selection_pool()

    for i in range(population):
        first, second = select(pool)
        result = crossover(first, second)
        result = mutate(result)
        new_population.append([fitness(result), result])

    current = new_population


def loop():
    """
    Loops until text is found
    :return: Nothing
    """
    global current
    count = 0
    while True:

        best = max(current)
        print('\r{:7d} : {} : {:3d}%'.format(count, ''.join(best[1]), best[0]), end='')
        if best[0] == 100:
            return
        evolve()
        count += 1


def random_character():
    """
    Creates random character (A-Z, a-z, 0-9 and space)
    :return: random character
    """
    sign = random.randint(61, 132)
    if sign == 61:
        sign = 32
    elif sign == 62:
        sign = 46
    elif sign > 122:
        sign -= 75
    return chr(sign)


def init():
    """
    Initializes starting population
    """
    global current
    current = []
    for i in range(population):
        unit = []
        for j in range(len(text)):
            unit.append(random_character())
        current.append((fitness(unit), unit))


def fitness(element):
    """
    Calculates fitness for each of the elements
    :param element: Element for which to calculate fitness
    :return:
    """
    counter = 0
    n = len(text)
    for i in range(n):
        if element[i] == text[i]:
            counter += 1
    return int(pow((counter/n), 2)*100)


if __name__ == '__main__':
    init()
    loop()
    print('\nFinished')
