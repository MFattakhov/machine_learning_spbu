

def main(s1, s2):
    # Задаем параметры для алгоритма
    match = 1
    INF = int(1e5)
    mismatch = -INF # Чтобы адекватно накладвать строки
    gap = -1
    a = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)] # Создаем матрицу для алгоритма
    # Начинаем заполнять матрицу
    for i in range(len(s2) + 1):
        a[i][0] = -i
    for j in range(len(s1) + 1):
        a[0][j] = -j

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            '''if s2[i - 1] == s1[j - 1]:
                a[i][j] = max(a[i - 1][j - 1] + match, a[i - 1][j] + gap, a[i][j - 1] + gap)
            else:
                a[i][j] = max(a[i - 1][j - 1] + mismatch, a[i - 1][j] + gap, a[i][j - 1] + gap)'''
            a[i][j] = max(a[i - 1][j - 1] + (match if s2[i - 1] == s1[j - 1] else mismatch), a[i - 1][j] + gap, a[i][j - 1] + gap)

    # Выводим готовую матрицу
    #for i in a:
    #   print(*i)

    # Находим обратный путь в матрице

    i = len(s2)
    j = len(s1)
    s1n = ''
    s2n = ''
    while i > 0 or j > 0:
        if i == 0:
            s1n = s1[:j] + s1n
            s2n = '-' * (j) + s2n
            break

        if j == 0:
            s2n = s2[:i] + s2n
            s1n = '-' * (i) + s1n
            break

        score = a[i][j]
        scoreDiag = a[i - 1][j - 1]
        scoreUp = a[i - 1][j]
        scoreLeft = a[i][j - 1]
        if s1[j - 1] == s2[i - 1] and score == scoreDiag + match:
            s1n = s1[j - 1] + s1n
            s2n = s2[i - 1] + s2n
            i -= 1
            j -= 1
        elif s1[j - 1] != s2[i - 1] and score == scoreDiag + mismatch:  # Можно это убрать, потому что тут строки не будут выравнваться
                                                                        # Мы сюда не должны попасть из-за значения mismatch, но в алгоритме есть
            s1n = s1[j - 1] + s1n
            s2n = s2[i - 1] + s2n
            i -= 1
            j -= 1
        elif score == scoreUp + gap:
            s1n = '-' + s1n
            s2n = s2[i - 1] + s2n
            i -= 1
        elif  score == scoreLeft + gap:
            s2n = '-' + s2n
            s1n = s1[j - 1] + s1n
            j -= 1

    # Вывод результата
    return s1n, s2n


if __name__ == '__main__':
    # Считываем строки
    s1 = input()
    s2 = input()
    s1n, s2n = main(s1, s2)
    print(s1n, s2n, sep='\n')

