with open("goats.txt", "r", encoding="utf-8") as file_in:
    data_in = list(map(lambda x: str(x).rstrip(),file_in.readlines()))
    data_colours = [i for i in data_in[1:data_in.index("GOATS")]]
    data_goats = [i for i in data_in[data_in.index("GOATS") + 1:]]
    data_len_goats = {}
    data_out_len = len(data_goats)
    for colour in data_colours:
        data_len_goats[colour] = data_goats.count(colour)
    data_out = [goat for goat in data_len_goats.keys() if data_len_goats[goat] * 100 / data_out_len > 7]

with open("answer.txt", "w", encoding="utf-8") as file_out:
    file_out.write("\n".join(data_out))