import importlib
import os

__wd = os.getcwd()
__dir = os.path.join(__wd, 'problems')

# load problem scripts
__problems = {}
__files = [f for f in os.listdir(__dir) if f.endswith('.py') and not f.startswith('__init__')]
for f in __files:
    __problems[f[:-3]] = importlib.import_module('problems.' + f[:-3])

if __name__ == '__main__':
    problem = input('enter problem > ')
    day = problem.split('p')[0]
    with open('./inputs/' + day + '.txt') as f:
        lines = f.readlines()
    __problems[problem].solve(lines)
