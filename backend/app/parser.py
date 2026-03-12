import re

def parse_receipt(text):

    items = []

    lines = text.split("\n")

    for line in lines:

        match = re.search(r'(.+?)\s+(\d+)$', line)

        if match:

            items.append({
                "name": match.group(1),
                "price": int(match.group(2))
            })

    return items
