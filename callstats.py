from delayed_print import*
resistance=0
durability=0
socialism=0
stealth=0
recovery=0

def call_stats():
    from callstats import recovery
    from callstats import resistance
    from callstats import socialism
    from callstats import stealth
    from callstats import durability
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
