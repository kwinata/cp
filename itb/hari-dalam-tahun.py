# assume format dd-mm-yyyy


def parse_and_validate(day):
	vals = day.split("-")
	if len(vals) != 3:
		raise ValueError("not following format dd-mm-yyyy")
	d, m, y = vals

	if not d.isdigit():
		raise ValueError("day not digit")
	if not m.isdigit():
		raise ValueError("month not digit")
	if not y.isdigit():
		raise ValueError("year not digit")

	d, m, y = int(d), int(m), int(y)

	month_day_count = {
		1: 31,
		2: 29 if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0) else 28,
		3: 31,
		4: 30,
		5: 31,
		6: 30,
		7: 31,
		8: 31,
		9: 30,
		10: 31,
		11: 30,
		12: 31,
	}

	if m not in month_day_count:
		raise ValueError("invalid month")
	if d > month_day_count[m]:
		raise ValueError("invalid day on month")
	return d, m, y, month_day_count

def calculate_day_range(day1, day2):
	d1, m1, y1, month_day_count = parse_and_validate(day1)
	d2, m2, y2, _ = parse_and_validate(day2)

	if y1 != y2:
		raise ValueError("can only work for same year")

	if (m1, d1) > (m2, d2):
		# swap such that m1 d1 is always smaller
		m1, d1, m2, d2 = m2, d2, m1, d2 

	if m1 == m2:
		return d2-d1

	day_in_m1 = month_day_count[m1]-d1
	day_in_m2 = d2

	day_in_months_in_between = 0
	for m in range(m1+1, m2): # (m1+1, m1+2, ...., m2-2, m2-1)
		day_in_months_in_between += month_day_count[m]

	return day_in_m1 + day_in_months_in_between + day_in_m2

def test():
	assert 2 == calculate_day_range("03-05-2000", "05-05-2000")
	assert 4 == calculate_day_range("28-09-2022", "02-10-2022")	
	assert 35 == calculate_day_range("28-08-2022", "02-10-2022")	
	assert 364 == calculate_day_range("01-01-2022", "31-12-2022")	
	assert 365 == calculate_day_range("01-01-2020", "31-12-2020")	
	assert 364 == calculate_day_range("01-01-1900", "31-12-1900")	
	assert 365 == calculate_day_range("01-01-2000", "31-12-2000")	

def main():
	day1 = input()
	day2 = input()
	print(calculate_day_range(day1, day2))

if __name__ == "__main__":
	test()
	main()