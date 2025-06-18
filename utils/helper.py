def flag_emoji(country_code):
    return chr(0x1F1E6 + ord(country_code[0]) - ord('A')) + \
           chr(0x1F1E6 + ord(country_code[1]) - ord('A'))
