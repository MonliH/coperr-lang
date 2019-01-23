import ply.lex as lex

reserved = {
    "elsif": "ELSIF",
    "else": "ELSE",
    "if": "IF",
    "nill": "NILL",
    "fun": "FUN",
    "give": "GIVE"
}

tokens = [
    "INT",
    "FLOAT",
    "NAME",
    "EQ",
    "BOOL",
    "STRING",

] + list(reserved.values())


literals = ["+", "-", "*", "/", "(", ")", "=", ";", "{", "}", ",", ":", "|", "&", "!", "<", ">", "%"]


def c_lexer():

    t_EQ = r"=="

    def t_COMMENT(t):
        r"\#.*"

    def t_STRING(t):
        r"\"[_A-Za-z0-9 \t\n!@#$%^&*()_+;:'<>,./?=]+\""
        t.value = str(t.value)[1:-1]
        return t

    def t_BOOL(t):
        r"(true|false)"
        if t.value == "true":
            t.value = True
        if t.value == "false":
            t.value = False

        return t

    def t_ID(t):
        r"[a-zA-Z_]+[a-zA-Z_0-9]*"
        if t.value in reserved:
            t.type = reserved[t.value]
        else:
            t.type = "NAME"

        return t

    def t_FLOAT(t):
        r"\d+\.\d+"
        t.value = float(t.value)
        return t

    def t_INT(t):
        r"\d+"
        t.value = int(t.value)
        return t

    t_ignore = ' \t'

    def t_error(t):
        print("Coperr.UnexpectedCharacter {}".format(t.value[0]))
        t.lexer.skip(1)

    return lex.lex()  # errorlog=lex.NullLogger() to not show warnings
