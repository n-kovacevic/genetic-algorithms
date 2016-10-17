"""
Genetic algorithm for generating desired using randomly generated strings of lowercase, uppercase and space character.
Program works by generating population of random words length of the text,
and then evolving best generations until finding desired text.
"""

import random

text = "Nikola"
population = 1000
mutation = 0.01
current = []  # [(fitness, char array)]


def main():
    """
    Main Function
    """
    init()
    calculate_fitness()
    loop()


def create_selection_pool():
    """
    Creates selection pool based on fitness of the elements
    """
    selection_pool = []
    for i in current:
        for j in range(i[0]):
            selection_pool.append(i[1])
    return selection_pool


def select(selection_pool):
    """
    Selects two elements from selection pool
    :param selection_pool: Pool from which to select elements
    :return: Two selected elements
    """
    first = selection_pool[random.randint(0, len(selection_pool)-1)]
    second = selection_pool[random.randint(0, len(selection_pool)-1)]
    return first, second


def crossover(parent1, parent2):
    """
    Crosses elements of two parents
    :param parent1: First parent from which to take elements
    :param parent2: Second parent from which to take elements
    :return: Child of two parents
    """
    midpoint = int(len(text)/2)
    child = parent1[:midpoint] + parent2[midpoint:]
    return child


def mutate(starting):
    """
    Mutates element from starting
    :param starting: Element on which to apply mutation
    :return: Mutated element
    """
    if random.random() <= mutation:
        char = random.randint(1, len(text)) - 1
        starting[char] = random_character()
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
        new_population.append([i, result])

    current = new_population


def loop():
    """
    Loops until text is found
    :return: Nothing
    """
    global current
    count = 0
    while True:
        print(str(count)+", ", end="")
        calculate_fitness()
        evolve()
        best = str().join(max(current)[1])
        print(best)
        if best == text:
            return
        count += 1


def random_character():
    """
    Creates random character (A-Z, a-z and space)
    :return: random character
    """
    sign = random.randint(1, 55)
    character = chr(32)
    if sign > 30:
        character = chr(random.randint(65, 90))
    elif sign > 5:
        character = chr(random.randint(97, 122))
    else:
        pass
    return character


def init():
    """
    Initializes starting population
    """
    global current
    for i in range(population):
        element = [i, []]
        for j in range(len(text)):
            element[1].append(random_character())
        current.append(element)


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
    return int((counter/n)*100)


def calculate_fitness():
    """
    Calculates fitness for each of the elements in current population
    """
    global current
    for i in range(population):
        current[i][0] = fitness(current[i][1])

main()
