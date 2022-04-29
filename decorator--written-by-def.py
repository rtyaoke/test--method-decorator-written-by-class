def stop_watch(func):
    def inner(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')

    return inner


@stop_watch
def global_func():
    print('> global_func')


if __name__ == '__main__':
    global_func()
