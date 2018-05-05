import operator, urllib.request, os

########################################################################################
### Error Checking
class Error(Exception):
	'''Base classe for other exceptions'''
	pass

class ValueTooSmall(Error):
	'''Raised when the input value is too small'''
	pass

class ValueTooLarge(Error):
	'''Raised when the input value is too large'''
	pass

while True:
	try:
		num = input("Please enter a number between 1-69: ")
		num = int(num)
		answer = True
		if(num > 69):
			raise ValueTooLarge
		elif(num < 1):
			raise ValueTooSmall
		break
	except ValueError: 
		print("Please enter a valid whole number! Please try again...")
	except ValueTooSmall:
		print("Your number is too small, must be greater than 0! Please try again...")
	except ValueTooLarge:
		print("Your number is too large, must be less than 101! Please try again...")
##############################################################################################

#################################################
###Get csv file from internet
my_path = os.getcwd()

print('Beginning file download with urllib2...')

url = 'https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD'

download_path = my_path + '\winning_numbers.csv'

urllib.request.urlretrieve(url, download_path)
#################################################


#################################################
## Open and process file

nf = open('winning_numbers.csv', 'r')

my_huge_list = []
next(nf) #skip first line
for x in nf:
    l = x.split(',')
    m = l[1].split(' ')
    for x in m:
        my_huge_list.append(int(x))

occur_count = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
'16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0, '31': 0,
'32': 0, '33': 0, '34': 0, '35': 0, '36': 0, '37': 0, '38': 0, '39': 0, '40': 0, '41': 0, '42': 0, '43': 0, '44': 0, '45': 0, '46': 0, '47': 0,
'48': 0, '49': 0, '50': 0, '51': 0, '52': 0, '53': 0, '54': 0, '55': 0, '56': 0, '57': 0, '58': 0, '59': 0, '60': 0, '61': 0, '62': 0, '63': 0, 
'64': 0, '65': 0, '66': 0, '67': 0, '68': 0, '69': 0}

for x in my_huge_list:
    occur_count[str(x)] = occur_count[str(x)] + 1

sorted_d = sorted(occur_count.items(), key=operator.itemgetter(1))

list1 = []
list2 = []
for (x1, x2) in sorted_d:
	list1.append(x1)
	list2.append(str(x2))
print("Your top " + str(num) + " numbers chosen for lottery are: ")
range_num = (69-num)

for x in range(range_num, 69):
	print(list1[x] + " chosen " + list2[x] + " times")

nf.close()

######################################################################

