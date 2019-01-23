import parse
import pprint


def get_data(file):
    data = parse.get_file(file)
    lexer = parse.c_lexer()
    lexer.input(data)

    while True:
        tok = lexer.token()
        print(tok)
        if not tok:
            break
    parser = parse.c_parse()
    tree = parser.parse(data)
    return tree


def eval_math(tree, variables):
    if tree[0] in ["INT", "FLOAT", "STRING", "OBJECT"]:
        return eval_expression(tree, variables)

    elif type(tree[0]) is list and type(tree[2]) is list:
        if tree[1] == "/":
            return eval_math(tree[0], variables) / eval_math(tree[2], variables)
        elif tree[1] == "*":
            return eval_math(tree[0], variables) * eval_math(tree[2], variables)
        elif tree[1] == "+":
            return eval_math(tree[0], variables) + eval_math(tree[2], variables)
        elif tree[1] == "-":
            return eval_math(tree[0], variables) - eval_math(tree[2], variables)
        elif tree[1] == "%":
            return eval_math(tree[0], variables) % eval_math(tree[2], variables)
        elif tree[1] == "^":
            return eval_math(tree[0], variables) ^ eval_math(tree[2], variables)


def eval_expression(tree, variables):
    if tree[0] in ["INT", "FLOAT", "STRING", "NILL"]:
        return tree[1]

    elif tree[0] == "OBJECT" and tree[1] in variables:
        return variables[tree[1]]

    elif tree[0] == "OBJECT" and tree[1] not in variables:
        print("VariableError: variable referenced before assignment!")
        quit()

    elif tree[1] in ["/", "*", "+", "-", "%", "^"]:
        return eval_math(tree, variables)

    else:
        print("Coperr.InternalExprEvaluateError: Attempted to evaluate expression that is not implemented")
        quit()


def eval_function(tree, variables):
    function_name = tree[1][1]

    if tree[2][0] == "ARGUMENT":
        function_argument = eval_expression(tree[2][1], variables)

    if function_name == "print":
        print(function_argument)

    elif function_name == "input":
        print(input(function_argument))


def eval_bool(tree, variables):
    if len(tree) == 2 and tree[0] == "BOOL":
        return tree[1]

    elif tree[0] == "BOOL_EXPR_EQ":
        if eval_bool(tree[1], variables) == eval_bool(tree[2], variables):
            return True
        else:
            return False

    elif tree[0] == "BOOL_MATH_COMPARE":
        if tree[2] == ">":
            if eval_expression(tree[1], variables) > eval_expression(tree[3], variables):
                return True
            else:
                return False

        elif tree[2] == "<":
            if eval_expression(tree[1], variables) < eval_expression(tree[3], variables):
                return True
            else:
                return False

    elif type(tree[0]) is list and tree[1] in ["AND", "OR"] and type(tree[2]) is list:
        arg1 = eval_bool(tree[0], variables)
        arg2 = eval_bool(tree[2], variables)

        if tree[1] == "AND":
            if arg1:
                if arg2:
                    return True
            else:
                return False

        elif tree[1] == "OR":
            if arg1:
                return True
            if arg2:
                return True
            else:
                return False

    elif tree[0] == "NOT":
        arg = eval_bool(tree[1], variables)

        if arg:
            return False
        else:
            return True

    elif tree[0] in ["INT", "FLOAT", "STRING", "NILL", "OBJECT", "MATH"]:
        return eval_expression(tree, variables)

    else:
        print("Coperr.InternalBoolEvaluateError: used boolean statement that is invalid/has not been implemented")
        quit()


def eval_conditional(tree, variables):

    if tree[0][0] == "IF_STATEMENT" and len(tree) == 1:
        if eval_bool(tree[0][1], variables):
            eval_tree(tree[0][2])
            return True

    elif tree[0][0] == "ELSE_IF_STATEMENT" and len(tree) == 1:
        if eval_bool(tree[0][1], variables):
            eval_tree(tree[0][2])
            return True

    elif len(tree) == 3 and tree[1][0] == "ELSE_IF_STATEMENT":
        if eval_conditional([tree[0]], variables):
            return None
        elif eval_conditional([tree[1][0:3]], variables):
            return None
        for i in range(len(tree[1])-3):
            if eval_conditional([tree[1][i+3]], variables):
                return None
        else:
            eval_tree(tree[2][1])
            return None


def eval_tree(tree, variables={}):
    # for debugging
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(tree)

    action_number = len(tree)

    for i in range(action_number):
        action_type = tree[i][0]
        if action_type == "VARIABLE_DEC":
            variables[tree[i][1][1]] = eval_expression(tree[i][2], variables)

        elif action_type == "FUNCTION_CALL":
            eval_function(tree[i], variables)

        elif action_type == "CONDITIONAL":
            eval_conditional(tree[i][1:], variables)

        elif action_type == "NILL":
            continue
