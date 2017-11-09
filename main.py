import pandas as pd
import numpy as np
import csv
from time import sleep
import sys
import get_puzzle
import parameters

params = parameters.params

def tryGetPuzzle(retries):
    global filename
    global curr_params

    if retries > 20:
        return

    try:
        with open(filename, 'a') as f:
            global i
            writer = csv.writer(f)

            while i <= no_puzzles:
                puzzle, solution = get_puzzle.get_sudoku(curr_params['puzzle'], curr_params['sol'])

                writer.writerow([puzzle, solution])
                f.flush()

                i += 1
    except Exception as e:
        print(e)
        sleep(2)
        retries += 1
        tryGetPuzzle(retries)


if __name__ == '__main__':
    try:
        size = int(sys.argv[1])
        if size < 2 or size > 8:
            raise Exception('Puzzle size not supported. Choose a size between 2 and 8.')

        no_puzzles = int(sys.argv[2])
    except IndexError:
        print('Arguments not found')

    curr_params = params[size]
    no_puzzles = min(curr_params['max'], no_puzzles)
    filename = 'sudokus_{}.csv'.format(size)
    i = 1

    df = pd.DataFrame({'puzzle':[], 'solution':[]})
    df.to_csv(filename, index=False, sep=',')

    tryGetPuzzle(0)
