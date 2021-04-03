from typing import Callable, Collection, List

from pydantic import BaseModel


class IsSevenResult(BaseModel):
    isseven: bool
    explanation: str


def yep(because: str) -> IsSevenResult:
    return IsSevenResult(isseven=True, explanation=because)


def nope(because: str) -> IsSevenResult:
    return IsSevenResult(isseven=False, explanation=because)


SevenChecker = Callable[[str], IsSevenResult]


class CheckerCollection:
    """
    Represents a collection of functions that can check if something is 7
    implements Collection[SevenChecker] and is hashable.
    """

    def __init__(self, *checkers: SevenChecker):
        self.checkers = checkers

    def __len__(self):
        return len(self.checkers)

    def __contains__(self, item):
        return item in self.checkers

    def __iter__(self):
        return iter(self.checkers)

    def __hash__(self):
        return hash(tuple(self.checkers))
