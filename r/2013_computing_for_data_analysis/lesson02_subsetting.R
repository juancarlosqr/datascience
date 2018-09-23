x <- c("a","b","c","a","d")
x[3]
x[2:4]
x[x>="b"]
#comment
x[x = "a"] # NA
u <- x < "b"
u
x[u]
x <- matrix(1:6, 2, 3)
x
x[2,1]
x[1,2]
x[2,3]
x[2,]
x[,3]
x[1,2]
x[1,2, drop = F]
x
x[,3]
x[,3, drop = F]
x <- list(foo = 1:5, bar = 5.6)
x
x[1]
x[2] # a list with a sequence
x[[2]] # just the sequence
x$bar # just the sequence
x$foo
x[["bar"]] # just the sequence
x["bar"] # a list with a sequence

# extracting multiple values from a list
x <- list(foo = 1:5, bar = 5.6, baz = "hello")
x
x[c(1:3)]
x[c(1,3)]
x[[c(1,3)]] # error
# u cannot use double [[ or $ for extracting multiple values
x
name <- "foo"
x[name] # a list with a sequence
x[[name]] # just the sequence
x$name # NULL

# [[ can contain integer sequences
x <- list(foo = 10:1, bar = 50:60)
x
x[[1]][4] # si quiere extraer el valor 7
x[[2]][6] # si quiere extraer el valor 55
x[[c(1,4)]] # si quiere extraer el valor 7
x[[c(2,6)]] # si quiere extraer el valor 55

#partial matching
x <- list(aqwerty = 1:10)
x$a # the list
x$aq # the list
x$q # NULL 
x[["a"]] # NULL
x[["a", exact = F]]
x <- list(aqwerty = 1:10, asw = "foo")
x
x$a # NULL , found 2 matches
x$aq # the list
x$as # foo!

# removing NAs
x <- c(1,2,NA,6,NA,8,9)
x
bad <- is.na(x)
bad
x[!bad]
good <- x[!bad]
good

# multiple subsets
x <- c(1,2,NA,6,NA,8,9)
y <- c("a",NA,"c","d",NA,"f","g")
x
y
good <- complete.cases(x,y) # verifica que para la misma posicion los dos valores no son NAs
good
x[good]
y[good]
x <- c(1,2,NA,6,NA,8,9,10) # Error in complete.cases(x, y) : not all arguments have the same length

airquality[1:10,]
good <- complete.cases(airquality)
good
table(good)
airquality[good, ][1:6,]
result <- airquality[good, ][1:6,]
result

# examples of airmiles
require(graphics)
plot(airmiles, 
     main = "airmiles example data",
     xlab = "Passenger-miles flown by U.S. commercial airlines", 
     ylab = "miles",
     col = 4)
# ploting result
plot(result, 
     main = "airmiles example data",
     xlab = "Ozone", 
     ylab = "miles",
     col = 1)

# no se pudo graficar :(
