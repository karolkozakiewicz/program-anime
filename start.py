import pandas as pd
filename = 'lista_anime.csv'
columns = ['tytul', 'sezony', 'odcinki', 'gatunek', 'rokpremiery']
try:
    f = open(filename,'x')
    f.write("tytul,sezony,odcinki,gatunek,rokpremiery")
    f.close()
except: 
    FileExistsError
class Anime:

    def __init__(self, filename):
        self.filename = filename

    #print(show_all())
    def show_all(self):
        df = pd.read_csv(filename, index_col=0)
        print(df)

    # remove_anime(input())
    def remove_anime(self, tytul='none'):
        df = pd.read_csv(filename, index_col=0)
        try:
            df.drop(tytul, axis=0, inplace=True)
            df.to_csv(filename)
            print("Usunięto.")
        except:
            ValueError
            print("Nie znaleziono takiego anime")

    #add_anime() #5 args. | str, int, int, str, int
    def add_anime(self, tytul='none', sezony=0, odcinki=0, gatunek='none', rokpremiery=0):
        data = {'tytul': tytul, 'sezony': sezony, 'odcinki': odcinki, 'gatunek': gatunek, 'rokpremiery': rokpremiery}
        df = pd.read_csv(filename)
        df = df.append(data, ignore_index=True)
        df.to_csv(filename, index=False)

    #edit_anime() #3 args. | str, str, str/int
    def edit_anime(self, tytul='none', kolumna='tytul', nowa_wartosc='none'):
        df = pd.read_csv(filename)
        tytul = tytul.lower()
        df['tytul'] = df['tytul'].str.lower()
        indeks = df.loc[df['tytul'] == tytul].index.values.astype(int)[0]
        try:
            df.at[indeks,kolumna] = nowa_wartosc
            df.to_csv(filename,index=False)
            print("Zmieniono")
        except:
            ValueError
            KeyError
            print("Błędne wartości")
    #search_anime() #1 arg. | str
    def search_anime(self, tytul='none'):
        df = pd.read_csv(filename)
        tytul = tytul.lower()
        df['tytul'] = df['tytul'].str.lower()
        anime = df.loc[df['tytul'] == tytul]
        print(anime)

    def if_anime_in_file(self, tytul='none'):
        df = pd.read_csv(filename)
        tytul = tytul.lower()
        df['tytul'] = df['tytul'].str.lower()
        for x in df['tytul']:
            if tytul == x:
                return True
            else:
                continue

anime = Anime('lista_anime.csv')

while True:

    print("\n1. Pokaż wszystkie anime\n2. Dodaj anime\n3. Usun anime\n4. Edytuj anime\n5. Szukaj anime\n6. Exit")
    a = input()
    if a == '1':
        anime.show_all()
    elif a == '2':
        tytul = input("Podaj tytuł: ")
        if anime.if_anime_in_file(tytul):
            print("Anime istnieje")
        else:
            sezony = input("Podaj liczbę sezonów: ")
            odcinki = input("Podaj liczbę odcinków: ")
            gatunek = input("Podaj gatunek: ")
            rokpremiery = input("Podaj rok premiery: ")
            anime.add_anime(tytul,sezony,odcinki,gatunek,rokpremiery)
    elif a == '3':
        tytul = input("Podaj tytuł anime, które chcesz usunąć z listy: ")
        anime.remove_anime(tytul)
    elif a == '4':
        tytul = input("Podaj tytuł anime w którym chcesz coś zmienić: ")
        kolumna = input("W której kolumnie chcesz coś zmienić? (tytul, sezony, odcinki, gatunek, rokpremiery): ")
        nowa_wartosc = input("Podaj nową wartość: ")
        anime.edit_anime(tytul, kolumna, nowa_wartosc)
    elif a == '5':
        tytul = input("Podaj tytuł anime którego szukasz: ")
        anime.search_anime(tytul)
    elif a == '6':
        print("Do widzenia")
        break