#!/usr/bin/python2
from iso_date import DateDistance, ISODate
birthdate = ISODate(1994, 11, 03)
date_now = ISODate()

distance_between = birthdate.get_distance_to(date_now)

print "\nYou are %d years, %d months, and %d days" \
      " old.\n"  %  ( distance_between.years,
      distance_between.months, distance_between.days )
print "Your birth week was %d" % birthdate.get_week_number()

years_to_celebrate = 10

while years_to_celebrate < 80:
    date_to_celebrate = ISODate(birthdate.year() + years_to_celebrate,
                                birthdate.month(),
                                birthdate.day())
    print "\n %d years old on %s (%s)" % (years_to_celebrate,
          date_to_celebrate, date_to_celebrate.get_day_of_week()),

    years_to_celebrate += 10
