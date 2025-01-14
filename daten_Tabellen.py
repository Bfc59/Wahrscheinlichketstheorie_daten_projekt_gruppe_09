##Programm um Box-Whisker- unde Scatterplot für gew Datei macht
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plots(filename,xlable,ylable,title,box=False,scatter=False):
    #einlesen
    df = pd.read_csv(filename,sep = ';')

    if box == True:
    # Boxplot für den DataFrame erstellen
        df.boxplot(column=[ylable])

    #Titel und Achsenbeschriftungen
        plt.title('Boxplot aus '+title+'.csv')
        plt.ylabel(ylable)
        plt.xticks([])

    # Diagramm anzeigen
        plt.show()

    # Scatterplot erstellen
    df[xlable] = pd.to_datetime(df[xlable], format='%d.%m.%Y')

    if scatter:
        plt.figure(figsize=(10, 6))
        plt.scatter(df[xlable], df[ylable], color='blue', alpha=0.7, s=5)

        # Titel und Achsenbeschriftungen für den Scatterplot hinzufügen
        plt.title('Scatterplot aus ' + title + '.csv')
        plt.xlabel(xlable)
        plt.ylabel(ylable)

        # Achseneinteilung so einstellen, dass nur jedes Jahrzehnt angezeigt wird
        #locator = mdates.YearLocator(1)  # Locator für jedes Jahrzehnt
        #formatter = mdates.DateFormatter('%Y')  # Formatter für das Jahr

        #ax = plt.gca()
        #ax.xaxis.set_major_locator(locator)
        #ax.xaxis.set_major_formatter(formatter)

        # Optional: Automatische Drehung der Datumsbeschriftungen für bessere Lesbarkeit
        #plt.gcf().autofmt_xdate()

        # Diagramm anzeigen
        plt.show()
    return 0

plots('data-2.csv','DATE','Percent change from a year ago','data-1',False,True)