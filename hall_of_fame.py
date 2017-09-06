def write_to_file(name, score):
    with open("hall_of_fejm.txt", "a", newline="", encoding='utf-8') as f:
        f.write('\nPlayer name: ' + str(name) + ',')
        f.write(' Score = ' + str(score))
        