import textworks as text
import csvwriter
cats = ['masjha', 'dasha', 'sasha', 'lika' ]




text.sort_and_print_list(names=cats)
text.make_pizza('mushrooms', 'green peppers', 'extra cheese', 'humph')

filename = 'conf/main.cfg'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)



filename = 'output/setup3.txt'

with open(filename, 'w') as file_object:
    file_object.write(input("type: ")+ '\n')
    file_object.write(input("type: "))

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

db = csvwriter.get_dbconn('data/FPMS.mdb', 'fdmsamho')

