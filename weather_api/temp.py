from datetime import datetime

date = '24.12.2022'
def date_slip(date):
    delta = datetime.strptime(date, "%d.%m.%Y").date() - datetime.today().date()
    return delta.days

print(date_slip(date))
