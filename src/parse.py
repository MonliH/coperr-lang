from lexer import *

import ply.yacc as yacc


def raise_error(error_name, detail, line, column, code):
    print(f"Coperr.{error_name}: {detail} at -l{line}c{column}-\n\"{code}\"")

    quit()


def toString(args):
    return "".join(args)


def c_parse():

    # MAIN PROGRAM
    def p_program(p):
        """program : actions"""
        p[0] = p[1]

    def p_actions(p):
        """actions : actions action"""
        p[1].append(p[2])
        p[0] = p[1]

    def p_actions1(p):
        """actions : action"""
        p[0] = [p[1]]

    def p_action(p):
        """action : get_py ';'
                  | function_call ';'
                  | variable_dec ';'
                  | conditional
                  | nill ';'"""
        p[0] = p[1]

    # IMPORTS
    def p_get_py(p):
        """get_py : GETPY STRING"""
        p[0] = ["GETPY", p[2]]

    # CONDITIONALS
    def p_conditional(p):
        """conditional : if_statement else_if_loop else_statement"""
        p[0] = ["CONDITIONAL", p[1], p[2], p[3]]

    def p_conditional1(p):
        """conditional : if_statement else_if_loop"""
        p[0] = ["CONDITIONAL", p[1], p[2]]

    def p_conditional2(p):
        """conditional : if_statement"""
        p[0] = ["CONDITIONAL", p[1]]

    def p_else_if_loop(p):
        """else_if_loop : else_if_loop else_if_statement"""
        p[1].append(p[2])
        p[0] = p[1]

    def p_else_if_loop2(p):
        """else_if_loop : else_if_statement"""
        p[0] = p[1]

    def p_if_statement(p):
        """if_statement : IF '(' bool_expression ')' '{' actions '}'"""
        p[0] = ["IF_STATEMENT", p[3], p[6]]

    def p_else_if_statement(p):
        """else_if_statement : ELSIF '(' bool_expression ')' '{' actions '}'"""
        p[0] = ["ELSE_IF_STATEMENT", p[3], p[6]]

    def p_else_statement(p):
        """else_statement : ELSE '{' actions '}'"""
        p[0] = ["ELSE_STATEMENT", p[3]]

    # FUNCTIONS
    def p_function_call(p):
        """function_call : object '(' function_input ')'"""
        p[0] = ["FUNCTION_CALL", p[1], p[3]]

    def p_function_input(p):
        """function_input : expression
                          | expression ',' function_input
                          | nill"""
        if len(p) == 4:
            p[0] = ["MULTIPLE_ARGUMENTS", p[1], p[3]]
        elif len(p) == 2:
            p[0] = ["ARGUMENT", p[1]]

    # VARIABLES
    def p_variable_dec(p):
        """variable_dec : object '=' expression"""
        p[0] = ["VARIABLE_DEC", p[1], p[3]]

    # EXPRESSIONS
    def p_expression_math(p):
        """expression : math"""
        p[0] = p[1]

    def p_expression(p):
        """expression : INT"""
        p[0] = ["INT", p[1]]

    def p_expression1(p):
        """expression : FLOAT"""
        p[0] = ["FLOAT", p[1]]

    def p_expression2(p):
        """expression : STRING"""
        p[0] = ["STRING", p[1]]

    def p_expression3(p):
        """expression : bool_expression"""
        p[0] = p[1]

    def p_expression4(p):
        """expression : object"""
        p[0] = p[1]

    def p_object(p):
        """object : NAME"""
        p[0] = ["OBJECT", p[1]]

    # MATH
    def p_math(p):
        """math : expression '/' expression
                | expression '*' expression
                | expression '-' expression
                | expression '+' expression
                | expression '%' expression
                | expression '^' expression"""

        p[0] = [p[1], str(p[2]), p[3]]

    # BOOLEANS
    def p_bool_expression(p):
        """bool_expression : BOOL"""
        p[0] = ["BOOL", p[1]]

    def p_bool_expression1(p):
        """bool_expression : expression EQ expression"""
        p[0] = ["BOOL_EXPR_EQ", p[1], p[3]]

    def p_bool_expression2(p):
        """bool_expression : '!' bool_expression"""
        p[0] = ["NOT", p[2]]

    def p_bool_expression3(p):
        """bool_expression : bool_expression '&' bool_expression"""
        p[0] = [p[1], "AND", p[3]]

    def p_bool_expression4(p):
        """bool_expression : bool_expression '|' bool_expression"""
        p[0] = [p[1], "OR", p[3]]

    def p_bool_expression5(p):
        """bool_expression : number '>' number
                           | number '<' number"""
        p[0] = ["BOOL_MATH_COMPARE", p[1],  p[2], p[3]]

    # NILL / NONE / NULL
    def p_nill(p):
        """nill : NILL"""
        p[0] = ["NILL", p[1]]

    def p_number(p):
        """number : INT"""
        p[0] = ["INT", p[1]]

    def p_number1(p):
        """number : FLOAT"""
        p[0] = ["FLOAT", p[1]]

    def p_number2(p):
        """number : object"""
        p[0] = p[1]

    """
    # ERROR HANDLING
    def p_function_call_error(p):
        "function_call_error : object '(' error ')' ';'"
        raise_error("FunctionInputNillError", "Function input cannot not be empty, instead pass nill; to the function",
                    p.lineno(0), p.lexpos(0), toString([p[1], p[2], p[3]]))

    """

    def p_error(p):
        print("Coperr.SyntaxError: Unknown Syntax Error")
        quit()

    return yacc.yacc()


def get_file(filename):
    file_obj = open(filename, "r")
    data = file_obj.read() + "nill;"
    file_obj.close()

    return data
