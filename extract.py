import re

phonenumberregex = '(?:\b\+?1[.\- ])?' # country code
phonenumberregex += '\(?[\dA-Z]{3}\)?[.\- ]' # area code
phonenumberregex += '[\dA-Z]{3}[.\- ][\dA-Z]{4}\W' # and the rest
phonenumberregex += '|\+[\dA-Z]{11}' # 11-digits no separator means you have to use +
phonenumber = re.compile(phonenumberregex)

mailingaddressregex = '\d+' # Street number
mailingaddressregex += '\s+[\dA-Za-z \-.\']+\s*\n\s*' # Street, Apt, etc
mailingaddressregex += '[A-Za-z \-.\']+' # City
mailingaddressregex += ',\s+[A-Z]{2}' # State
mailingaddressregex += '\s+\d{5}(?:-\d{4})?' # ZIP code
mailingaddress = re.compile(mailingaddressregex)

def extract(document):
    '''
        input: document, the string to be indexed
        ouput: a list of dicts, each indicating the start and end point
                   and type of a found entity
    '''
    entities = []
    for m in phonenumber.finditer(document):
        entities += [{'start': m.start(), 'end': m.end(), 'type': 'phonenumber'}]
    for m in mailingaddress.finditer(document):
        entities += [{'start': m.start(), 'end': m.end(), 'type': 'address'}]
    return entities

def extractfile(filename):
    '''
        input: filename, a stringe with the document to be indexed
        ouput: a list of dicts, each indicating the start and end point
                   and type of a found entity
        This is mostly to make it easy to test extract()
    '''
    f = open(filename, 'r')
    document = f.read()
    f.close()
    return extract(document)
