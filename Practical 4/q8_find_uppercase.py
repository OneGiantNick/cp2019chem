def find_num_uppercase(x):
    count = 0
    for i in x:
        if i.isupper():
            count = count + 1
    print(count)


string = 'Good MorninG!'
find_num_uppercase(string)
