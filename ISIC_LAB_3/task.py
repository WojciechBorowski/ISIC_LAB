import sqlite3

conn = sqlite3.connect('AMW.db')
cursor = conn.cursor()


cursor.execute("CREATE TABLE uczelnia (id_uczelni INT NOT NULL PRIMARY KEY,nazwa_uczelni VARCHAR(100) NOT NULL,lokalizacja VARCHAR(100) NOT NULL,rok_zalozenia INT NOT NULL,typ_uczelni VARCHAR(50) NOT NULL,adres VARCHAR(255) NOT NULL);")
cursor.execute("CREATE TABLE wydzial (id_wydzialu INT NOT NULL PRIMARY KEY,nazwa_wydzialu VARCHAR(100) NOT NULL,id_uczelni INT NOT NULL,dziekan VARCHAR(100) NOT NULL,adres VARCHAR(255) NOT NULL,FOREIGN KEY (id_uczelni) REFERENCES uczelnia(id_uczelni));")
cursor.execute("CREATE TABLE grupa_studencka (id_grupy INT NOT NULL PRIMARY KEY,nazwa_grupy VARCHAR(100) NOT NULL,id_wydzialu INT NOT NULL,rok_rozpoczecia INT NOT NULL,kierunek_studiow VARCHAR(100) NOT NULL,FOREIGN KEY (id_wydzialu) REFERENCES wydzial(id_wydzialu));")
cursor.execute("CREATE TABLE wykladowca (id_wykladowcy INT NOT NULL PRIMARY KEY,imie VARCHAR(50) NOT NULL,nazwisko VARCHAR(50) NOT NULL,stopien_naukowy VARCHAR(50) NOT NULL,specjalizacja VARCHAR(100) NOT NULL,id_wydzialu INT NOT NULL,FOREIGN KEY (id_wydzialu) REFERENCES wydzial(id_wydzialu));")
cursor.execute("CREATE TABLE przedmiot (id_przedmiotu INT NOT NULL PRIMARY KEY,nazwa_przedmiotu VARCHAR(100) NOT NULL,id_wykladowcy INT NOT NULL,id_wydzialu INT NOT NULL,semestr INT NOT NULL,liczba_godzin INT NOT NULL,FOREIGN KEY (id_wykladowcy) REFERENCES wykladowca(id_wykladowcy),FOREIGN KEY (id_wydzialu) REFERENCES wydzial(id_wydzialu));")
cursor.execute("CREATE TABLE student (id_studenta INT NOT NULL PRIMARY KEY,imie VARCHAR(50) NOT NULL,nazwisko VARCHAR(50) NOT NULL,data_urodzenia DATE NOT NULL,id_grupy INT NOT NULL,FOREIGN KEY (id_grupy) REFERENCES grupa_studencka(id_grupy));")
cursor.execute("CREATE TABLE ocena (id_oceny INT NOT NULL PRIMARY KEY,id_studenta INT NOT NULL,id_przedmiotu INT NOT NULL,ocena DECIMAL(3,2) NOT NULL,data_wystawienia DATE NOT NULL,FOREIGN KEY (id_studenta) REFERENCES student(id_studenta),FOREIGN KEY (id_przedmiotu) REFERENCES przedmiot(id_przedmiotu));")

