#!/usr/bin/python2
from iso_date import DateDistance, ISODate

class AnotherDate(ISODate):
    def to_anti_iso_format(self):
        
       day_as_string    =  "%02d"  %  self.this_day 

       month_as_string  =  "%02d"  %  self.this_month

       year_as_string   =  "%04d"  %  self.this_year

       string_to_caller  =  day_as_string + "." + month_as_string  \
                           + "."  +  year_as_string

       return  string_to_caller


birthdate = AnotherDate(1994, 11, 03)
date_now = ISODate()
print "Your birthday in anti ISO format is %s " % birthdate.to_anti_iso_format()
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

day_counter        =  0 
second_counter = 0
date_to_increment  =  ISODate( birthdate )
while  day_counter < 20001 :
   day_counter += 1
   date_to_increment.increment()
   if day_counter == 10000:
        print "\nYou will be 10000 days old on %s (%s)" % (date_to_increment,
                                                           date_to_increment.get_day_of_week())
   elif day_counter == 20000:
        print "\nYou will be 20000 days old on %s (%s)" % (date_to_increment,
                                                           date_to_increment.get_day_of_week())
days_to_increment = ISODate(birthdate)
while second_counter < 1000000001:
    second_counter += 1
    if second_counter % (86400) == 0:
        days_to_increment.increment()
    
    if second_counter == 1000000000:
      print "You will be 1000000000 seconds old on %s" % days_to_increment
