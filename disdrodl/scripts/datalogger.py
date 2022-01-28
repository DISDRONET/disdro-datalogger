import time
from loguru import logger
# from disdrodl import Parsivel
# from disdrodl.thies import Thies
# from os import environ
# import csv

DATA_DIR = "/data"


# class ParsivelDataLogger(Parsivel):
#     def __init__(self):
#         super().__init__()
#
#     def loop_forever(self) -> None:
#         while True:
#             dt = time.strftime("%Y%m%d-%H%M%S")
#             todays_date = time.strftime("%Y%m%d")
#             filename = DATA_DIR + todays_date + '.csv'
#             field_61 = todays_date + '_field61.csv'
#
#             try:
#                 parsivel_bytes = self.ser.readline()
#
#                 if 0 <= len(parsivel_bytes) <= 5:
#                     logger.info(parsivel_bytes)
#                 elif 5 < len(parsivel_bytes) < 20:
#                     with open(field_61, "a") as g:
#                         writer = csv.writer(g, delimiter=";")
#                         writer.writerow([dt, time.time(), parsivel_bytes])
#                     logger.info(parsivel_bytes)
#                 else:
#                     with open(filename, "a") as f:
#                         writer = csv.writer(f, delimiter=";")
#                         writer.writerow([dt, time.time(), parsivel_bytes])
#                         print(parsivel_bytes)
#                         time.sleep(1)
#                         self.request_field_61()
#
#             except Exception as e:
#                 if hasattr(e, 'message'):
#                     logger.error(e.message)
#                 else:
#                     logger.error(e)


if __name__ == "__main__":
    # device_logger = ParsivelDataLogger()
    # device_logger.loop_forever()
    while True:
        logger.info("I'm working!")
        time.sleep(3)
