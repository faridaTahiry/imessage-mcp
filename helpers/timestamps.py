from datetime import datetime

def normalize_timestamp(integer_timestamp):
    unix_seconds = (integer_timestamp/ 1_000_000_000) + 978_307_200
    return datetime.utcfromtimestamp(unix_seconds)