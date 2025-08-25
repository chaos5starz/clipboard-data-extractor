import pyperclip
import re

phoneregex = re.compile(r"(?:\+20|0020|0)?1[0125]\d{8}")
emailregex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

text = str(pyperclip.paste())

phones = phoneregex.findall(text)
emails = emailregex.findall(text)

matches = phones + emails

if matches :
    result = "\n".join(matches)
    pyperclip.copy(result)
    print(f"Extracted {len(phones)} phone(s) and {len(emails)} email(s).")
    print("Data copied to clipboard.")
else :
    print ("no data found")

    



