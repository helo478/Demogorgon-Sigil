from abc import ABC, abstractmethod


class BaseMatcher(ABC):

    def __init__(self, conf):
        self.conf = conf

    @abstractmethod
    def match(self, soup):
        raise Exception("you must override abstract method 'match'")
