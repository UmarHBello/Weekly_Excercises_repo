
text1 = 'Thirty'
text2 = 'Days'
text3 = 'of'
text4 = 'python'
result = text1 + ' ' + text2 + ' ' + text3 + ' ' + text4
print(result)

text5 = 'coding'
text6 = 'for'
text7 = 'All ArewaDs'
result2 = text5 + ' ' + text6 + ' ' + text7
print(result2)


company = 'Coding for All'
'''''''''
print(company)
lenth = (len(company))
print(lenth)
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

sliced = company.split(' ', 1)
print(sliced)

company = company.find('Coding')
print(company)
'''''

company_modified = company.replace('Coding', 'Python')
print(company_modified)

newtext = 'Python for Everyone'
newtext_m = newtext.replace('Everyone', 'All')
print(newtext_m)

print(company.split(' '))         

Socials = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
socials_list = Socials.split(', ')
print(socials_list)

char_index = (company[0])
print(char_index)

last_index = (company[-1])
print(last_index)

char_index10 = (company[10])
print(char_index10)

index_of_c = company.index('C')
index_of_f = company.index('f')
print(index_of_c)
print(index_of_f)

last_oc_l = company.rfind('l')
print(last_oc_l)

sentence = 'You cannot end a sentence with because because because is a conjunction'
findindex = sentence.find('because')
print(findindex)

findindexr = sentence.rfind('because')
print(findindexr)

sliced_sentence = sentence.split('because', 2)
print(sliced_sentence)

check = company.startswith('Coding')
print(check)

check2 = company.endswith('Coding')
print(check2)

w1 = '30DaysOfPython'
w2 = 'thirty_days_of_python'

check3 = w1.isidentifier()
check4 = w2.isidentifier()

print(check3)
print(check4)

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_libraries = '#'.join(libraries)
print(join_libraries)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print(f"the area of a circle with radius 10 is: {str(area)} meters square.")

a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")