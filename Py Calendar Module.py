# Calendar Module
# The calendar module allows you to output calendars and 
# provides additional useful functions for them.

# class calendar.TextCalendar([firstweekday])

# This class can be used to generate plain text calendars.

# Task

# You are given a date. Your task is to find what the day is on that date.

# Input Format

# A single line of input containing the space separated month,
# day and year, respectively, in  MM DD YYYY  format.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

mm, dd, yyyy = map(int, input().split())
day_of_week = calendar.weekday(yyyy, mm, dd)
day_name = calendar.day_name[day_of_week]
print(day_name.upper())