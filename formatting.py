name = 'yaw'
age = 42

print('hello ' + name + ', you are ' + str(age) + ' years old.')

print('hello %s you are %s years old' % (name,age))

print('hello {0}, you are {1} years old'.format(name,age))

print(f'hello {name}, you are {age} yeras old!!! ')

print(f'hello {name}, in ten years, you will be {age + 10} yeras old!!! ') # <-Here we have enbeded a statement/expression

# This is the most ledgable and visible code- It is the best out of 5 format examples
message = (
    f'hello {name},'
    f'you are {age} years old'
    f'In ten yers you will be {age + 10}years old'
)

print(message)
