#!/usr/bin/python2
from iso_date import DateDistance, ISODate
my_birthdate = ISODate(1994, 11, 03)
date_now = ISODate()


distance_between = my_birthdate.get_distance_to(date_now)



print "\n   I am %d years, %d months, and %d days" \
      " old.\n"  %  ( distance_between.years,
      distance_between.months, distance_between.days )
