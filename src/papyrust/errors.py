class PapyrustError(Exception):
    """Base class for all papyrust exceptions"""


class UnwrapError(PapyrustError):
    """Raised when unwrapping an Err"""
