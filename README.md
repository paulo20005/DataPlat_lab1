# Redovisning
Ingest Storage Transform Access

Först läste jag in CSV filen med pd.read_csv. Datan sparades i en DataFrame. Sen rensade jag datan genom att ta bort mellanslag, göra om "free" till 0, konvertera priser till siffror och fixa datum. Till sist skapade jag en ny CSV fil med statistiken.

Extract Transform Load

Samma sak fast andra ord. Jag hämtade data från CSV filen, rensade den och sparade till en ny fil.

Teknologier

Jag använde pandas för att läsa, rensa och analysera datan