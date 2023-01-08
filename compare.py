from tkinter import W
from functions import levenstein
from functions import CodeChecker
import numpy as np
import sys

# путь до файла с именами файлов кода, которые надо проверить
INPUT_PATH = '/Users/ilyalobanov/ML Tinkoff/Andrey/' 

# путь до папки с кодами
PLAGIAT_PATH = '/Users/ilyalobanov/ML Tinkoff/Andrey/plagiat/'

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise AssertionError('Error while building, check the number of inputs')
    else:
        checker = CodeChecker(sys.argv[1:], INPUT_PATH, PLAGIAT_PATH)
        checker.get_result()
    
