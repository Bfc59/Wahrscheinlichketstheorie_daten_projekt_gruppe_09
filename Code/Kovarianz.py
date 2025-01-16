###Berechnet hier Kovarianz zwischen Prozentwerten und Daten

import pandas as pd

data = pd.read_csv('bereinigte_datei.csv',sep=',')
df = pd.DataFrame(data)

# Datumswerte in datetime-Format konvertieren
#df['DATE'] = pd.to_datetime(df['DATE'], format='%d.%m.%Y')

# Datumswerte in numerische Werte (z. B. Tage seit 2000) umwandeln
#df['DATE_numeric'] = (df['DATE'] - pd.Timestamp("2000-07-01")).dt.days


# Kovarianzmatrix berechnen
cov_matrix = df.cov()
print("Kovarianz zwischen X und Y:", cov_matrix.loc['Jahr','Lebendgeborene (Anzahl) Insgesamt'])

correlation = df['Jahr'].corr(df['Lebendgeborene (Anzahl) Insgesamt'])

print("Korellationskoeffizient: ",correlation)

"""Das Programm berechnet die Kovarianz zwischen einer Tabellenspalte DATE_numeric, in der Daten im Format
TT.MM.JJJJ in Anzahl der Tage umgewandelt wird, die seit dem ersten vorhandenen Datum vergangen sind, damit
die Kovarianz der beiden vorhandenen Spalten mit numerischen Werten berechnet werden kann. Wenn man in Exel
die Kovarianz der einzelnen Spalte  'Percent change...' berechnen lässt, kommt ein ähnlicher Wert heraus, wie
wenn man es hier macht, mit dem Unterschie dass Exel die Daten nicht in numereische Werte umwandeln kann.
Dass es eigentlich wenig Sinn ergibt, einen ernsthaften Zusammenhang zwischen Jahreszahlen und prozentualen
Veränderungen von Immobilienpreisen zu suchen (mit Ausnahme von großen Ereignissen wie z.B. Wirtschaftskrisen
oder etwas dergleichen), ist hier zu beachten! """