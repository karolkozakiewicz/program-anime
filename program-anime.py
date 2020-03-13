import pandas as pd


class Anime:

    def __init__(self, filename):
        self.filename = filename
        self.check_file()  # sprawdza, czy plik istnieje. Jeśli nie, tworzy nowy.
        self.kolumny = ['tytul', 'sezony', 'odcinki', 'gatunek', 'rokpremiery']
        self.columns = dict(tytul=[], sezony=[], odcinki=[], gatunek=[], rokpremiery=[])  # lista kolumn

    def check_file(self):
        try:
            self.df = pd.read_csv(self.filename)  # czyta plik
        except FileNotFoundError:
            # columns = dict(tytul=[], sezony=[], odcinki=[], gatunek=[], rokpremiery=[])  # lista kolumn
            nowy_plik = pd.DataFrame(self.columns)  # tworzy DataFrame z kolumnami
            nowy_plik.to_csv(self.filename, index=False)  # dodaje DataFrame do pliku
            print("Tworzę nowy plik")

    def show_all(self):
        print(self.df)  # printuje DataFrame z pliku

    def if_anime_in_file(self, tytul):
        tytul = tytul.lower()
        for x in self.df['tytul']:
            if tytul == x.lower():
                return True
            else:
                continue

    def add_anime(self):
        tytul = input("Podaj tytuł: ")
        if self.if_anime_in_file(tytul):
            print("Anime istnieje")
        else:
            sezony = input("Podaj liczbę sezonów: ")
            odcinki = input("Podaj liczbę odcinków: ")
            gatunek = input("Podaj gatunek: ")
            rokpremiery = input("Podaj rok premiery: ")
            data = {'tytul': tytul, 'sezony': sezony, 'odcinki': odcinki, 'gatunek': gatunek,
                    'rokpremiery': rokpremiery}  # tworzy nowy row z danymi
            self.df = self.df.append(data, ignore_index=True)  # dodaje row do DataFrame
            self.df.to_csv(self.filename, index=False)  # dodaje DataFrame do pliku
            print("Dodano")

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
            self.df.drop(tytul, axis=0, inplace=True)  # usuwa tytuł wraz z pozostałymi danymi z DataFrame
            self.df.to_csv(self.filename)  # dodaje nowy DataFrame do pliku
            print("Usunięto.")
        except KeyError:
            print("Nie znaleziono takiego anime")

    def edit_anime(self):
        tytul = input("Podaj tytuł anime w którym chcesz coś zmienić: ")

        if self.if_anime_in_file(tytul):
            if tytul in self.kolumny:
                print("Nie możesz zmienić nazw kolumn")
            else:
                kolumna = input("W której kolumnie chcesz coś zmienić? (tytul, sezony, odcinki, gatunek, rokpremiery): ")
                if kolumna not in self.kolumny:
                    print("Zła kolumna")
                else:
                    nowa_wartosc = input("Podaj nową wartość: ")
                    tytul = tytul.lower()
                    # self.df['tytul'].str.lower()
                    indeks = self.df.loc[self.df['tytul'].str.lower() == tytul].index.values.astype(int)[0]
                    try:
                        self.df.at[indeks, kolumna] = nowa_wartosc
                        self.df.to_csv(self.filename, index=False)
                        print("Zmieniono")
                    except ValueError:  # do poprawy \/
                        print("Błędne wartości")
                    except KeyError:
                        print("Błędne wartości")  # do poprawy /\
        else:
            print("Tytuł nie znajduje się na liście")
# x

anime = Anime('lista_anime.csv')


while True:

    print("\n1. Pokaż wszystkie anime\n2. Dodaj anime\n3. Usun anime\n4. Edytuj anime\n5. Szukaj anime\n6. Exit")
    wybor = input()
    if wybor == '1':
        anime.show_all()
    elif wybor == '2':
        anime.add_anime()
    elif wybor == '3':
        anime.remove_anime()
    elif wybor == '4':
        anime.edit_anime()
    elif wybor == '5':
        anime.search_anime()
    elif wybor == '6':
        print("Do widzenia")
        break
