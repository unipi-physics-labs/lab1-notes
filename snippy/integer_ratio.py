x = 0.1
numerator, denominator = x.as_integer_ratio()
print(f'{x} = {numerator} / {denominator}')
print(f'Num. = {bin(numerator)}')
print(f'Den. = {bin(denominator)}')
