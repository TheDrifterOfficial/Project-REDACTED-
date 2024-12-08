from delayed_print import*
from callstats import*

def class_armor_selection():
    delay_print("\nAs part of you helping us, you will need some armour and weapons.")
    delay_print("\nPlease select your armour:")
    delay_print("\nIron Armour (+40 resistance, 7/10 durability) / Leather Armour (+30 resistance, 10/10) / Chainmail Armour (+60 resistance, 4/10 durability)")
    delay_print("\nI for Iron, L for Leather, C for Chainmail: ")
    a=str(input(""))
    player_class=str
    if a == "I" or a == "L" or a == "C":
        1+1
    else:
        delay_print("\nPlease select your armour:")
        delay_print("\nIron Armour (+50 resistance, 7/10 durability) / Leather Armour (+30 resistance, 10/10) / Chainmail Armour (+50 resistance, 4/10 durability)")
        delay_print("\nI for Iron, L for Leather, C for Chainmail: ")
        a=str(input(""))
        if a == "I" or a == "L" or a == "C":
            1+1
        else:
            delay_print("\nPlease select your armour:")
            delay_print("\nIron Armour (+50 resistance, 7/10 durability) / Leather Armour (+30 resistance, 10/10) / Chainmail Armour (+50 resistance, 4/10 durability)")
            delay_print("\nI for Iron, L for Leather, C for Chainmail: ")
            a=str(input(""))
            if a == "I" or a == "L" or a == "C":
                1+1
            else:
                delay_print("\nPlease select your armour:")
                delay_print("\nIron Armour (+50 resistance, 7/10 durability) / Leather Armour (+30 resistance, 10/10) / Chainmail Armour (+50 resistance, 4/10 durability)")
                delay_print("\nI for Iron, L for Leather, C for Chainmail: ")
                a=str(input(""))
                if a == "I" or a == "L" or a == "C":
                    1+1
                else:
                    delay_print("\nPlease select your armour:")
                    delay_print("\nIron Armour (+50 resistance, 7/10 durability) / Leather Armour (+30 resistance, 10/10) / Chainmail Armour (+50 resistance, 4/10 durability)")
                    delay_print("\nI for Iron, L for Leather, C for Chainmail: ")
                    a=str(input(""))
                    if a == "I" or a == "L" or a == "C":
                        delay_print("\nYou have pissed me off, so now I am just giving you armour")
                        a="A"
    if a == "I":
        resistance=40
        durability=7
    else:
        if a == "L":
            resistance=30
            durability=10
        else:
            if a == "C":
                resistance=60
                durability=4
            else:
                if a == "A":
                    resistance=10
                    durability=3
    delay_print("\nVery well, now it is time to pick your class.")
    delay_print("\nPlease select a class:")
    delay_print("\nWarlords: Specializes on combat, specifically close combat. Warlords can focus on one target, dealing great damage. +50 Resistance, +30 Socialism, -20 Stealth, +5 Recovery.")
    delay_print("\nScripters: Specializes in the arts of magic, casting different spells that grant benefits and punishments. Scripters are able to focus on multiple targets or one target. +5 Resistance, -40 Socialism, 0 Stealth, +50 Recovery.")
    delay_print("\nPythons: Specializes on stealth and maneuvering. Pythons are able to focus on multiple targets at once. 0 Resistance, 0 Socialism, +50 Stealth, +10 Recovery")
    delay_print("\nWarlords (W), Scripters (S), Pythons (P):")
    player_class=str(input(" "))
    if player_class == "W" or player_class =="S" or player_class == "P":
        1+1
    else:
        delay_print("\nPlease select a class:")
        delay_print("\nWarlords: Specializes on combat, specifically close combat. Warlords can focus on one target, dealing great damage. +50 Resistance, +30 Socialism, -20 Stealth, +5 Recovery.")
        delay_print("\nScripters: Specializes in the arts of magic, casting different spells that grant benefits and punishments. Scripters are able to focus on multiple targets or one target. +5 Resistance, -40 Socialism, 0 Stealth, +50 Recovery.")
        delay_print("\nPythons: Specializes on stealth and maneuvering. Pythons are able to focus on multiple targets at once. 0 Resistance, 0 Socialism, +50 Stealth, +10 Recovery")
        delay_print("\n Warlords (W), Scripters (S), Pythons (P)")
        player_class=str(input(" "))
        if player_class == "W" or player_class =="S" or player_class == "P":
            1+1
        else:
            delay_print("\nPlease select a class:")
            delay_print("\nWarlords: Specializes on combat, specifically close combat. Warlords can focus on one target, dealing great damage. +50 Resistance, +30 Socialism, -20 Stealth, +5 Recovery.")
            delay_print("\nScripters: Specializes in the arts of magic, casting different spells that grant benefits and punishments. Scripters are able to focus on multiple targets or one target. +5 Resistance, -40 Socialism, 0 Stealth, +50 Recovery.")
            delay_print("\nPythons: Specializes on stealth and maneuvering. Pythons are able to focus on multiple targets at once. 0 Resistance, 0 Socialism, +50 Stealth, +10 Recovery")
            delay_print("\n Warlords (W), Scripters (S), Pythons (P)")
            player_class=str(input(" "))
            if player_class == "W" or player_class =="S" or player_class == "P":
                1+1
            else:
                delay_print("\nPlease select a class:")
                delay_print("\nWarlords: Specializes on combat, specifically close combat. Warlords can focus on one target, dealing great damage. +50 Resistance, +30 Socialism, -20 Stealth, +5 Recovery.")
                delay_print("\nScripters: Specializes in the arts of magic, casting different spells that grant benefits and punishments. Scripters are able to focus on multiple targets or one target. +5 Resistance, -40 Socialism, 0 Stealth, +50 Recovery.")
                delay_print("\nPythons: Specializes on stealth and maneuvering. Pythons are able to focus on multiple targets at once. 0 Resistance, 0 Socialism, +50 Stealth, +10 Recovery")
                delay_print("\n Warlords (W), Scripters (S), Pythons (P)")
                player_class=str(input(" "))
                if player_class == "W" or player_class =="S" or player_class == "P":
                    1+1
                else:
                    delay_print("\nPlease select a class:")
                    delay_print("\nWarlords: Specializes on combat, specifically close combat. Warlords can focus on one target, dealing great damage. +50 Resistance, +30 Socialism, -20 Stealth, +5 Recovery.")
                    delay_print("\nScripters: Specializes in the arts of magic, casting different spells that grant benefits and punishments. Scripters are able to focus on multiple targets or one target. +5 Resistance, -40 Socialism, 0 Stealth, +50 Recovery.")
                    delay_print("\nPythons: Specializes on stealth and maneuvering. Pythons are able to focus on multiple targets at once. 0 Resistance, 0 Socialism, +50 Stealth, +10 Recovery")
                    delay_print("\n Warlords (W), Scripters (S), Pythons (P)")
                    player_class=str(input(" "))
                    if player_class == "W" or player_class =="S" or player_class == "P":
                        1+1
                    else:
                        delay_print("\nVery well, you leave me no choice. You are now a Joker.")
                        resistance=resistance-20
                        stealth=stealth-20
                        socialism=socialism-20
                        recovery=recovery-20