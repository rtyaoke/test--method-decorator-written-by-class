def stop_watch(func):
    stop_watch.calls = 0

    def inner(*args, **kwargs):
        stop_watch.calls += 1
        func(*args, **kwargs)
        print(stop_watch.calls)
    return inner


class C:

    def __init__(self, obj_prop=None):
        self.obj_prop = obj_prop

    @stop_watch
    def no_input_method(self):
        print('> no_input_method')

    @stop_watch
    def one_input_method(self, input):
        print(f'> one_input_method(input={input})')

    @stop_watch
    def print_self_prop(self):
        print(f'> print_self_prop(self.obj_prop={self.obj_prop})')


if __name__ == '__main__':
    obj1 = C()
    obj2 = C()
    obj3 = C('obj_prop_1')
    for _ in range(3):
        obj1.no_input_method()
        obj2.no_input_method()
        obj1.one_input_method('input_1')
        obj3.print_self_prop()
