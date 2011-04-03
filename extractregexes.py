import re

# precompiling regexes will make it faster for repeated operations

phonenumberregex  = r"\b((?:\+?1[.\- ])?" # country code
phonenumberregex += r"\(?[\dA-Z]{3}\)?[.\- ]" # area code
phonenumberregex += r"[\dA-Z]{3}[.\- ][\dA-Z]{4}" # and the rest
phonenumberregex += r"|\+[\dA-Z]{11})\b" # 11-digits no separator means you have to use +
phonenumber = re.compile(phonenumberregex)

mailingaddressregex  = r"\d+" # Street number
mailingaddressregex += r"\s+[\dA-Za-z \-.\']+\s*\n\s*" # Street, Apt, etc
mailingaddressregex += r"[A-Za-z \-.\']+" # City
mailingaddressregex += r",\s+[A-Z]{2}" # State
mailingaddressregex += r"\s+\d{5}(?:-\d{4})?" # ZIP code
mailingaddress = re.compile(mailingaddressregex)

flightconfirmationregex  = r"\b([A-Z\d]{6}" # Most airlines use 6 alphanumerics
flightconfirmationregex += r"|\d{13}" # United
flightconfirmationregex += r")\b"
flightconfirmation = re.compile(flightconfirmationregex)

