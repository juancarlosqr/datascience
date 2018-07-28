import json

def get_json(data):
    return json.dumps(data)

def write_json(data):
    f = open('data.json', 'w')
    json.dump(data, f)
    f.close()

def read_json():
    f = open('data.json', 'r')
    data = json.load(f)
    f.close()
    return data

if __name__ == '__main__':
    data = ['earth', 'mars', 'mercury', 'venus']
    json_data = get_json(data)
    print(json_data)
    write_json(json_data)
    print(read_json())
