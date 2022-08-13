"""
 - Complex expression can be built combining 'and', 'or', and 'not' operators.
 - In this example first the expression in parenteses is evaluated to False
 - True and not (False)
 - not (False) evaluates to True since 'not' has higher precedence
 - True and True -> True
"""
True and not (1 != 1)  # evaluates to True








"""
 - In this example first the expressions in parenteses are evaluated to False
 - (False) or not (False)
 - not (False) evaluates to True since 'not' has higher precedence
 - False and True -> False
"""
(1 != 1) or not (1 >= 2)  # evaluates to False








"""
 - In this example first the expression False == True is evaluated
    since == operator has a higher precedence
 - True and (False == True) and False
 - True and False and False -> False
"""
True and False == True and False  # evaluates to False
