
def get_offer_for_class(f_class):
    # Offer code for A-E
    if 65 <= ord(f_class) <= 69:
        return "OFFER_20"
    # Offer code for F-K
    if 70 <= ord(f_class) <= 75:
        return "OFFER_30"
    # Offer code for L-R
    if 76 <= ord(f_class) <= 82:
        return "OFFER_25"
    return ""
