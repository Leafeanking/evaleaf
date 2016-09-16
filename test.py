import evaleaf
import six

operators = ['+','-','*','**','/','%','<','<=','>', '>=', '==', '!=']

for o in operators:
    expr = '1{}1'.format(o)
    six.print_('\'{}\'\t='.format(expr),  evaleaf.eval_expr(expr))
