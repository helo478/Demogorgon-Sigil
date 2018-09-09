from Extractor.base_extractor import BaseExtractor


class ConcatAllFieldExtractor(BaseExtractor):

    def extract(self, soup):
        values = []
        for matcher_field in self.conf['matchers']:
            matcher = self.matcher_factory.get_instance(matcher_field)
            matched = matcher.match(soup)
            for e in matched:
                values.append(e.string)

        return str.join(' ', values)