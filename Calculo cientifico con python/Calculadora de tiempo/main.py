# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

add_time("3:30 PM", "2:12")
# add_time("11:55 AM", "3:12")
# add_time("9:15 PM", "5:30")
# add_time("11:40 AM", "0:25")
# add_time("2:59 AM", "24:00")
# add_time("11:59 PM", "24:05")
# add_time("8:16 PM", "466:02")
# add_time("5:01 AM", "0:00")
# add_time("3:30 PM", "2:12", "Monday")
# add_time("2:59 AM", "24:00", "Saturday")
# add_time("11:59 PM", "24:05", "Wednesday")
# add_time("8:16 PM", "466:02", "tuesday")

# Run unit tests automatically
main(module='test_module', exit=False)