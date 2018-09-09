from Extractor.first_found_field_extractor import FirstFoundFieldExtractor
from Extractor.concat_all_field_extractor import ConcatAllFieldExtractor


class ExtractorFactory:

    @staticmethod
    def get_instance(conf):
        if conf['type'] == 'FirstFoundFieldExtractor':
            return FirstFoundFieldExtractor(conf)
        elif conf['type'] == 'ConcatAllFieldExtractor':
            return ConcatAllFieldExtractor(conf)
        else:
            raise Exception('Unexpected extractor type: {}'.format(conf['type']))

