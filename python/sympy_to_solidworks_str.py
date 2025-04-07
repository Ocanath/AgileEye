import sympy as sp

def sympy_to_solidworks(sympy_expr):
    return str(sympy_expr).replace('**', '^').replace('sqrt','sqr').replace("asin","arcsin").replace("acos","arccos")
