import numpy as np
import time

def calculate_news_entropy(initial_impact, timestamp):
    """
    Michael Healy's '07 Calculus Model: e^-kt
    Targets a 30-minute window for the e^-2 threshold.
    """
    k = 0.066 # Decay constant for 30-min half-life
    t_minutes = (time.time() - timestamp) / 60
    
    decay = np.exp(-k * t_minutes)
    current_impact = initial_impact * decay
    
    # The Sosa Check: 13.5% threshold (e^-2)
    is_stale = decay <= 0.135
    return current_impact, is_stale
  
