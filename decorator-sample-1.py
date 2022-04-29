# from https://stackoverflow.com/questions/44968004/python-decorators-count-function-call

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        print(helper.calls)
        return func(*args, **kwargs)
    helper.calls = 0
    return helper


@call_counter
def succ(x):
    return x + 1


succ(10)
