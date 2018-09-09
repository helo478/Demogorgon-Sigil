from bs4 import BeautifulSoup
import json
from Extractor.extractor_factory import ExtractorFactory


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
        _extracted_fields[field_name] = extracted

    return _extracted_fields


if __name__ == '__main__':
    test_schema = 'schema2.json'
    test_file = 'data1.html'
    extracted_fields = _extract_fields(test_schema, test_file)
    print(extracted_fields)
