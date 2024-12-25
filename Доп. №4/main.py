import re
import urllib.request
import csv

site = urllib.request.urlopen('https://msk.spravker.ru/avtoservisy-avtotehcentry')
html_content = site.read().decode()

pattern = r"(?:-link\">)(?P<name>[^<]+)(?:[^o]*[^l]*.*\n *)(?P<address>[^\n]+)(?:\s*.*>\s*.*>\s*.*>\s*<d[^>]*>\s*.*\s*.*>(?P<phone>[^<]+).*>\s*</dl>)?(?:\s*<.*>\s*<.*\s*<.*>(?P<workhour>[^<]+)</dd>)?"
match = re.findall(pattern, html_content)

with open('out_data.csv', 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', ' Address', ' Phone number', ' Work hours'])
    writer.writerows(match)

matches = re.finditer(pattern, html_content)

for match in matches:
    print("Name:", match.group('name'))
    print("Address:", match.group('address'))
    print("Phone:", match.group('phone'))
    print("Work hours:", match.group('workhour'))
    print("\n")
