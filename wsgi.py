from app import main

def app(*args, **kwargs):
    import sys
    sys.argv = ['--wsgi']
    for k in kwargs:
        ck = k.replace("_", "-")
        sys.argv.append(f"--{ck}")
        if not isinstance(kwargs[k], bool) or not kwargs[k]:
            sys.argv.append(kwargs[k])

    instance = main()

    return instance if kwargs else instance(*args, **kwargs)
