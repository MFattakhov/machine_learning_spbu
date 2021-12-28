
import numpy as np
import random as rd
from datetime import datetime

def lengthCal(antPath, distmat):         # Рассчитать расстояние
    length = []
    dis = 0
    for i in range(len(antPath)):
        for j in range(len(antPath[i]) - 1):
            dis += distmat[antPath[i][j]][antPath[i][j + 1]]
        dis += distmat[antPath[i][-1]][antPath[i][0]]
        length.append(dis)
        dis = 0
    return length


print('Print graph size')
size = int(input())


def createPoints(size):
    points = []
    distmat = np.array([[0 for _ in range(size)] for _ in range(size)])
    for j in range(size):
        points.append([rd.randint(0, 100), rd.randint(0, 100)])
        for i in range(len(points) - 1):
            distmat[i][j] = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            distmat[j][i] = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
    return points, distmat


points, distmat = createPoints(size)
print(points)
for i in distmat:
    print(*i)

antNum = 15                   # кол-во муравьев, столько же или меньше чем городов
alpha = 1                     # Фактор важности феромона
beta = 3                      # Фактор важности эвристической функции
pheEvaRate = 0.3              # Скорость испарения феромона
cityNum = distmat.shape[0]
pheromone = np.ones((cityNum, cityNum))                   # Феромоновая матрица
heuristic = 1 / (np.eye(cityNum) + distmat) - np.eye(cityNum)       # Матрица эвристической информации
itermax = 500                       # Итерации

startAll = datetime.now()

for iter in range(itermax):
    startIter = datetime.now()
    antPath = np.zeros((antNum, cityNum)).astype(int) - 1   # Путь муравья
    firstCity = [i for i in range(antNum)]
    rd.shuffle(firstCity)                                   # Случайный город для каждого муравья

    for i in range(len(antPath)):
        antPath[i][0] = firstCity[i]

    for i in range(cityNum - 1):                             # Обновление пути муравья
        for j in range(antNum):
            unvisted = []
            p = []
            pAccum = 0

            for k in range(cityNum):
                if k not in antPath[j]:
                    unvisted.append(k)

            for m in unvisted:
                pAccum += pheromone[antPath[j][i]][m] ** alpha * heuristic[antPath[j][i]][m] ** beta

            for n in unvisted:
                p.append(pheromone[antPath[j][i]][n] ** alpha * heuristic[antPath[j][i]][n] ** beta / pAccum)

            roulette = np.array(p).cumsum()
            #print(p, roulette)
            r = rd.uniform(min(roulette), max(roulette))
            for x in range(len(roulette)):
                if roulette[x] >= r:                      # Выбрать следующий город
                    antPath[j][i + 1] = unvisted[x]
                    break
    pheromone = (1 - pheEvaRate) * pheromone            # Феромон летучий
    length = lengthCal(antPath, distmat)
    for i in range(len(antPath)):
        for j in range(len(antPath[i]) - 1):
            pheromone[antPath[i][j]][antPath[i][j + 1]] += 1 / length[i]     # Обновление феромона
        pheromone[antPath[i][-1]][antPath[i][0]] += 1 / length[i]
    endIter = datetime.now()
    print(iter, 'iter time', endIter - startIter)
endAll = datetime.now()
print('All time', endAll - startAll)

print('minimum path length')
print(min(length))
print('minimum path')
print(antPath[length.index(min(length))])