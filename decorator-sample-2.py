# from https://python-course.eu/advanced-python/decorators-decoration.php

def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0
    return helper


@call_counter
def succ(x):
    return x + 1


print(succ.calls)
for i in range(10):
    succ(i)
print(succ.calls)
