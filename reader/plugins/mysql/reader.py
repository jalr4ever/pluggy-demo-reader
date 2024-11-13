from reader.hookspecs import hookimpl


@hookimpl
def limit(n: int, name: str):
    """
    return limit n rows data from table(name)
    :param n:
    :param name:
    :return:
    """
    print("mysql limit", n, name)


@hookimpl
def read(name: str):
    """
    return a streaming read data from table(name)
    :param name:
    :return:
    """
    print("mysql read", name)
