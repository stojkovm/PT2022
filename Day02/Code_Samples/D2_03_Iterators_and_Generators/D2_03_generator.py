"""
 - 'yield' keyword returns the value and pauses execution.
 - When generator is called again, it resumes on the line after 'yield' keyword.
"""


def gen_AB():
    print("start")
    yield "A"
    print("continue")
    yield "B"
    print("end.")


for ch in gen_AB():
    print("-->", ch)
