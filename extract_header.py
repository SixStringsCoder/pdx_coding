"""
Write a function named extract_domain that will print the first matching domain name in a given string.

>>> extract_domain("kieran@pdxcodeguild.com")
"pdxcodeguild.com"

>>> extract_domain("domain of jwackman@hvc.rr.com designates 2a00:1450:400c:c09::22d as permitted sender")
"hvc.rr.com"

"""


def extract_domain(domain):
  start = domain.index('@') + 1
  com = domain.index('.com') + 4
  slicer = domain[start:com]
  print(slicer)


def email_addie():
    email = input("Type your email address. >>")
    extract_domain(email)


email_addie()