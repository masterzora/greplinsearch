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

# Dates get to be a little fun, so let's predeclare a few things
# When in doubt, stick with the Chicago Manual of Style for now
days = [r"Sunday", r"Sun", r"Su", r"Monday", r"Mon", r"M", r"Tuesday", r"Tues", r"Tu", r"Wednesday", r"Wed", r"W", r"Thursday", r"Thurs", r"Th", r"Friday", r"Fri", r"F", r"Saturday", r"Sat", r"Sa"]

months = [r"January", r"Jan", r"Ja", r"February" r"Feb", r"F", r"March", r"Mar", r"Mr", r"April", r"Apr", r"Ap", r"May", r"My", r"June", r"Jun", r"Je", r"July", r"Jul", r"Jl", r"August", r"Aug", r"Ag", r"September", r"Sept", r"Sep", r"S", r"October", r"Oct", r"O", r"November", r"Nov", r"N", r"December", r"Dec", r"D"]

timeintervals = [r"seconds?", r"s", r"minutes?", r"mins?", r"hours?", r"hrs?", r"days?", r"weeks?", r"wks?", r"months?", r"years", r"yrs?"]

relativedays = [r"today", r"tomorrow", r"yesterday"]

relativedesignators = [r"next", r"last", r"this"]

relativeregex = r"(?:" + r"|".join(relativedesignators) + r") (?:" + r"|".join(days+months) + r"week|month|year)\.?"

dates = r"[0-2]?\d|3[0-1]"

ordinals = r"st|nd|rd|th"

# this will totally bite me down the road, but I'm willing to bet nobody's scheduling appointments for 1492 or 2525
years = r"(?:19|2[0-2])?\d{2}" 

hours = r"[01]?\d|2[0-3]"

sixties = r"[0-5]\d"

# comprehensive list is possible, but let's stay US-specific for ease right now
timezones = r"[ECMPAH][DS]T|(?:Eastern|Central|Mountain|Pacific|Alaskan|Hawaiian)(?: Standard| Daylight)?(?: Time)?"

timeregex = r"\b(?:" + hours + r")(?::" + sixties + r"(?::" + sixties + r")?)?\s*[ap]?m?\s*(?:" + timezones + r")?\b"
print timeregex
time = re.compile(timeregex, re.I)

