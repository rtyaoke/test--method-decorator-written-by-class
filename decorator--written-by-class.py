class stop_watch:

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('start')
        result = self._func(self, *args, **kwargs)
        print('end')
        return result


@stop_watch
def global_func():
    print('> global_func')


if __name__ == '__main__':
    global_func()
