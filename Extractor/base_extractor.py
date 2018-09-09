from abc import ABC, abstractmethod
from Matcher.matcher_factory import MatcherFactory


class BaseExtractor(ABC):

    def __init__(self, conf):
        self.conf = conf
        self.matcher_factory = MatcherFactory

    @abstractmethod
    def extract(self, soup):
        raise Exception('you must override abstract method "extract"')
