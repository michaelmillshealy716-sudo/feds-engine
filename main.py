import os
import time
from agents.edgar_allan_bro import telltale_heart_reality_check
from agents.dutchman import initialize_dutchman, execute_scout_order
from utils.knock_list import get_sosa_knock_list
import robin_stocks.robinhood as rs

def sosa_orchestrator():
    """
    SUDO: The Master Orchestrator. 
    Monitors the NOC List for the 2:00 PM Flush.
    """
    print("🦅 SOSA: Orchestrator is online. The 'Bad Company' is playing.")
    
    # 1. Boot up the Dutchman Bridge
    initialize_dutchman()
    
    # 2. Load the Hit List
    targets = get_sosa_knock_list()
    
    while True:
        for target in targets:
            ticker = target['ticker']
            floor = target['reality_floor']
            
            # 3. Audit Reality Anchor ($R$)
            reality_r = telltale_heart_reality_check(ticker)
            
            # 4. Check the Tape (Live Midday Price)
            price_data = rs.stocks.get_latest_price(ticker)
            current_price = float(price_data[0])
            
            print(f"🕵️ SOSA Audit: {ticker} | Price: ${current_price} | R: ${reality_r}")
            
            # 5. The Execution Logic: 2:00 PM Reversal
            if current_price <= floor:
                print(f"🎯 TARGET ACQUIRED: {ticker} hit the ${floor} floor.")
                
                # Using the $39 Scout Capital for the first strike
                # 13 shares of WTI @ ~$3 ≈ $39
                quantity = 13 if ticker == "WTI" else 1 
                
                execute_scout_order(ticker, floor, quantity)
                print("🔥 Strike Complete. Scout in the field.")
                return 
            
        print("⏳ Waiting for the Flush... The 'hunks' are still holding the line.")
        time.sleep(60) # 1-minute pulse check

if __name__ == "__main__":
    sosa_orchestrator()

