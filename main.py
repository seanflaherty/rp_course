from clock import Clock

bed_room_clock = Clock("06:00", "08:00")
kitchen_clock = Clock("12:00", "18:00")
time_bed_room = bed_room_clock.set_clock_time().strftime("%H:%M")
time_kitchen = kitchen_clock.set_clock_time().strftime("%H:%M")
print(time_bed_room)
print(time_kitchen)
    