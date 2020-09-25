class Readfile():
    def __init__(self):
        0
    def read(self, link):
        with open(link) as file_object:
            for line in file_object:
                print(line.rstrip())

    def write(self, link, data):
        with open(link, 'w') as file_object:
            file_object.write(data)