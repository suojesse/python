from flask import Flask, jsonify
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='jessecs',
    password='mariadb',
    autocommit=True
)

app = Flask(__name__)

def get_airport_info_by_icao(icao_code):
    sql = "SELECT gps_code AS ICAO, name AS Name, municipality AS Municipality FROM airport WHERE gps_code = %s LIMIT 1"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao_code,))
    result = kursori.fetchone()
    kursori.close()
    return result

@app.route('/kentta/<icao>', methods=['GET'])
def koodi(icao):
    result = get_airport_info_by_icao(icao.upper())
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)