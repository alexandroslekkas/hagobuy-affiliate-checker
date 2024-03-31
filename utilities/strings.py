def get_clean_number(text_value):
    return float(text_value.replace('$', '').replace(',', '').strip())