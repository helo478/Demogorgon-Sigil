from Extractor.base_extractor import BaseExtractor


class FirstFoundFieldExtractor(BaseExtractor):

    def extract(self, soup):
        for matcher_field in self.conf['matchers']:
            matcher = self.matcher_factory.get_instance(matcher_field)
            matched = matcher.match(soup)
            if len(matched) > 0:
                return matched[0].string
