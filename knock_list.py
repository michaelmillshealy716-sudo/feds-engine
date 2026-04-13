def get_sosa_knock_list():
    """
    SOSA AUDIT: The 'Hit List' for the FEDS Engine.
    Targets where sentiment (X) has diverged from Reality (R).
    """
    return [
        {
            "ticker": "WTI", 
            "reality_floor": 2.88, 
            "hedge_ceiling": 70.20,
            "description": "The Hormuz Blockade Play"
        },
        {
            "ticker": "ORCL", 
            "reality_floor": 142.50, 
            "hedge_ceiling": None,
            "description": "AI Utility Momentum"
        }
    ]
  
