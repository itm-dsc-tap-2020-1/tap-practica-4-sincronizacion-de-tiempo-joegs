import datetime
from time import ctime
import ntplib
import os


def main():
    timeserver = "time.nist.gov"
    ntp_client = ntplib.NTPClient()

    t1 = datetime.datetime.now()
    response = ntp_client.request(timeserver)
    t2 = datetime.datetime.now()
    datetime_response = datetime.datetime.fromtimestamp(response.tx_time)
    time_string = datetime_response.strftime("%a %b %d %H:%M:%S %Y")
    offset = (t2 - t1) / 2
    final_time = datetime_response + offset

    print(f"Hora de inicio de la peticion: {t1}")
    print(f"Hora de llegada de la peticion: {t2}")
    print(f"Hora recibida del servidor: {datetime_response}")
    print(f"Ajuste: {offset}")
    print(f"Hora final: {final_time}")
    print("Cambiando la hora")
    print(f"date -u {final_time.strftime('%m%d%H%M%Y.%S')}")
    os.system(f"date -u {final_time.strftime('%m%d%H%M%Y.%S')}")


main()
