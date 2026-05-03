import os, sys, time, json
from datetime import datetime, timedelta

PERI = "\033[38;5;147m"
GOLD = "\033[38;5;220m"
print(f"{PERI}SOSA ORCHESTRATOR V1.8 | {datetime.now().strftime('%H:%M:%S')} | CORTEX SYNCED\033[0m")

HISTORY_FILE = "trade_history.json"

def load_bullets():
    if not os.path.exists(HISTORY_FILE): return []
    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
        five_days_ago = datetime.now() - timedelta(days=5)
        return [t for t in history if datetime.fromisoformat(t) > five_days_ago]
    except: return []

def save_bullet(timestamp):
    history = load_bullets()
    history.append(timestamp.isoformat())
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def sosa_orchestrator():
    print(f"{GOLD}SOSA: Initiating Cortex Handshake...{0}")
    try:
        from fase_master import (
            STOCKS, rh_login, execute_strike, 
            veritas_bridge, price_history, get_cortex_price
        )
        rh_login()
    except Exception as e:
        print(f"\033[91mCRITICAL ERROR: {e}\033[0m")
        return

    print(f"{PERI}SOSA: Handshake Verified. SPARTAN 300 ACTIVE.{0}")
    
    while True:
        spent = load_bullets()
        if len(spent) >= 3:
            sys.stdout.write(f"\r{GOLD}PDT GUARD: 3/3 Bullets Spent. Magazine Empty.{0}")
            sys.stdout.flush()
            time.sleep(60)
            continue

        for ticker in STOCKS:
            try:
                price = get_cortex_price(ticker)
                if not price: continue
                if veritas_bridge(ticker, price, price_history[ticker]):
                    execute_strike(ticker, price)
                    save_bullet(datetime.now())
                    if len(load_bullets()) >= 3: break
            except: continue
        time.sleep(60)

if __name__ == "__main__":
    try:
        sosa_orchestrator()
    except KeyboardInterrupt:
        print(f"\n\033[91mSOSA: Manual Override. Engine Halted.\033[0m")
        sys.exit()

