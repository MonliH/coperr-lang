import interpreter
from sys import argv


tree = interpreter.get_data(argv[1])

interpreter.eval_tree(tree)
