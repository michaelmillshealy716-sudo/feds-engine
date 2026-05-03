import robin_stocks.robinhood as rs
import os

def initialize_dutchman():
    """
    SUDO: Log into the Dutch bridge.
    Requires RH_USERNAME and RH_PASSWORD in .env.
    """
    user = os.getenv("RH_USERNAME")
    password = os.getenv("RH_PASSWORD")
    
    rs.login(username=user, password=password, expiresIn=86400)
    print("🦅 SOSA: Dutchman Bridge Active. Executioner is ready.")

def execute_scout_order(ticker, price, quantity):
    """
    The 'Kill Switch' executioner.
    Fires the limit buy once the Pendulum hits the mark.
    """
    print(f"💰 DUTCHMAN: Executing Limit Buy for {ticker} @ ${price}")
    
    # We cancel existing orders first to clear the floorboards
    rs.orders.cancel_all_stock_orders(ticker)
    
    # Place the new order with the Scout Capital
    order = rs.orders.order_buy_limit(ticker, quantity, price)
    return order

