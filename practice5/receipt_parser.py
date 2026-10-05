import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Prices
prices = re.findall(r"\d[\d ]*,\d{2}", text)

# Product names
products = re.findall(r"^\d+\\?\.\s*\n(.+)", text, re.M)

# Total
total = re.search(r"ИТОГО:\s*([\d ]+,\d{2})", text).group(1)

# Date and time
date, time = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
    text
).groups()

# Payment
payment = re.search(r"(Банковская карта|Наличные)", text).group(1)

data = {
    "products": products,
    "prices": prices,
    "total": total,
    "date": date,
    "time": time,
    "payment": payment
}

print(json.dumps(data, ensure_ascii=False, indent=2))

