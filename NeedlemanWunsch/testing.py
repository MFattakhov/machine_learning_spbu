import main
import os

TEST_PATH = './tests/'

for i in os.listdir(TEST_PATH):
    with open(TEST_PATH + i) as f:
        s1 = f.readline()
        s2 = f.readline()
        s1n, s2n = main.main(s1, s2)
        print(len(s1n), len(s2n))

