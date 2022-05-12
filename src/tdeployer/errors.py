class TDeployerBaseError(Exception):
    """基础异常类

    Args:
        Exception (_type_): _description_
    """

    pass


class ServiceNotFound(TDeployerBaseError):
    """服务没找到

    Args:
        TDeployerBaseError (_type_): _description_
    """


class InvalidCommand(TDeployerBaseError):
    """无效命令错误

    Args:
        TDeployerBaseError (_type_): _description_
    """