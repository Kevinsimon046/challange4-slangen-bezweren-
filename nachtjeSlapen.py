import datetime

vandaag_datum = datetime.date.today()

jaar = int(input("geef hier het jaar door:\n"))
maand = int(input("geef hier de maand aan:\n"))
dag = int(input("geef hier de dag aan:\n"))

datum = datetime.date(jaar, maand, dag)
vandaag_datum = datetime.date.today()

delta = datum - vandaag_datum

print("hieronder ziet u uw voor of achterlopende dagen. ")
print(delta.days ,"dagen")