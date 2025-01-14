import pandas as pd
import statistics
import matplotlib.pyplot as plt

def descriptive_values(filename,column_name,val=False,file=False,outputname=None):
                     #(Dateiname,gew.Spalte,sortieren.j/n,dateiErstellen?,Name der erstellten Datei(falls ja))
    df = pd.read_csv(filename,sep = ';')

    if val == True:    #man kann entscheiden ob die Werte sortiert oder unsortiert bearbeitet werden
        df = df.sort_values(by=column_name)

    #Mittelwert
    mean = df[column_name].mean()

    #Median
    median = df[column_name].median()

    #Modus
    mode = df[column_name].mode()

    #Spannweite
    range = df[column_name].max() - df[column_name].min()

    # Stichprobenvarianz berechnen
    sample_variance = df[column_name].var(ddof=1)

    #Variationskoeffizient
    variation_coefficient = df[column_name].std(ddof=1) / df[column_name].mean()

    # Mittlere Abweichung vom Median
    mad_from_median = (df[column_name] - df[column_name].median()).abs().mean()

    #Datei mit Werten ausgeben
    if file == True:
        df.to_csv(outputname)

    if val == True:
        print("Werte für sortierte Liste:\n")
    else:
        print("Werte für unsortierte Liste:\n")

    values = ["mean:",mean,"median:",median,"mode:",mode,"range:",range,"sample_variance:",
              sample_variance,"variation_coefficient:",variation_coefficient,
              "mad_from_median:",mad_from_median]
    return values
############

result = descriptive_values('data-1.csv','Percent change from a year ago',False)
for i in result:
    print(i)

result_sorted = descriptive_values('data-1.csv','Percent change from a year ago',True)
for i in result_sorted:
    print(i)

#x_werte = df1['DATE']  # Ersetze 'Spalte1' durch den tatsächlichen Spaltennamen
#y_werte = df1['Percent change from a year ago']

#plt.scatter(x_werte, y_werte, color='red')
#plt.xlabel('X-Achse (Spalte1)')
#plt.ylabel('Y-Achse (Spalte2)')
#plt.title('Punktdiagramm aus CSV-Werten')
#plt.show()

#df.to_csv('urliste_daten.csv',index=False)
#df_sorted_percent.to_csv('sorted_data_percent.csv', index=False)