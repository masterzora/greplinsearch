import extractregexes

def extract(document):
    '''
        input: document, the string to be indexed
        ouput: a list of dicts, each indicating the start and end point
                   and type of a found entity
    '''
    entities = []
    for m in extractregexes.phonenumber.finditer(document):
        entities += [{'start': m.start(), 'end': m.end(), 'type': 'phonenumber'}]
    for m in extractregexes.mailingaddress.finditer(document):
        entities += [{'start': m.start(), 'end': m.end(), 'type': 'address'}]
    for m in extractregexes.flightconfirmation.finditer(document):
        entities += [{'start': m.start(), 'end': m.end(), 'type': 'flightconfirmation'}]
    for m in extractregexes.time.finditer(document):
        entities += [{'start': m.start(), 'end': m.end(), 'type': 'time'}]
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
    
def testfile(filename):
    '''
        input: filename, a string with the document to check
        output: none; prints found entities to stdout
        Some easy scaffolding to check outputs
    '''
    entities = extractfile(filename)
    for i in entities:
        print i['type'], ":"
        print checksubfile(filename, i['start'], i['end'])
