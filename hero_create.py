def hero_create():
    name = input("Enter your name: ")
    hero_choice = input("Chose your hero, knight(hp = 100, attack = 20) tank(hp = 140, attack = 9: ")
    while True:
        if hero_choice == "knight":
            hp = 100
            attack = 20
            break
        elif hero_choice == "tank":
            hp = 140
            attack = 9
            break
        else:
            hero_choice = input("Invalid choice(knight or tank): ")
    return hp, attack
