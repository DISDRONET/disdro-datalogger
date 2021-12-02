#!/usr/bin/env python3

# import csv
import time
import serial

# parsivel = serial.Serial('/dev/ttyUSB0', baudrate=19200, timeout=1)  # Defines the serial port
# parsivel.reset_input_buffer()  # Flushes input buffer

Parsivel_name = 'PAR002'
Parsivel_ID = '002'
parsivel_telegram_command = 'CS/RA\r'  # Asks the Parsivel to read out all fields
parsivel_request_field_61 = 'CS/R/61\r'  # Asks the Parsivel to read out field 61
parsivel_request_field_90 = 'CS/R/90\r'  # Asks the Parsivel to read out field 61
parsivel_command_list = 'CS/?\r'  # Reads out a list of serial commands for the Parsivel.
parsivel_ott_telegram = 'CS/M/M/0\r'  # The Parsivel broadcasts the OTT telegram.
parsivel_telegram_start = 'CS/*/D/0\r'  # The Parsivel broadcasts the OTT telegram.
# parsivel_user_telegram = 'CS/M/M/1\r'  # The Parsivel broadcasts the user defined telegram.
parsivel_set_telegram_list = 'CS/M/S/%01;%02;%03;%04;%05;%06;%07;%08;%09;%10;%11;%12;%13;%14;%15;%16;%17;%18;%19;%20;%21;%22;%23;%24;%25;%26;%27;%28;%30;%31;%32;%33;%34;%35;%60;%90;%91;%93\r'  # Defines which fields are in the telegram
parsivel_current_configuration = 'CS/L\r'  # Outputs current configuration
parsivel_impulse_mode = 'CS/I/60\r'  # Turns poll mode off
parsivel_set_time = 'CS/T/' + time.strftime("%H:%M:%S") + '\r'  # Sets the time on the Parsivel to the time on the Pi
parsivel_set_date = 'CS/D/' + time.strftime("%d.%m.%Y") + '\r'  # Sets the date on the Parsivel to the date on the Pi
parsivel_set_name = 'CS/K/' + Parsivel_name + '\r'  # Sets the name of the Parsivel, maximum 10 characters
parsivel_set_ID = 'CS/J/' + Parsivel_ID + '\r'  # Sets the ID of the Parsivel, maximum 4 numerical characters
parsivel_reset_factory_settings = 'CS/F/1\r'  # Resets the Parsivel to factory settings.
# parsivel_real_time = 'CS/U\r'
# parsivel_set_real_time = 'CS/U/' + time.strftime("%d.%m.%Y ") + time.strftime("%H:%M:%S") + '\r'
# parsivel_restart = 'CS/Z/1\r'

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


def main():
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

if __name__ == '__main__':
    pass
