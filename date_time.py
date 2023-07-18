import datetime

now = datetime.datetime.now()
print(datetime.datetime.now())
print(datetime.date.today())

print(now.strftime("%d:%b:%Y"))

x = datetime.datetime(year=2020, day=4, month=12)
y = datetime.datetime(year=2023, day=23, month=6)

dif = y - x
print(dif)

end = datetime.datetime.now()

differ = end - now

print(differ)
