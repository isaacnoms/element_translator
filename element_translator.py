
import csv

letter_element = {}

csvfile = open('elements.csv')
reader = csv.DictReader(csvfile)
for row in reader:
	symbol = row['symbol'].lower()
	element = row['element']
	letter_element[symbol] = element
csvfile.close()

trans_message = []

message = input('Message: ').lower()

def element_finder(message):
	result = []
	for e in letter_element:
		if message.startswith(e):
			#print(letter_element[e])
			#result.append(letter_element[e])
			remainder = message[len(e):]
			if remainder == '':
				return [[letter_element[e]]]

			for i in element_finder(remainder):
				i.insert(0, letter_element[e])
				#print(i)
				result.append(i)

	if result == []:
		remainder = message[1:]
		if not remainder:
			return[[message[0].upper()]]
		for i in element_finder(remainder):
			#print(i)
			i.insert(0, message[0].upper())
			result.append(i)
		#print(result)
	return result


options = element_finder(message)

last_op = 0
for op in options:
	if last_op == 0 or len(op) < len(last_op):
		last_op = op

#print(options)
print(''.join(last_op))
