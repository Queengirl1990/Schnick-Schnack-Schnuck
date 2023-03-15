import random

print("Willkommen bei Schere, Stein, Papier! Lass uns zusammen Spielen.")

while True:
    print("Wähle deine Waffe:")
    print("1. Stein")
    print("2. Papier")
    print("3. Schere")

    player = input("Deine Wahl (1-3): ").strip()

    if not player.isdigit():
        print("Bitte eine Zahl eingeben!\n")
        continue

    player = int(player)

    if player not in range(1, 4):
        print("Ups, da ist ein Fehler aufgetreten.\n")
        continue

    weapons = {1: "Stein", 2: "Papier", 3: "Schere"}

    computer = random.randint(1, 3)

    print(f"Du hast {weapons[player]} gewählt.")
    print(f"Der Computer hat {weapons[computer]} gewählt.\n")

    if player == computer:
        print("Unentschieden, wir dachten an dasselbe!")
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("You win! Die Runde geht an dich.")
    else:
        print("You lose. Viel Glück beim nächsten mal.")

    print("")

    play_again = input("Möchtest du noch einmal spielen (j/n)? ").lower()
    if play_again != "j":
        break

print("\nDanke fürs Spielen!\n")
input("Zum Beenden beliebige Taste drücken.")