import re

# precompiling regexes will make it faster for repeated operations

phonenumberregex = '(?:\\b\+?1[.\- ])?' # country code
phonenumberregex += '\(?[\dA-Z]{3}\)?[.\- ]' # area code
phonenumberregex += '[\dA-Z]{3}[.\- ][\dA-Z]{4}\\b' # and the rest
phonenumberregex += '|\+[\dA-Z]{11}' # 11-digits no separator means you have to use +
phonenumber = re.compile(phonenumberregex)

mailingaddressregex = '\d+' # Street number
mailingaddressregex += '\s+[\dA-Za-z \-.\']+\s*\n\s*' # Street, Apt, etc
mailingaddressregex += '[A-Za-z \-.\']+' # City
mailingaddressregex += ',\s+[A-Z]{2}' # State
mailingaddressregex += '\s+\d{5}(?:-\d{4})?' # ZIP code
mailingaddress = re.compile(mailingaddressregex)

flightconfirmationregex = '\\b([A-Z\d]{6}' # Most airlines use 6 alphanumerics
flightconfirmationregex += '|\d{13}' # United
flightconfirmationregex += ')\\b'
flightconfirmation = re.compile(flightconfirmationregex)

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
    for m in flightconfirmation.finditer(document):
        entities += [{'start': m.start(), 'end': m.end(), 'type': 'flightconfirmation'}]
    return entities

def extractfile(filename):
    '''
        input: filename, a string with the document to be indexed
        ouput: a list of dicts, each indicating the start and end point
                   and type of a found entity
        This is mostly to make it easy to test extract()
    '''
    f = open(filename, 'r')
    document = f.read()
    f.close()
    return extract(document)

def checksubfile(filename, start, end):
    '''
        input: filename, a string with the document to check
               start, end: slicing indices for the document
        output: the startth-endth chars of the document
        Some easy scaffolding to check what is found
    '''
    f = open(filename, 'r')
    document = f.read()
    f.close()
    return document[start:end]
    
