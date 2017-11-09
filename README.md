**Sudoku Scraper**
===================


Python web scraper to retrieve Sudoku puzzles from [menneske.no](http://www.menneske.no/sudoku/eng/).

Supported Sudoku puzzle sizes are:
1. 2x2
2. 3x3
3. 4x4
4. 5x5
5. 6x6
6. 7x7
7. 8x8


Running the scraper
----------

Use `python main.py arg1 arg2`, where:
* arg1 = size of the puzzle
* arg2 = number of puzzles to be saved


Where are the puzzles?
----------------------
Sudoku puzzles and their solutions are stored in .csv files named `sudokus_#.csv` depending on the size of the puzzle.
