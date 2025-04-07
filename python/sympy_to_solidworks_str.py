import sympy as sp

def sympy_to_solidworks(sympy_expr, symbol_mapping=None):
    """
    Converts a SymPy expression to a string suitable for SolidWorks equations.

    Args:
        sympy_expr: The SymPy expression to convert.
        symbol_mapping (dict, optional): A dictionary mapping SymPy symbols
                                         to SolidWorks variable names.
                                         Defaults to None (SymPy symbol names used directly).

    Returns:
        str: A string representation of the SymPy expression formatted for SolidWorks.
    """

    if symbol_mapping is None:
        symbol_mapping = {}

    def custom_printer(expr):
        if isinstance(expr, sp.Symbol):
            return symbol_mapping.get(str(expr), str(expr))
        elif isinstance(expr, sp.Pow):
            base = custom_printer(expr.args[0])
            exponent = custom_printer(expr.args[1])
            return f"({base})^({exponent})"
        elif isinstance(expr, sp.Mul):
            args_str = [custom_printer(arg) for arg in expr.args]
            return "*".join(args_str)
        elif isinstance(expr, sp.sin):
            return f"SIN({custom_printer(expr.args[0])})"
        elif isinstance(expr, sp.cos):
            return f"COS({custom_printer(expr.args[0])})"
        elif isinstance(expr, sp.tan):
            return f"TAN({custom_printer(expr.args[0])})"
        elif isinstance(expr, sp.asin):
            return f"ASIN({custom_printer(expr.args[0])})"
        elif isinstance(expr, sp.acos):
            return f"ACOS({custom_printer(expr.args[0])})"
        elif isinstance(expr, sp.atan):
            return f"ATAN({custom_printer(expr.args[0])})"
        elif isinstance(expr, sp.sqrt):
            return f"SQRT({custom_printer(expr.args[0])})"
        elif isinstance(expr, sp.log):
            return f"LN({custom_printer(expr.args[0])})" # Natural log in SolidWorks
        # Add more function mappings as needed
        elif isinstance(expr, (int, float)):
            return str(expr)
        else:
            return str(expr) # Fallback to default string representation

    return custom_printer(sympy_expr)