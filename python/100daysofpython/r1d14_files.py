#!/usr/bin/env python3

import json

def run_files():
    ''''''
    print('\nfiles')
    filename = 'r1d14.txt'
    print('\nwrite', filename)
    with open(filename, 'w') as file:
        file.write('hello python')
        file.write('\n')
        file.write('bye python')
        file.write('\n')
    print('\nread', filename)
    content = ''
    with open(filename, 'r') as file:
        content = file.read()
    print(1, 'content')
    print(content)
    print('\nread lines', filename)
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line)
    print(2, 'lines')
    print(lines)

def run_csv():
    my_csv = 'r1d14_iris.csv'
    print('\nread csv', my_csv)
    iris = []
    with open(my_csv) as csv:
        for line in csv:
            line = line.split(',')
            user = {
                'sepal_length': line[0],
                'sepal_width': line[1],
                'petal_length': line[2],
                'petal_width': line[3],
                'species': line[4]
            }
            iris.append(user)
    print(1, 'iris', iris)
    user_file = 'r1d14_users.csv'
    print('\nwrite csv', user_file)
    users = [{'id': 1, 'email': 'mark@exmaple.com', 'name': 'Mark'}, {'id': 2, 'email': 'jane@example.com', 'name': 'Jane'}]
    print(2, 'users', users)
    with open(user_file, 'w') as file:
        file.write('id,email,name\n')
        for user in users:
            line = f"{user['id']},{user['email']},{user['name']}\n"
            file.write(line)

def run_json():
    ''''''
    filename = 'r1d14_users.json'
    print('\nread json', filename)
    users = []
    with open(filename, 'r') as file:
        json_content = json.load(file)
        users = json_content['users']
        print(1, 'json', json_content)
        print(2, 'users', users)
        print(3, 'type(users[0])', type(users[0]))
    filename = 'r1d14_users_final.json'
    print('\nwrite json', filename)
    for user in users:
        user['country'] = 'US'
    print(1, 'users', users)
    with open(filename, 'w') as file:
        json.dump({'users': users}, file)

if __name__ == '__main__':
    run_files()
    run_csv()
    run_json()

'''
output:

files

write r1d14.txt

read r1d14.txt
1 content
hello python
bye python


read lines r1d14.txt
2 lines
['hello python\n', 'bye python\n']

read csv r1d14_iris.csv
1 iris [{'sepal_length': 'sepal_length', 'sepal_width': 'sepal_width', 'petal_length': 'petal_length', 'petal_width': 'petal_width', 'species': 'species\n'}, {'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'setosa\n'}, {'sepal_length': '4.9', 'sepal_width': '3.0', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'setosa\n'}, {'sepal_length': '7.0', 'sepal_width': '3.2', 'petal_length': '4.7', 'petal_width': '1.4', 'species': 'versicolor\n'}, {'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'versicolor\n'}, {'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '6.0', 'petal_width': '2.5', 'species': 'virginica\n'}, {'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.9', 'species': 'virginica'}]

write csv r1d14_users.csv
2 users [{'id': 1, 'email': 'mark@exmaple.com', 'name': 'Mark'}, {'id': 2, 'email': 'jane@example.com', 'name': 'Jane'}]

read json r1d14_users.json
1 json {'users': [{'id': 1, 'email': 'mark@exmaple.com', 'name': 'Mark'}, {'id': 2, 'email': 'jane@example.com', 'name': 'Jane'}]}
2 users [{'id': 1, 'email': 'mark@exmaple.com', 'name': 'Mark'}, {'id': 2, 'email': 'jane@example.com', 'name': 'Jane'}]
3 type(users[0]) <class 'dict'>

write json r1d14_users_final.json
1 users [{'id': 1, 'email': 'mark@exmaple.com', 'name': 'Mark', 'country': 'US'}, {'id': 2, 'email': 'jane@example.com', 'name': 'Jane', 'country': 'US'}]
'''