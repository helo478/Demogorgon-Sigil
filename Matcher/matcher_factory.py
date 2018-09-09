from Matcher.first_found_element_attr_matcher import FirstFoundElementAttrMatcher
from Matcher.all_element_attr_matcher import AllElementAttrMatcher


class MatcherFactory:

    @staticmethod
    def get_instance(conf):
        if conf['type'] == 'FirstFoundElementAttrMatcher':
            return FirstFoundElementAttrMatcher(conf)
        elif conf['type'] == 'AllElementAttrMatcher':
            return AllElementAttrMatcher(conf)
        else:
            raise Exception('Unexpected matcher type: {}'.format(conf['type']))
