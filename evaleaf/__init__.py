import ast
import operator as op


# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Mod: op.mod,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg, ast.Eq: op.eq, ast.LtE: op.le, ast.Lt: op.lt,
             ast.GtE: op.ge, ast.Gt: op.gt, ast.NotEq: op.ne}


def eval_expr(expr):
    return eval_(ast.parse(expr, mode='eval').body)


def eval_(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    elif isinstance(node, ast.Compare):
        return operators[type(node.ops[0])](eval_(node.left), eval_(node.comparators))
    elif isinstance(node, list):
        for n in node:
            return eval_(n)
    else:
        raise TypeError(node)
