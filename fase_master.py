import robin_stocks.robinhood as r
import numpy as np
from datetime import datetime

# --- THE SPARTAN 300 PAYLOAD (TOTAL LIQUIDITY) ---
STOCKS = [
    "TSLA", "NVDA", "AMD", "AAPL", "MSFT", "AMZN", "META", "GOOGL", "NFLX", "PLTR",
    "COIN", "MARA", "RIOT", "BABA", "NIO", "PYPL", "AMC", "GPRO", "XOM", "CVX",
    "SQ", "ROKU", "SHOP", "U", "DKNG", "HOOD", "SOFI", "AFRM", "PINS", "SNAP",
    "INTC", "MU", "SNOW", "ADBE", "CRM", "TSM", "ORCL", "IBM", "UBER", "LYFT",
    "ABNB", "DASH", "SPOT", "ZM", "TWLO", "OKTA", "DDOG", "NET", "SE", "MSTR",
    "GME", "TLRY", "CGC", "ACB", "BB", "NOK", "F", "GM", "XPEV", "LI",
    "QS", "CHPT", "JPM", "BAC", "GS", "MS", "WFC", "C", "V", "MA",
    "AXP", "DIS", "SBUX", "NKE", "T", "VZ", "TMUS", "CMCSA", "WMT", "TGT",
    "COST", "HD", "LOW", "BA", "LMT", "RTX", "NOC", "GD", "GE", "MMM",
    "CAT", "HON", "DE", "UPS", "FDX", "FCX", "AA", "NEM", "GOLD", "SLV",
    "GLD", "TLT", "SPY", "QQQ", "IWM", "DIA", "XLF", "XLE", "XLK", "XLI",
    "XLV", "XLP", "XLY", "XLB", "XLU", "XLRE", "SMH", "ARKK", "TQQQ", "SQQQ",
    "SOXL", "SOXS", "LABU", "LABD", "UVXY", "VIXY", "BITO", "GBTC", "EEM", "FXI",
    "GDX", "GDXJ", "UNH", "PFE", "JNJ", "MRK", "ABBV", "LLY", "AMGN", "VRTX",
    "BIIB", "GILD", "MRNA", "BNTX", "CVS", "WBA", "KR", "PG", "CL", "KMB",
    "PEP", "KO", "MDLZ", "MO", "PM", "BUD", "STZ", "KDP", "MNST", "CELH",
    "ELF", "ULTA", "EL", "LULU", "ADI", "AVGO", "KLAC", "LRCX", "AMAT", "TER",
    "TXN", "NXPI", "ON", "MCHP", "MPWR", "LSCC", "ALGN", "IDXX", "ISRG", "SYK",
    "BSX", "EW", "ZBH", "DXCM", "ABT", "MDT", "DHR", "TMO", "A", "ILMN",
    "WAT", "MTD", "KEYS", "TEL", "APH", "MSI", "CSCO", "PANW", "FTNT", "CRWD",
    "ZS", "MDB", "TEAM", "WDAY", "NOW", "DOCU", "ETSY", "EBAY", "DFS", "COF",
    "SYF", "ALL", "PGR", "MET", "PRU", "AFL", "TRV", "CB", "HIG", "L",
    "AIZ", "UNM", "RJF", "SCHW", "IBKR", "AMTD", "LPLA", "BLK", "STT", "NTRS",
    "BEN", "IVZ", "AMG", "AMP", "TROW", "BX", "KKR", "APO", "CG", "OWL",
    "STEP", "BAM", "BN", "GPN", "FIS", "FISV", "JKHY", "PAYX", "ADP", "INTU",
    "ROP", "TYL", "CDW", "LDOS", "BAH", "BR", "IT", "GART", "EXAS", "GH",
    "PACB", "TWST", "DNA", "BEAM", "NTLA", "EDIT", "CRSP", "BE", "PLUG", "BLDP",
    "FCEL", "RUN", "ENPH", "SEDG", "FSLR", "CSIQ", "JKS", "DQ", "TAN", "ICLN",
    "PBW", "QCLN", "LIT", "PAVE", "XME", "KRE", "KBE", "XHB", "ITB", "VNQ",
    "VNQI", "SCHH", "REET", "EWJ", "EWG", "EWU", "EWC", "EWA", "EWZ", "EWY", "EWT",
    "SHAK", "BYND", "PENN", "WYNN", "LVS", "MGM", "CCL", "RCL", "NCLH", "DAL",
    "UAL", "AAL", "LUV", "SAVE", "JBLU", "MRVL", "SWKS", "QRVO", "AVGO", "MP",
    "LTHM", "ALB", "SQM", "VALE", "RIO", "BHP", "PBR", "E", "EQNR", "TTE",
    "SHEL", "BP", "OXY", "HES", "VLO", "MPC", "PSX", "APA", "DVN", "MRO", "ASML"
]

