people = ['Jonas','Julio','Mike','Mez']
ages = [25,30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England','Bangladesh']
for person, age, natiolity in zip(people, ages, nationalities):
    print(person, age, natiolity)
