import pluggy

namesapce = "data-reader"
hookimpl = pluggy.HookimplMarker(namesapce)
hookspec = pluggy.HookspecMarker(namesapce)


@hookspec
def limit(n: int, name: str):
    """
    return limit n rows data from table(name)
    :param n:
    :param name:
    :return:
    """
    pass


@hookspec
def read(name: str):
    """
    return a streaming read data from table(name)
    :param name:
    :return:
    """
    pass
