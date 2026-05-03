from fase_master import STOCKS

def get_sosa_knock_list():
    """
    SOSA AUDIT: The 'Hit List' for the FEDS Engine.
    Dynamically imports the asset load from FASE Master
    and translates them into Robinhood execution profiles.
    """
    knock_list = []
    
    # We loop through whatever tickers FASE Master gives us
    for symbol in STOCKS:
        target_profile = {
            "ticker": symbol,
            "reality_floor": 0.0,  # Failsafe default.
            "hedge_ceiling": None,
            "description": "FASE Master Dynamic Import"
        }
        knock_list.append(target_profile)
        
    return knock_list

