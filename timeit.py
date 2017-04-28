import time

def timeit(method):

    def timed(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()

        print('{} ({} {}) = {} {:.2f} sec'.format(method.__name__, args, kwargs, result, end_time-start_time))

        return result

    return timed

