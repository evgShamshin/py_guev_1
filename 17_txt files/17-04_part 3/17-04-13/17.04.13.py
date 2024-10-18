txt_count = int(input())
txt_name = [input() for _ in range(txt_count)]

for txt in txt_name:
    with open(txt) as txt_file, open("output.txt", "a") as output_file:
        output_file.write(txt_file.read())