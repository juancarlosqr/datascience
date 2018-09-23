library(datasets)
head(airquality)
# str muestra la estructura de un objeto
str(airquality)
head(airmiles)
str(airmiles)

m <- matrix(rnorm(100),10,10)
m
str(m)

# a list representation of the data in form of columns 
s <- split(airquality, airquality$Month)
str(s)

# explorando la funcion split
# devuelve el primer objeto el cual es mayo, no el mes 1
s[1]
# devuelve mayo
s["5"]
# devuelve mayo
s$"5"
# genera error
s$5