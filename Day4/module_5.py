my_list = ["milk", "eggs", "bread", "butter", "cheese", "milo", "sardine"]

empty_list = []

print(len(my_list))

print(my_list[0] + " " + my_list[3] + " " + my_list[-1])

mixed_data_type = ['Umar', '15', '7.5', 'single', 'kano',]

IT_companies = ["Facebook", "Google", "Microsoft", "Apple","IBM", "Oracle","Twitter","Amazon", "#;"]
IT_companies.insert (4,'Android')
print(IT_companies)
print(len(IT_companies))
print(IT_companies[0] + " " + IT_companies[3] + " " + IT_companies[-1])
print(IT_companies[1].upper())


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']


full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'python')
full_stack.insert(full_stack.index('python') + 1, 'SQL')
print(full_stack)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = min(ages)
max_age = max(ages)

print("Sorted list:", ages)
print("Min age:", min_age)
print("Max age:", max_age)

ages.append(min_age)
ages.append(max_age)
print("List after adding min and max again:", ages)

n = len(ages)
if n % 2 == 1:
    median_age = ages[n // 2]
else:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2

print("Median age:", median_age)

average_age = sum(ages) / len(ages)
print("Average age:", average_age)

age_range = max_age - min_age
print("Range of ages:", age_range)

min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Difference between min and average:", min_diff)
print("Difference between max and average:", max_diff)

Countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = Countries_list[len(Countries_list) // 2]
print('Middle country is: ', middle_country)


divide = len(Countries_list) // 2

first_half = Countries_list[:divide + 1] if len(Countries_list) % 2 != 0 else Countries_list[:divide]
second_half = Countries_list[divide + 1:] if len(Countries_list) % 2 != 0 else Countries_list[divide:]

print("First half:", first_half)
print("Second half:", second_half)

###########################################

Empty_tuple = ()
brothers = ('Musa','Abubakar','Saleh','Mustapha')
sisters =('Khadija','Zainab','Fatima','Aisha')
siblings = brothers + sisters
print('Siblings:', siblings)

family_members = ('Hassan', 'Sadiya') + siblings
print('Family members:', family_members)

del siblings,family_members

fruits = ('mango','Guava','pineapple','watermelon','orange')
Vegetables = ('carrots','lettuces','onion','tomato')
animal_products = ('sardine','chicken','beef')

food_stuff = fruits + Vegetables + animal_products
food_stuff_list = list(food_stuff)
print(food_stuff_list)

sliced = fruits[2:3]
print(sliced)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('iceland' in nordic_countries)





