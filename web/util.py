def extract_amount(amount):
    return float(amount.split(" ")[0])


def format_date(date):
    return date.strftime("%d/%m")


def format_time(time):
    return time.strftime("%Y-%m-%d %H:%M")
