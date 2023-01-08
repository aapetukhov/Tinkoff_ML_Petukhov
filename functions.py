import ast

def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


class CodeChecker: 

    def __init__(self, argv, input_path, plagiat_path): 
        self.input_name = argv[0]
        self.output_name = argv[1]
        self.INPUT_PATH = input_path
        self.PLAGIAT_PATH = plagiat_path
        self.result = open(self.INPUT_PATH + 'output.txt', 'w')

    def get_result(self): 
        input_file = open(self.INPUT_PATH + self.input_name, 'r')

        for line in input_file:
            arr = line.split()

            # препроцессинг первого файла
            code_0 = open(self.PLAGIAT_PATH + arr[0], 'r')
            str_0 = ast.dump(ast.parse(code_0.read()))
            
            # препроцессинг второго файла
            code_1 = open(self.PLAGIAT_PATH + arr[1], 'r')
            str_1 = ast.dump(ast.parse(code_1.read()))
            
            local_score = self.score(str_0, str_1)

            self.result.write(str(local_score) + '\n')

    def score(self, str1, str2):
        return levenstein(str1,str2)