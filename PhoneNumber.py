

import re
def isValidPhoneNumber(phone):
    pattern = r"\(\d{3}\) \d{3}-\d{4}"
    return bool(re.match(pattern, phone))

print(isValidPhoneNumber("(123) 456-7890"))
print(isValidPhoneNumber("1111)555 2345"))
print(isValidPhoneNumber("098) 123 4567"))