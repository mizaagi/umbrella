import miztools as mt
import datetime as dt

"""Set up json appendage tools."""
f = mt.atools("umbrella_storage.json")
dl_td = dt.datetime.now()

"""Add installation date to OS."""
f.append(f"Umbrella installed at {dl_td.month}/{dl_td.day}/{dl_td.year} at {dl_td.hour} hours, 
{dl_td.minute} minutes, {dl_td.second} seconds and {dl_td.microsecond} microseconds GMT.")

f.append(f'{dl_td.month}/{dl_td.day}/{dl_td.year}')
