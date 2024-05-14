#!/usr/bin/env python3

import sys
from transliterate import translit, get_available_language_codes

# Read text from standard input (pipe)
text = sys.stdin.read()

# Transliterate to English (language code 'en')
latin_text = translit(text, 'ru', 'en')

# Print the transliterated text
print(latin_text)
