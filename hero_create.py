def hero_create():
    print("Chose your hero, handsome(happiness level = 70, convincing power = 7) inteligent(happiness level = 30, convincing power = 10): ")
    hero_choice = input('\n To chose handsome type h, inteligent type i: ')
    while True:
        if hero_choice == "h":
            happiness_level = 70
            convincing_power = 7
            break
        elif hero_choice == "i":
            happiness_level = 30
            convincing_power = 10
            break
        else:
            hero_choice = input("Invalid choice(h or i): ")
    return happiness_level, convincing_power
