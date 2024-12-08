from delayed_print import*
from class_armor_selection import*
resistance=0
durability=0
socialism=0
stealth=0
recovery=0
player_class=str

def calculate_stats():
    if player_class == "W":
        resistance += 50
        stealth -= 20
        socialism += 30
        recovery += 5
    else:
        if player_class == "S":
            resistance += 5
            stealth += 0
            socialism += 40
            recovery += 50
        else:
            if player_class == "P":
                resistance += 0
                stealth += 50
                socialism += 0
                recovery += 10

def call_stats():
    delay_print("\nHere are your statistics: Resistance = ")
    resist=str(resistance)
    delay_print(resist)
    delay_print(", Socialism = ")
    social=str(socialism)
    delay_print(social)
    delay_print(", Stealth = ")
    hunter=str(stealth)
    delay_print(hunter)
    delay_print(", Recovery = ")
    recov=str(recovery)
    delay_print(recov)
    delay_print(".")
