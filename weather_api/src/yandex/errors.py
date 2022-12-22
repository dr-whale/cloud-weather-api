class ClientError(Exception):
    pass

class InvalidMethodError(ClientError):
    pass

class BadConfigError(ClientError):
    pass

class InvalidArgumentError(ClientError):
    pass
