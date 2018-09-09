from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import json


class BaseExtractor(ABC):

    def __init__(self, conf):
        self.conf = conf

    @abstractmethod
    def extract(self, soup):
        raise Exception('you must override abstract method "extract"')


class SingleFieldExtractor(BaseExtractor):

    def extract(self, soup):
        for matcher_field in self.conf['matchers']:
            matcher = MatcherFactory.get_instance(matcher_field)
            matched = matcher.match(soup)
            if len(matched) > 0:
                return matched[0].string


class ConcatMultiValueFieldExtractor(BaseExtractor):

    def extract(self, soup):
        values = []
        for matcher_field in self.conf['matchers']:
            matcher = MatcherFactory.get_instance(matcher_field)
            matched = matcher.match(soup)
            for e in matched:
                values.append(e.string)

        return str.join(' ', values)


class ExtractorFactory:

    @staticmethod
    def get_instance(conf):
        if conf['type'] == 'SingleFieldExtractor':
            return SingleFieldExtractor(conf)
        else:
            raise Exception('Unexpected extractor type: {}'.format(conf['type']))


class BaseMatcher(ABC):

    def __init__(self, conf):
        self.conf = conf

    @abstractmethod
    def match(self, soup):
        raise Exception("you must override abstract method 'match'")


class FirstElementAttrMatcher(BaseMatcher):

    def match(self, soup):
        element = self.conf['element']
        attr = self.conf['attr']
        key = attr['key']
        value = attr['value']
        return soup.findAll(element, {key: value})


class AllElementAttrMatcher(BaseMatcher):

    def match(self, soup):
        element = self.conf['element']
        attr = self.conf['attr']
        key = attr['key']
        value = attr['value']
        return soup.find(element, {key: value})


class MultiValueTitleBodyMatcher(BaseMatcher):

    def match(self, soup):
        pass


class MatcherFactory:

    @staticmethod
    def get_instance(conf):
        if conf['type'] == 'FirstElementAttrMatcher':
            return FirstElementAttrMatcher(conf)
        else:
            raise Exception('Unexpected matcher type: {}'.format(conf['type']))


def _extract_fields(schema_file, data_file):

    with open(schema_file) as schema_json:
        schema = json.load(schema_json)

    with open(data_file) as stream:
        soup = BeautifulSoup(stream, 'html.parser')

    if not schema or not schema['fields']:
        raise Exception("schema requires element 'fields'")

    _extracted_fields = {}

    for field in schema['fields']:
        field_name = field['name']
        extractor = ExtractorFactory.get_instance(field['extractor'])
        extracted = extractor.extract(soup)
#        print('{}: {}'.format(field_name, extracted))
        _extracted_fields[field_name] = extracted

    return _extracted_fields


if __name__ == '__main__':
    test_schema = 'schema2.json'
    test_file = 'data1.html'
    extracted_fields = _extract_fields(test_schema, test_file)
    print(extracted_fields)
