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