cursor.execute("INSERT INTO uczelnia (id_uczelni, nazwa_uczelni, lokalizacja, rok_zalozenia, typ_uczelni, adres)VALUES (1, 'AMW', 'Gdynia', 1922, 'publiczna', 'ul.Inżyniera Jana Śmidowicza 69');")
cursor.execute("INSERT INTO wydzial (id_wydzialu, nazwa_wydzialu, id_uczelni, dziekan, adres)VALUES (1, 'WME', 1, 'Prof. Jan Kowalski', 'ul.Inżyniera Jana Śmidowicza 69'),(2, 'Wydział Informatyki', 1, 'Prof. Anna Nowak', 'ul.Inżyniera Jana Śmidowicza 69');")
cursor.execute("INSERT INTO grupa_studencka (id_grupy, nazwa_grupy, id_wydzialu, rok_rozpoczecia, kierunek_studiow)VALUES (1, '215IC', 2, 2019, 'Informatyka'),(2, '222MC', 1, 2021, 'Mechatronika');")
cursor.execute("INSERT INTO wykladowca (id_wykladowcy, imie, nazwisko, stopien_naukowy, specjalizacja, id_wydzialu)VALUES (1, 'Adam', 'Nowak', 'dr hab.', 'Bazy danych', 2),(2, 'Maria', 'Kowalska', 'prof.', 'Algorytmy', 1),(3, 'Piotr', 'Lewandowski', 'dr', 'Programowanie', 2),(4, 'Alicja', 'Zawadzka', 'dr hab.', 'Analiza matematyczna', 1),(5, 'Tomasz', 'Wójcik', 'prof.', 'Sieci komputerowe', 2);")
cursor.execute("INSERT INTO przedmiot (id_przedmiotu, nazwa_przedmiotu, id_wykladowcy, id_wydzialu, semestr, liczba_godzin)VALUES (1, 'Bazy danych', 1, 2, 3, 60),(2, 'Analiza matematyczna', 4, 1, 2, 90),(3, 'Sieci komputerowe', 5, 2, 4, 45),(4, 'Algorytmy', 2, 1, 3, 75),(5, 'Programowanie w C++', 3, 2, 2, 60);")
cursor.execute("INSERT INTO student (id_studenta, imie, nazwisko, data_urodzenia, id_grupy)VALUES (1, 'Jan', 'Kowalski', '2000-05-15', 1),(2, 'Anna', 'Nowak', '2001-02-20', 1),(3, 'Piotr', 'Lewandowski', '2000-11-10', 1),(4, 'Alicja', 'Zawadzka', '2001-09-25', 2),(5, 'Tomasz', 'Wójcik', '2000-08-30', 2),(6, 'Katarzyna', 'Kowalczyk', '2000-04-03', 2);")
cursor.execute("INSERT INTO ocena (id_oceny, id_studenta, id_przedmiotu, ocena, data_wystawienia)VALUES (1, 1, 1, 4.5, '2023-06-12'),(2, 2, 2, 5.0, '2023-06-15'),(3, 3, 4, 4.0, '2023-06-20'),(4, 4, 3, 4.5, '2023-06-10'),(5, 5, 5, 4.0, '2023-06-05'),(6, 6, 1, 3.5, '2023-06-18');")


cursor.execute("SELECT * FROM student")
output = cursor.fetchall()
print("Wszyscy studenci:")
for o in output:
    print(o)

cursor.execute("SELECT * FROM student WHERE id_grupy = 1")
output = cursor.fetchall()
print("\nStudenci z grupy 1:")
for o in output:
    print(o)


cursor.execute("SELECT s.* FROM student s JOIN ocena o ON s.id_studenta = o.id_studenta WHERE o.ocena >= 4")
output = cursor.fetchall()
print("\nStudenci ktorzy z jednego przedmiotu otrzymali ocene wyzsza badz rowna 4:")
for o in output:
    print(o)


cursor.execute("SELECT w.*, p.nazwa_przedmiotu FROM wykladowca w JOIN przedmiot p ON w.id_wykladowcy = p.id_wykladowcy")
output = cursor.fetchall()
print("\nWykladowcy i ich przedmioty")
for o in output:
    print(o)


cursor.execute("SELECT w.*, g.* FROM wydzial w JOIN grupa_studencka g ON w.id_wydzialu = g.id_wydzialu")
output = cursor.fetchall()
print("\nWydzial i jego grupy")
for o in output:
    print(o)

cursor.execute("SELECT s.imie, s.nazwisko, AVG(o.ocena) AS srednia_ocen FROM student s JOIN ocena o ON s.id_studenta = o.id_studenta GROUP BY s.id_studenta")
output = cursor.fetchall()
print("\nStudenci wraz z ich srednia ocen")
for o in output:
    print(o)

conn.commit()
conn.close()
