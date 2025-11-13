import re
def contains_pii(text):
    if re.search(r"\b\d{10,}\b", text): return True
    if re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text): return True
    return False
