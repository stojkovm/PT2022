"""
 - if/elif/else is a complete construct for conditional flows.
 - 'if' is mandatory part, 'elif' and 'else' are optional, depending
    on the business logic.
"""

grade_points = 87

if grade_points >= 91:
    print(
        f"With a {grade_points} point(s), you passed the exam with a grade 10")
elif grade_points >= 81:
    print(f"With a {grade_points} point(s), you passed the exam with a grade 9")
elif grade_points >= 71:
    print(f"With a {grade_points} point(s), you passed the exam with a grade 8")
elif grade_points >= 61:
    print(f"With a {grade_points} point(s), you passed the exam with a grade 7")
elif grade_points >= 51:
    print(f"With a {grade_points} point(s), you passed the exam with a grade 6")
else:
    print(f"You need minimum 51 points to pass the exam!")










"""
 - Nesting of conditions is allowed.
"""
grade_points = 91
extra_curriculum_activity = True

if grade_points >= 91:
    print(
        f"With a {grade_points} point(s), you passed the exam with a grade 10")
    if extra_curriculum_activity:
        print(f"Congratulations! We are offering you a TA position for this course.")









"""
 - Ternary operator is mechanism that provides a shorted syntax for if statements.
 - Template: <value_if_True> if <condition> else <value_if_False>
"""
loyalty_bonus_points = 55
discount = 'Yes' if loyalty_bonus_points > 50 else 'No'









"""
 - Be careful, it may be harder to read the code if condition is long.
"""
grade_points = 97
mark = 10 if grade_points >= 91 else (9 if grade_points >= 81 else (
    8 if grade_points >= 71 else (7 if grade_points >= 61 else (6 if grade_points >= 51 else 5))))
