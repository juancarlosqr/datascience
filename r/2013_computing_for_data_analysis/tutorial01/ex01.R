# tutorial en
# http://www.johndcook.com/R_language_for_programmers.html

## VECTORS
vec1 <- c(1:5)
vec1
length(vec1)
vec2 <- c(11:20)
vec2
length(vec2)
# longer object length is not a multiple of shorter object length
# applies a vector recycling feature
# longitud del vector largo debe ser multiplo de la longitud del vector corto
# recicla el vector corto para realizar operaciones
# vectores de longitudes 5 y 5 lo hace
# vectores de longitudes 5 y 9 no lo hace
# vectores de longitudes 5 y 10 lo hace
vec1 + vec2

## SEQUENCES
seq(1, 14, 3)

# The notation a:b is an abbreviation for seq(a, b, 1)
1:14

# secuencia desde el 2 hasta el 50, de 2 en 2
seq(2,50,2)


## TYPES
as.integer(3.2)

## LISTS

a <- list(name="Joe", 4, foo=c(3,8,9))
a$name
a[[1]]
a["name"]
a[["name"]]
a[[2]]
# Now a[[1]] and a$name both equal the string "Joe".


# You can also assign to non-existent named fields, such as saying
a$bar = "hello"
a

# you can assign to a non-existent element of a list
a[[6]] # error: subscript out of bounds
a[[6]] = "world"
a # a[[5]] was created with NULL

# asignando nombres
names(a)
# output before is : 
# [1] "name" ""     "foo"  "bar"  ""     ""  

names(a) <- c("name","age","foo","bar","greet1","greet2")
# output after is : 
# [1] "name"   "age"    "foo"    "bar"    "greet1" "greet2"


## FUNCTIONS

f <- function(a, b=10)
{
  # the word return is optional
  #return (a+b)
  a + b
}

f(10,6)


## MISC

# prints the R version, OS, packages loaded, etc.
sessionInfo()

# shows which objects are defined.
ls()

# clears all defined objects.
rm(list=ls()) 

example(min)
help(min)
min(a$foo)
max(a$foo)