import pandas as pd


class Anime:

    def __init__(self, filename):
        self.filename = filename
        self.check_file()

    def check_file(self):
        try:
            self.df = pd.read_csv(self.filename)  # czyta plik
        except FileNotFoundError:
            columns = dict(tytul=[], sezony=[], odcinki=[], gatunek=[], rokpremiery=[])  # lista kolumn
            nowy_plik = pd.DataFrame(columns)  # tworzy DataFrame z kolumnami
            nowy_plik.to_csv(self.filename, index=False)  # dodaje DataFrame do pliku
            print("Tworzę nowy plik")

    def show_all(self):
        print(self.df)  # printuje DataFrame z pliku

    def add_anime(self):
        tytul = input("Podaj tytuł: ")
        try:
            tytul = tytul.lower()
            for x in self.df['tytul']:
                if tytul == x.lower():
                    return True
                else:
                    print("Anime istnieje")
                    break
        except KeyError:
            pass
        sezony = input("Podaj liczbę sezonów: ")
        odcinki = input("Podaj liczbę odcinków: ")
        gatunek = input("Podaj gatunek: ")
        rokpremiery = input("Podaj rok premiery: ")
        data = {'tytul': tytul, 'sezony': sezony, 'odcinki': odcinki, 'gatunek': gatunek,
                'rokpremiery': rokpremiery}  # tworzy nowy row z danymi
        self.df.append(data, ignore_index=True)  # dodaje row do DataFrame
        self.df.to_csv(self.filename, index=False)  # dodaje DataFrame do pliku

    def search_anime(self):
        tytul = input("Podaj tytuł anime którego szukasz: ")
        tytul = tytul.lower()  # zamienia wpisany tytuł na małe litery
        try:
            self.df['tytul'] = self.df['tytul'].str.lower()  # zamienia każdy tytuł w kolumnie na małe litery
            print(self.df.loc[self.df['tytul'] == tytul])  # printuje informacje o tytule
        except KeyError:
            print("Nie znaleziono takiego anime")

    def remove_anime(self):
        try:
            tytul = input("Podaj tytuł anime, które chcesz usunąć z listy: ")
            self.df.drop(tytul, axis=0, inplace=True)
            self.df.to_csv(self.filename)
            print("Usunięto.")
        except KeyError:
            print("Nie znaleziono takiego anime")

    def edit_anime(self):
        tytul = input("Podaj tytuł anime w którym chcesz coś zmienić: ")
        kolumna = input("W której kolumnie chcesz coś zmienić? (tytul, sezony, odcinki, gatunek, rokpremiery): ")
        nowa_wartosc = input("Podaj nową wartość: ")
        tytul = tytul.lower()
        # self.df['tytul'].str.lower()
        indeks = self.df.loc[self.df['tytul'].str.lower() == tytul].index.values.astype(int)[0]
        try:
            self.df.at[indeks, kolumna] = nowa_wartosc
            self.df.to_csv(self.filename, index=False)
            print("Zmieniono")
        except ValueError:
            print("Błędne wartości")
        except KeyError:
            print("Błędne wartości")


anime = Anime('lista_anime.csv')
