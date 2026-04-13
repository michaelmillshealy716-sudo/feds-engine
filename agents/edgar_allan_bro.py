from edgar import Company, set_identity
import os

def telltale_heart_reality_check(ticker="WTI"):
    """
    SOSA AUDIT: Searches for the 'Reality Anchor' ($R$).
    """
    # VERITAS: Identity verification for the SEC (Michael Healy)
    set_identity(os.getenv("EDGAR_IDENTITY"))
    
    try:
        company = Company(ticker)
        # Pull the latest 10-K for structural floorboards
        filings = company.get_filings(form="10-K")
        latest_10k = filings[0].obj()
        
        # Architect's Logic: Parse Item 3 (Risk Factors) for the $70.20/Bbl hedge
        audit_text = str(latest_10k.section('Item 3'))
        
        if "70.20" in audit_text:
            print(f"🦅 SOSA: Reality Anchor Found. R = $70.20/Bbl.")
            return 70.20 
            
        return 0
        
    except Exception as e:
        print(f"⚠️ SOSA ALERT: Reality Audit Failed. Error: {e}")
        return None
      
