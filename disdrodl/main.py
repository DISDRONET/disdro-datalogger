#!/usr/bin/env python3

import serial
import time
import csv
from variables import port, baud

# import send_data


parsivel = serial.Serial(port, baud, timeout=1)  # Defines the serial port
parsivel.reset_input_buffer()  # Flushes input buffer
# parsivel.write(parsivel_ott_telegram.encode('utf-8')) # Writes the Parsivel OTT telegram command to the Parsivel
# parsivel.write(parsivel_set_telegram_list.encode('utf-8')) # Writes the parsivel user telegram string to the Parsivel
# parsivel.write(parsivel_telegram_command.encode('utf-8'))
# parsivel.write(parsivel_command_list.encode('utf-8'))
# parsivel.write(parsivel_user_telegram.encode('utf-8'))
# parsivel.write(parsivel_telegram_start.encode('utf-8'))
# parsivel.write(parsivel_current_configuration.encode('utf-8'))
# parsivel.write(parsivel_impulse_mode.encode('utf-8'))
# parsivel.write(parsivel_set_name.encode('utf-8'))
# parsivel.write(parsivel_set_ID.encode('utf-8'))
# parsivel.write(parsivel_real_time.encode('utf-8'))
# parsivel.write(parsivel_request_field_90.encode('utf-8'))
# parsivel.write(parsivel_set_real_time.encode('utf-8'))
# parsivel.write(parsivel_restart.encode('utf-8'))
# parsivel.write('CS/R/19\r'.encode('utf-8'))

while True:
    try:
        parsivel_bytes = parsivel.readline()  # Reads the output the serial communication
        datetime1 = time.strftime("%Y%m%d-%H%M%S")
        todays_date = time.strftime("%Y%m%d")
        filename = todays_date + '.csv'
        field_61 = todays_date + '.csv'

        if len(parsivel_bytes) < 20:
            print(parsivel_bytes)
        else:
            with open(filename, "a") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow([datetime1, time.time(), parsivel_bytes])
            print(parsivel_bytes)
    #           time.sleep(10)
    #             with open(field_61, "a") as g:
    #                     parsivel.write(parsivel_request_field_61.encode('utf-8'))
    #                     writer = csv.writer(g, delimiter=";")
    #                     writer.writerow([datetime1, time.time(), parsivel_bytes])
    #             print(parsivel_bytes)

    #               send_data.SendtoWebServer()
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
