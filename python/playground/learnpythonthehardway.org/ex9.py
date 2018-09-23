#!/usr/bin/python
# -*- coding: utf-8 -*-

# ex01
print 'hello world'
print "i'm a developer"

# ex02
# this is a comment

# ex03
print 'hens', 25+30 / 6
print 'is it greater', 30 > 6

# ex04
cars = 30
drivers = 40
print "number of cars is", cars, "and total of drivers is", drivers

# ex05
my_twitter = 'juancarlosqr'
my_email_domain = 'gmail.com'
my_age = 25
print "I'm %d years old!" % my_age
print 'My Twitter account is %s' % my_twitter
print 'My Twitter account is %s, and my email is at %s' % (my_twitter, my_email_domain)
print 'My Twitter account is %s, (%d) and my email is at %s' % (my_twitter, my_age*4, my_email_domain)

# ex06
x = "there are %d types of people" % 10
binary = 'binary'
do_not = "don't"
y = "those who know %s, and those who %s" % (binary,do_not)
print x
print y
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = 'this is the left side of...'
e = 'a string with a right side.'
print w + e

# ex07
print '.'*10
end1 = 'a'
end2 = 'b'
end3 = 'c'
end4 = 'd'
print end1 + end2, end3 + end4
print end1 + end2, 
print end3 + end4

# ex08
formatter = "%r %r %r %r"
text = 'hello python'
print formatter % (1, 2, 3, 4)
print formatter % ("one","two","three","four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (1, "two", False, text)

# ex09
feb = 'feb'
jul = 'jul'
sep = 9
days = "mon tue wen thu fri sat sun"
months = "\njan\n%s\nmar\napr\nmay\njun\n%r\n%s\n%s" % (feb, jul, jul, sep)
print "here afre the days: ",days
print "here afre the months: ",months
print """
hi python
there is something going on here
"""

# ex

