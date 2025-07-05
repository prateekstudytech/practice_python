import re

def extract_emails(text: str) -> list:
   pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
   match = pattern.findall(text)
   return match

def extract_dates(text: str) -> list:
  pattern = re.compile(
    r'\b(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-[0-9]{4}\b')
  return [match.group(0) for match in pattern.finditer(text)]

def is_valid_ipv4(ip: str) -> bool:
  pattern = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')
  match = pattern.match(ip)
  if not match:
    return False
  ip_nums = match.groups()
  for num in ip_nums:
    if num != str(int(num)):
      return False  # has leading zeros
    num = int(num)
    if not 0 <= num <= 255:
      print("Wrong IP")
      return False
  return True


if __name__ == '__main__':
  #  text = "Please contact us at support@example.com or sales@domain.co.in"
  #  emails = extract_emails(text)
  #  print(emails)
  ip = "124.0.1.244"
  is_valid_ipv4(ip)
