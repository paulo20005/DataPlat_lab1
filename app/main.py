import pandas as pd
import numpy as np
import os

# Här hämtar vi sökvägen till mappen där detta script ligger
current_dir = os.path.dirname(os.path.abspath(__file__))
# Här lägger vi ihop mappsökvägen med filnamnet så vi får hela sökvägen till CSV filen
csv_path = os.path.join(current_dir, 'lab 1 - csv.csv')

# Läser in CSV-filen. sep=';' betyder att kolumnerna separeras med semikolon
df = pd.read_csv(csv_path, sep=';', encoding='utf-8')

# Tar bort onödiga mellanslag från kolumnnamn
df.columns = df.columns.str.strip()
# Tar bort mellanslag från produktnamn
df['name'] = df['name'].str.strip()
# Tar bort mellanslag från valuta-kolumnen
df['currency'] = df['currency'].str.strip()

# Här konverterar vi priser till siffror
# replace('free', '0') byter ut texten "free" mot "0"
# errors='coerce' gör att allt som inte går att konvertera blir NaN (Not a Number)
df['price_clean'] = pd.to_numeric(df['price'].replace('free', '0'), errors='coerce')

# Här konverterar vi datum till rätt format
# errors='coerce' gör att ogiltiga datum blir NaN
df['date_clean'] = pd.to_datetime(df['created_at'], errors='coerce')

# Här flaggar vi olika problem
df['negativt_pris'] = df['price_clean'] < 0                    # Pris mindre än 0
df['fel_datum'] = df['date_clean'].isna()                      # Datum som är ogiltiga
df['saknar_id'] = df['id'].isna()                              # Produkter utan ID
df['saknar_namn'] = df['name'].isna()                          # Produkter utan namn

# Här markerar vi vilka rader som ska tas bort
df['ta_bort'] = df['negativt_pris'] | df['fel_datum'] | df['saknar_id'] | df['saknar_namn']

# Här behåller vi bara rader som INTE ska tas bort
bra_data = df[df['ta_bort'] == False].copy()

# Här räknar vi ut statistiken från den rena datan
snittpris = bra_data['price_clean'].mean()                     # Medelvärdet av alla priser
medianpris = bra_data['price_clean'].median()                  # Medianpriset
antal_produkter = len(bra_data)                                # Hur många produkter vi har kvar
antal_saknat_pris = bra_data['price_clean'].isna().sum()       # Hur många som saknar pris
