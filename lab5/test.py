"""test av uppslagsverk"""

tel = {'jack': 222, 'sape': 333}

print(tel['jack'])

tel2 = {1: 555, 2: 666}

print(tel2[1])

i = 2

tel[f'student {i}'] = 777

for k, v in tel.items():
    print(k, v)