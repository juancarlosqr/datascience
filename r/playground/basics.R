# module operator
10%%3

# variables 
4+4 -> y
y

x <- c(2,3,4)
x

z = c(1:10)
z

assign("q", c(10:50))
q

# list existing variables

ls()
objects()

# removing

a = "some var"
rm("a")

y = c(x, 100, x)
y
lessthan5 = y > 5
lessthan5

sum(y)

sqrt(y)

y[2]

# data sequences

seq(2,10)
# [1]  2  3  4  5  6  7  8  9 10

seq(from=2, to=10)
# [1]  2  3  4  5  6  7  8  9 10

seq(from=5, length=10)
# [1]  5  6  7  8  9 10 11 12 13 14

seq(from=50, length=10, by=0.5)
# [1] 50.0 50.5 51.0 51.5 52.0 52.5 53.0 53.5 54.0 54.5

rep(c(1:3), 3)
# [1] 1 2 3 1 2 3 1 2 3

rep(1:5, times=3)
# [1] 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5

s <- c(1,2,3)
rep(s, each=3)
# [1] 1 1 1 2 2 2 3 3 3

rep(s, each=3, times=3)
# [1] 1 1 1 2 2 2 3 3 3 1 1 1 2 2 2 3 3 3 1 1 1 2 2 2 3 3 3

help(rep)

# functions

paste("foo", 1:5)
# [1] "foo 1" "foo 2" "foo 3" "foo 4" "foo 5"

paste("foo", c(2,4,6,"bar", 10))
# [1] "foo 2"   "foo 4"   "foo 6"   "foo bar" "foo 10" 

paste("foo", 1:6, sep="")
# [1] "foo1" "foo2" "foo3" "foo4" "foo5" "foo6"

# knowing position

x = c(2:20)
x
which(x == 10)
#[1] 9

x[3]

# exercises

paste("R is great", c(4,7,45), "and i will love it")
# [1] "R is great 4 and i will love it" 
# [2] "R is great 7 and i will love it" 
# [3] "R is great 45 and i will love it"

y <- c(1:3)
y
rep(y, length=31)
# [1] 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1


# functions

myFunc <- function(x) {
  (x+x)*3
}
myFunc(5)

# R is functional

myFuncDouble <- function(fn) {fn(2)}
myFuncPlusFive <- function(y) {
  y+5
}
myFuncDouble(myFuncPlusFive)
# [1] 7

# loops

for (i in 1:10) {print(i)}


# datasets

library("datasets") # built-in RStudio datasets
?lynx
head(lynx) # first 6 elements
?iris # dataframes
head(iris)
tail(lynx) # last 6 elements
lynxSummary <- summary(lynx)
lynxSummary

plot(lynx)
hist(lynx)

sum(iris$Sepal.Length)
iris$Species
levels(iris$Species)


jcdata <- matrix(c(1:12), 4, 3)
jcdata
head(jcdata)
tail(jcdata)
summary(jcdata)

plot(jcdata)
hist(jcdata)

# setwd(path) to set the working directory

datadir <- "nba/"

files <- list.files(datadir)
files

nba <- read.csv(paste(datadir,files[1], sep=""))
nba
levels(nba$bref_team_id) # all teams
length(levels(nba$bref_team_id)) # 31 teams
levels(nba$pos) # all positions

head(nba)
tail(nba)

nba["player"]
nba$player
nba[1, 5]
nba[5, 1]


# Graphs

x <- 5:8
y <- 18:15
plot(x,y)
plot(lynx)
plot(lynx, main="Lynx Trappings", col="orange", col.main=75, cex.main=1.5)
# the cex family can be used to change magnification factors

plot(lynx, ylab="Lynx Trappings", xlab="", col="orange")
plot(lynx, ylab="Lynx Trappings", xlab="", col="orange", las=1)
# change the scale direction
#las = 0 is for xlabs horiz, ylabs vert (default)
#las = 1 is for xlabs horiz, ylabs horiz
#las = 2 is for xlabs vert,  ylabs horiz
#las = 3 is for xlabs vert,  ylabs vert


colors()
x=2:10
?pch
plot(x, pch="e")
plot(x, pch=18)


plot(lynx)
plot(lynx, type="p", main="Type p") # points (default) 
plot(lynx, type="l", main="Type l") # lines (default for time series)
plot(lynx, type="b", main="Type b") # points connected by lines
plot(lynx, type="o", main="Type o") # points overlaid by lines
plot(lynx, type="h", main="Type h", las=1, col="orange") # high density
plot(lynx, type="s", main="Type s") # steps
plot(lynx, type="n", main="Type n") # no plot

# Graphs parameters
par()
?par

# Graph exercise
# my solution
?rivers
length(rivers)
plot(rivers, xlab="River Index", ylab = "Length", 
     main = "Rivers\nlength", col.main="red", las=1, pch=18, col="green")

# provided solution
?rivers
x = 1:141
y= rivers
plot(x,y, col = "green", pch = 20,
     main = "Lengths of\nMajor N. American Rivers",
     col.main ="red", xlab = "",
     ylab = "length in miles")


# apply family functions

?apply
example(apply)

x <- matrix(c(1:9), nr = 3, byrow = T)
x
y <- matrix(c(1:9), nr = 3, byrow = F)
y

# MARGIN :: 1 for row, 2 for col

apply(x, 1, mean)
apply(x, 2, mean)

apply(x, 1, plot)



# exercise

install.packages("ggplot2")
library(ggplot2)
?qplot
?diamonds
?nortest

head(diamonds)
tail(diamonds)

# normality test
qqnorm(diamonds$depth) # looks to curvy for normal distribution
hist(diamonds$depth) # hist looks also not normal

depthsmall = sample(diamonds$depth, 5000)

shapiro.test(depthsmall) #shapiro can take up to 5000 observations
#  Shapiro-Wilk normality test
#     data:  depthsmall
#     W = 0.93432, p-value < 2.2e-16

# as the p-value is a significantly high value,
# this depth data is not normally distributed


# Tests for Normality
install.packages("nortest") 
library(nortest)

cvm.test(diamonds$depth)
#  Cramer-von Mises normality test
#data:  diamonds$depth
#W = 88.147, p-value = 7.37e-10

lillie.test(diamonds$depth)
# Lilliefors (Kolmogorov-Smirnov) normality test
# data:  diamonds$depth
# D = 0.075871, p-value < 2.2e-16

sf.test(depthsmall)
# Shapiro-Francia normality test
# data:  depthsmall
# W = 0.93318, p-value < 2.2e-16

pearson.test(diamonds$depth)
# Pearson chi-square normality test
# data:  diamonds$depth
# P = 153230, p-value < 2.2e-16