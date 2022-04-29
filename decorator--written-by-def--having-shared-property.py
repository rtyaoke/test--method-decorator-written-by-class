def stop_watch(func):
    def inner(*args, **kwargs):
        inner.calls += 1
        func(*args, **kwargs)
        print(inner.calls)
    inner.calls = 0

    return inner


@stop_watch
def global_func():
    print('> global_func')


if __name__ == '__main__':
    global_func()
    global_func()
    global_func()
    global_func()
    global_func()
