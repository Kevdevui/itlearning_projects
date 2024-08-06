import exchange_rates  # Assuming this module provides the necessary exchange rates

# Function to convert USD to EUR
def convert_usd_to_eur(amount):
    return amount * exchange_rates.USD_TO_EUR

# Function to convert USD to GBP
def convert_usd_to_gbp(amount):
    return amount * exchange_rates.USD_TO_GBP

# Function to convert USD to JPY
def convert_usd_to_jpy(amount):
    return amount * exchange_rates.USD_TO_JPY

# Function to convert USD to CAD
def convert_usd_to_cad(amount):
    return amount * exchange_rates.USD_TO_CAD

# Function to convert USD to AUD
def convert_usd_to_aud(amount):
    return amount * exchange_rates.USD_TO_AUD

# Function to convert USD to INR
def convert_usd_to_inr(amount):
    return amount * exchange_rates.USD_TO_INR

def main():
    usd_amount = 150  # Updated USD amount
    
    # Convert USD to various currencies
    eur_amount = convert_usd_to_eur(usd_amount)
    gbp_amount = convert_usd_to_gbp(usd_amount)
    jpy_amount = convert_usd_to_jpy(usd_amount)
    cad_amount = convert_usd_to_cad(usd_amount)
    aud_amount = convert_usd_to_aud(usd_amount)
    inr_amount = convert_usd_to_inr(usd_amount)
    
    # Print the results
    print(f"USD {usd_amount} is equal to:")
    print(f"- EUR {eur_amount:.2f}")  # Formatting to 2 decimal places
    print(f"- GBP {gbp_amount:.2f}")  # Formatting to 2 decimal places
    print(f"- JPY {jpy_amount:.2f}")  # Formatting to 2 decimal places
    print(f"- CAD {cad_amount:.2f}")  # Formatting to 2 decimal places
    print(f"- AUD {aud_amount:.2f}")  # Formatting to 2 decimal places
    print(f"- INR {inr_amount:.2f}")  # Formatting to 2 decimal places

if __name__ == "__main__":
    main()
