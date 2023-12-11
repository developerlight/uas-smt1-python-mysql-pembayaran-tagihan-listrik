from datetime import date

today = date.today()

# Month abbreviation, day and year	
tanggal = today.strftime("%Y-%m-%d")
print("d4 =", tanggal)
