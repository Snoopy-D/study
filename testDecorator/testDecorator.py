import functools


def log(text):
    if isinstance(text, basestring):
        def decorator(func):
            functools.wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
                print '%s %s' % (text, func.__name__)
            print '%s %s' % ('start', func.__name__)
            return wrapper
        return decorator
    else:
        def decorator(func):
            functools.wraps(func)
            def wrapper(*args, **kwargs):
                print 'Call %s:' % (func.__name__)
                return func(*args, **kwargs)
            return wrapper
        return decorator

@log('end')
def now():
    print '2018-01-18'

@log(1)
def then():
    print 'naother decorator: 2018-01-18'

now()
then()