price_history = {t: [0.0] * 50 for t in STOCKS}

def rh_login():
    """V1.9: Secure Handshake"""
    username = "Michaelmillshealy716@gmail.com"
    password = "M3141592654h*!*$$"
    r.login(username, password, expiresIn=86400, store_session=True)

def get_cortex_price(ticker):
    """SOSA Cortex Bridge: Bypasses 404 via get_quotes"""
    try:
        data = r.stocks.get_quotes(ticker)
        if data and data[0]:
            return float(data[0]['last_trade_price'])
        return None
    except: return None

def veritas_bridge(ticker, price, history):
    """Veritas V2.2: 3rd-Order Taylor Series Expansion"""
    if len(history) < 4: 
        history.append(price)
        return False
    p = np.array(history[-4:])
    v = p[-1] - p[-2]
    a = (p[-1] - p[-2]) - (p[-2] - p[-3])
    j = ((p[-1] - p[-2]) - (p[-2] - p[-3])) - ((p[-2] - p[-3]) - (p[-3] - p[-4]))
    p_next = p[-1] + v + (0.5 * a) + (0.1667 * j)
    history.append(price)
    if len(history) > 50: history.pop(0)
    return p_next > p[-1] and v > 0

def execute_strike(ticker, price):
    """The $0.25 Aggressor Strike: CORRECTED FOR 2026 API"""
    print(f"\n\033[93m>>> CORTEX STRIKE: {ticker} @ ${price} <<<\033[0m")
    try:
        # CORRECTED ARGUMENT NAMES: positionEffect, price (limit), quantity
        order = r.orders.order_buy_option_limit(
            positionEffect='open', 
            creditOrDebit='debit',
            price=0.25, 
            symbol=ticker, 
            quantity=1,
            expirationDate='2026-05-08', 
            strike=None, 
            optionType='call', 
            timeInForce='gtc'
        )
        if 'id' in order:
            print(f"\033[92m[!] SUCCESS: Order {order['id']}\033[0m")
        else:
            print(f"\033[91m[X] REJECTED: {order.get('detail', 'Funds Issue')}\033[0m")
    except Exception as e:
        print(f"CRITICAL EXECUTION ERROR: {e}")

def monitor_and_close():
    """The Closer: 30% TP / 10% SL"""
    try:
        positions = r.options.get_open_option_positions()
        for pos in positions:
            symbol = pos['chain_symbol']
            entry = float(pos['average_price']) / 100
            m_data = r.options.get_option_market_data_by_id(pos['option_id'])
            current = float(m_data['last_trade_price'])
            pcnt = (current - entry) / entry
            if pcnt >= 0.30 or pcnt <= -0.10:
                print(f"\n\033[92m>>> CLOSING {symbol}: {pcnt*100:.1f}% Change <<<\033[0m")
                r.orders.order_sell_option_limit(
                    positionEffect='close', 
                    creditOrDebit='credit', 
                    price=current, 
                    symbol=symbol, 
                    quantity=1, 
                    expirationDate=pos['pending_buy_expiration_date'], 
                    strike=pos['strike_price'], 
                    optionType='call'
                )
    except: pass

