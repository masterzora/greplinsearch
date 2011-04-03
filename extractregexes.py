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
