import datetime
from time import ctime
import ntplib
import os


def main():
    timeserver = "pool.ntp.org"
    ntp_client = ntplib.NTPClient()

    t1 = datetime.datetime.now()
    response = ntp_client.request(timeserver)
    t2 = datetime.datetime.now()
    datetime_response = datetime.datetime.fromtimestamp(response.tx_time)
    time_string = datetime_response.strftime("%a %b %d %H:%M:%S %Y")
    offset = (t2 - t1) / 2
    final_time = datetime_response + offset

    print(f"T1: {t1}")
    print(f"Hora recibida: {datetime_response}")
    print(f"T2: {t2}")
    print(f"Ajuste: {offset}")
    print(f"Hora final: {final_time}")
    print(f"date -u {final_time.strftime('%m%d%H%M%Y')}")
    # os.system(f"date -u {final_time.strftime('%m%d%H%M%Y')}")


main()
