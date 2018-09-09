from Matcher.base_matcher import BaseMatcher


class AllElementAttrMatcher(BaseMatcher):

    def match(self, soup):
        element = self.conf['element']
        attr = self.conf['attr']
        key = attr['key']
        value = attr['value']
        return soup.findAll(element, {key: value})