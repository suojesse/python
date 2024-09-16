import mysql.connector


def lentokentan_tiedot(icao_koodi, yhteys):
    sql = "SELECT name, municipality FROM airport WHERE gps_code = %s"

    try:
        kursori = yhteys.cursor()
        kursori.execute(sql, (icao_koodi,))
        tulos = kursori.fetchone()

        if tulos:
            lentokentan_nimi, kunta = tulos
            print(f"Lentokentän nimi: {lentokentan_nimi}, Kunta: {kunta}")

    finally:
        kursori.close()


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='jessecs',
    password='mariadb',
    autocommit=True
)


if __name__ == "__main__":
    icao_koodi = input("Anna lentoaseman ICAO-koodi: ")

    lentokentan_tiedot(icao_koodi, yhteys)
    yhteys.close()

