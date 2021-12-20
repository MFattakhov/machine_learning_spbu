import random
import math
from datetime import datetime
import matplotlib.pyplot as plt

def generate_nodes(size):
    return [(random.uniform(0, size), random.uniform(0, size)) for i in range(size)]

def mutate(path):
    i = random.randrange(len(path))
    j = random.randrange(len(path))
    if i > j:
        i, j = j, i
    new_path = path[:i] + path[i:j][::-1] + path[j:]
    return new_path

def run_annealing(initial_path, trials, initial_temp, cooling_rate):
    history = [distance(initial_path)]
    path = initial_path[:]
    temperature = initial_temp
    for trial in range(trials):
        new_path = mutate(path)
        delta = (distance(new_path) - distance(path)) / distance(path)
        try:
            if math.exp((delta*(-1))/temperature) > random.random():
                path = new_path
        except:
            pass
        temperature *= cooling_rate
        history.append(distance(path))
    return history, path

def distance(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += math.sqrt(math.pow(path[i][0] - path[i+1][0], 2) + math.pow(path[i][1] - path[i+1][1], 2))
    dist += math.sqrt(math.pow(path[0][0] - path[-1][0], 2) + math.pow(path[0][1] - path[-1][1], 2))
    return dist

if __name__ == "__main__":
    initial_temp = 0.05
    size = 100
    cooling_constant = 0.99997
    number_of_iteration = 100000

    start = datetime.now()

    path = generate_nodes(size)
    history, path = run_annealing(path, number_of_iteration, initial_temp, cooling_constant)

    end = datetime.now()

    path.append(path[0])
    x = [path[i][0] for i in range(len(path))]
    y = [path[i][1] for i in range(len(path))]

    plt.figure(1, figsize=(7, 15))
    plt.subplot(211)
    plt.title('Learning curve\n'
              f'Initial temperature: {initial_temp}\n'
              f'Number of trials: {number_of_iteration}\n'
              f'Cooling rate: {cooling_constant}\n'
              f'Found solution: {history[-1]}\n'
              f'Working time: {end - start}', fontsize=10, fontweight='bold')
    plt.xlabel('trials', labelpad=1)
    plt.ylabel('optimal path length', labelpad=2)
    plt.plot(history)
    plt.subplot(212)
    plt.title('Optimal path', pad=2, fontsize=10, fontweight='bold')
    plt.plot(x, y, markersize=12)
    plt.show()