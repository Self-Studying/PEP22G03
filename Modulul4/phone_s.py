import phonenumbers
from phonenumbers import geocoder
from termcolor import colored
from phonenumbers import carrier
phone_number = phonenumbers.parse("+40754350995")
service_provider = phonenumbers.parse("+40754350995")
text = "Please call me at +40754350995 if it's before 12:30 or on 111 is safe-house is compromised."
for match in phonenumbers.PhoneNumberMatcher(text, "RO"):
    print(colored(match,'yellow'))
    print(colored(geocoder.description_for_number(phone_number, 'en'), 'magenta'))
    print(colored(carrier.name_for_number(service_provider,'en'), 'cyan'))