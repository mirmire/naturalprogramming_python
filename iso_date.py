
#  ISODate.py  Copyright (c) Kari Laitinen

#  http://www.naturalprogramming.com

#  2006-05-01  File Date.py created.
#  2009-01-20  File ISODate.py created.
#  2009-01-23  Last modification.

#  This file is a slightly modified version of Date.py.
#  The difference between the ISODate class and the original
#  Date class is that ISODate objects must be created so
#  that date information is given in format YYYY-MM-DD 
#  which is the format recommended by an ISO standard.
#  ISODate objects are also printed in this format.
#  The ISODate constructor creates an object of "current date"
#  if no initialization values are given. The class CurrentDate,
#  which is a subclass of the original Date class, is thus
#  somewhat superfluous.

#  The logical functionality of classes ISODate and Date
#  is the same.

#  Two classes are defined in this file (module). The ISODate class
#  represents a date. The DateDistance class is a helper class
#  that represents a chronological distance between two Date
#  instance objects. ISODate method get_distance_to() returns a
#  DateDistance object and initializes the three data fields,
#  years, months and days, inside the object.

#  More notes at the end of this file.

from datetime import date  # to get the computer system date

class  DateDistance :

   pass


class  ISODate :

   #  The single constructor allows Date objects to be constructed
   #  in several ways. *given_parameters means that a varying
   #  number of parameters can be given to this constructor, and
   #  given_parameters refers to a tuple that contains the parameters.

   def __init__(  self, *given_parameters ) :

      if len( given_parameters ) == 3 :

         # We suppose that the object was created by giving
         # three integer values as parameters, e.g., ISODate( 2009, 1, 22 )

         self.this_year    =  given_parameters[ 0 ]
         self.this_month   =  given_parameters[ 1 ]
         self.this_day     =  given_parameters[ 2 ]
            
      elif len( given_parameters ) == 1 and \
           isinstance( given_parameters[ 0 ], str ) :

         #  The date was given as a string. We'll suppose that the
         #  the date is given in the ISO format YYYY-MM-DD

         date_as_string  =  given_parameters[ 0 ]
      
         self.this_year  = int( date_as_string[ 0 : 4 ] )
         self.this_month = int( date_as_string[ 5 : 7 ] )
         self.this_day   = int( date_as_string[ 8 :   ] )


      elif len( given_parameters ) == 1 and \
           isinstance( given_parameters[ 0 ], ISODate ) :

         #  Another ISODate object was given as a parameter.
         #  let's make a copy of that object.

         another_date  =  given_parameters[ 0 ]

         self.this_year  = another_date.this_year
         self.this_month = another_date.this_month
         self.this_day   = another_date.this_day


      elif len( given_parameters ) == 0 :

         #  No parameters were given when the ISODate object was
         #  created. We'll read the system date.
         
         current_system_date  =  date.today()
      
         self.this_year   =  current_system_date.year
         self.this_month  =  current_system_date.month
         self.this_day    =  current_system_date.day

      else :

         print  "\n Wrong type of argument to ISODate constructor."


   def day( self ) :     return  self.this_day
   def month( self ) :   return  self.this_month
   def year( self ) :    return  self.this_year

   def is_last_day_of_month( self ) :

      it_is_last_day_of_month  =  False

      if  self.this_day  >  27  :

         if  self.this_day  ==  31  :

            it_is_last_day_of_month  =  True

         elif  self.this_day  ==  30  and  \
               ( self.this_month  ==  2  or  self.this_month  ==  4  or  \
                 self.this_month  ==  6  or  self.this_month  ==  9  or  \
                 self.this_month  ==  11 )  :

            it_is_last_day_of_month  =  True

         elif  self.this_day  ==  29  and  self.this_month  ==  2  :

            it_is_last_day_of_month  =  True

         elif  self.this_day    ==  28  and  \
               self.this_month  ==   2  and  \
               not self.this_is_a_leap_year() :

            it_is_last_day_of_month  =  True

      return  it_is_last_day_of_month


   def this_is_a_leap_year( self )  :

      return_code  =  False

      if  self.this_year  %  4   ==  0  :

         #  Years which are equally divisible by 4 and which
         #  are not full centuries are leap years. Centuries
         #  equally divisible by 4 are, however, leap years.

         if  self.this_year  %  100  ==  0  :

            century  =  self.this_year  /  100

            if  century  %  4   ==   0  :

               return_code  =  True

         else  :

            return_code  =  True

      return  return_code


   def is_within_dates( self, earlier_date, later_date )  :

      return (( self.is_equal_to( earlier_date )  )  or  \
              ( self.is_equal_to( later_date )   )  or  \
              ( self.is_later_than( earlier_date ) and   \
                self.is_earlier_than( later_date ) ) )


   def index_for_day_of_week( self )  :

      #  day_index will get a value in the range from 0 to 6,
      #  0 meaning Monday and 6 meaning Sunday.

      day_index  =  0

      known_date  =  ISODate( "1997-10-06" )
      # Oct. 6, 1997 is Monday.

      if  known_date.is_later_than( self )  :

         while  known_date.is_not_equal_to( self )  :

            if  day_index  >  0  :

               day_index  -=  1

            else  :

               day_index  =  6

            known_date.decrement()

      else  :

         while  known_date.is_not_equal_to( self )  :

            if  day_index  <  6  :

               day_index  +=  1

            else  :

               day_index  =  0


            known_date.increment()

      return  day_index


   def get_day_of_week( self )  :

      days_of_week  =  ( "Monday", "Tuesday", "Wednesday",
                         "Thursday", "Friday", "Saturday", "Sunday" )

      return  days_of_week[ self.index_for_day_of_week() ]


   def increment( self )  :

      if  self.is_last_day_of_month()  :

         self.this_day   =  1

         if   self.this_month  <  12  :

            self.this_month  +=  1

         else  :

            self.this_month  =  1
            self.this_year  +=  1

      else  :

         self.this_day  +=  1



   def decrement( self )  :

      if  self.this_day  >  1  :

         self.this_day  -=  1

      else  :

         if  self.this_month  ==   5  or  self.this_month  ==   7  or   \
             self.this_month  ==  10  or  self.this_month  ==  12  :

            self.this_day    =  30
            self.this_month  -=  1

         elif  self.this_month  ==   2  or  self.this_month  ==   4  or  \
               self.this_month  ==   6  or  self.this_month  ==   8  or  \
               self.this_month  ==   9  or  self.this_month  ==  11   :

            self.this_day    =  31
            self.this_month  -=  1

         elif  self.this_month  ==  1  :

            self.this_day    =  31
            self.this_month  =  12
            self.this_year   -=  1

         elif  self.this_month  ==  3  :

            self.this_month  =  2

            if  self.this_is_a_leap_year()  :

               self.this_day  =  29

            else  :

               self.this_day  =  28


   def get_distance_to( self, another_date )  :

      distance_to_return  =  DateDistance()

      if  self.is_earlier_than( another_date ) :

         start_date  =  self
         end_date    =  another_date

      else :

         start_date  =  another_date
         end_date    =  self


      #  We will suppose that day 30 is the last day of every
      #  month. This way we minimize calculation errors.

      if  start_date.is_last_day_of_month() or  \
           ( start_date.day()    ==  28  and   \
             start_date.month()  ==  2  )    :

         start_day   =  30

      else :

         start_day   =  start_date.day()


      if  end_date.is_last_day_of_month() or  \
           ( end_date.day()    ==  28  and   \
             end_date.month()  ==  2  )     :

         end_day   =  30

      else :

         end_day   =  end_date.day()


      distance_to_return.years  =  end_date.year()  - start_date.year()
      distance_to_return.months =  end_date.month() - start_date.month()
      distance_to_return.days   =  end_day  -  start_day

      if  distance_to_return.days  <  0  :

         distance_to_return.months  -=  1
         distance_to_return.days  =  distance_to_return.days  +  30


      if  distance_to_return.months  <  0  :

         distance_to_return.years   -=  1
         distance_to_return.months  =  distance_to_return.months +  12

      return  distance_to_return



   def get_week_number( self )  :

      # January 1, 1883 was a Monday with week number 1.
      # January 1, 1990 was a Monday with week number 1.

      date_to_increment  =  ISODate( "1883-01-01" )
      week_number  =  1
      local_index_for_day_of_week  =  0   # 0 means Monday

      while  date_to_increment.is_earlier_than( self ) :

         date_to_increment.increment()

         if  local_index_for_day_of_week  ==  6  :  # 6 means Sunday

            local_index_for_day_of_week  =  0   # back to Monday

            if  week_number  <   52  :

               week_number  +=  1

            elif  week_number  ==  52  :

               if  date_to_increment.day()    <=  28  and   \
                   date_to_increment.month()  ==  12   :

                  week_number  =  53

               else  :

                  week_number  =  1

            else  :  # must be week_number  53

               week_number  =  1

         else  :

            local_index_for_day_of_week  +=  1

      return  week_number



   def is_equal_to( self, another_date )  :

      return ( self.this_day    ==  another_date.day()    and   \
               self.this_month  ==  another_date.month()  and   \
               self.this_year   ==  another_date.year()  )


   def is_not_equal_to( self, another_date )  :

      return ( self.this_day    !=  another_date.day()    or   \
               self.this_month  !=  another_date.month()  or   \
               self.this_year   !=  another_date.year()  )


   def is_earlier_than( self, another_date )  :

      return ( (   self.this_year  <   another_date.year()     )  or  \
               ( ( self.this_year  ==  another_date.year() )  and     \
                 ( self.this_month <   another_date.month() )  )  or  \
               ( ( self.this_year  ==  another_date.year() )  and     \
                 ( self.this_month ==  another_date.month() ) and     \
                 ( self.this_day   <   another_date.day() )   )    )

   def is_later_than( self, another_date )  :

      return ( (   self.this_year  >   another_date.year()     )  or  \
               ( ( self.this_year  ==  another_date.year() )  and     \
                 ( self.this_month >   another_date.month() )  )  or  \
               ( ( self.this_year  ==  another_date.year() )  and     \
                 ( self.this_month ==  another_date.month() ) and     \
                 ( self.this_day   >   another_date.day() )   )    )


   def __str__( self )  :

      day_as_string    =  "%02d"  %  self.this_day 

      month_as_string  =  "%02d"  %  self.this_month

      year_as_string   =  "%04d"  %  self.this_year

      string_to_caller  =  year_as_string + "-" + month_as_string  \
                           + "-"  +  day_as_string

      return  string_to_caller

#  This program follows at least the basic idea of
#  ISO 8601, which is an international standard for
#  date and time representations issued by the International
#  Organization for Standardization (ISO)

#  The signature feature of ISO 8601 date and time representations
#  is the ordering of date and time values from the most
#  to the least significant or, in plain terms, from
#  the largest (the year) to the smallest (the second).




