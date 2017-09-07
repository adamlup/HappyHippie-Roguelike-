def write_to_file(name, time):
    with open("hall_of_fame.txt", "a", newline="", encoding='utf-8') as f:
        f.write('\nPlayer name: ' + str(name) + ',')
        f.write(' Time = ' + str(time) + ' seconds')
