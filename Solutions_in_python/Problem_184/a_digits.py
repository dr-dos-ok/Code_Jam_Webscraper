def solve_case(given_string):
	
	numbers = [['ZERO', 'Z', 0], \
	['TWO', 'W', 2], \
	['FOUR', 'U', 4], \
	['SIX', 'X', 6], \
	['EIGHT', 'G', 8], \
	['SEVEN', 'S', 7], \
	['FIVE', 'V', 5], \
	['NINE', 'I', 9], \
	['THREE', 'T', 3], \
	['ONE', 'N', 1]]

	phone_number = ''

	counts = dict((letter, given_string.count(letter)) for letter in set(given_string ))

	start_string = given_string
	for number in numbers:
		occurrences = process_number(counts, number[0], number[1])
		phone_number += occurrences * str(number[2])

	phone_number_ascending = ''.join(sorted(phone_number))
	return phone_number_ascending

def process_number(counts, number, unique_letter):

	occurrences = 0

	if unique_letter in counts.keys():
		if counts[unique_letter] > 0:
			occurrences = counts[unique_letter]
			for char in number:
				counts[char] += -occurrences

	return occurrences