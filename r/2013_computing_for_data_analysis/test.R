
source("http://spark-public.s3.amazonaws.com/compdata/scripts/getmonitor-test.R")
getmonitor.testscript()

source("http://spark-public.s3.amazonaws.com/compdata/scripts/complete-test.R")
complete.testscript()

source("http://spark-public.s3.amazonaws.com/compdata/scripts/corr-test.R")
corr.testscript()


library(datasets)
data(iris)
?iris

iris
lista <- split(iris,iris$Species)
mean(split(iris$Sepal.Length,iris$Species))

lapply(iris, )

colMeans(iris$Species,2)

lista$virginica

lapply(lista$virginica, mean)

apply(iris[, 1:4], 2, mean)

apply(iris, 1, mean)

apply(iris, 2, mean)

apply(iris[, 1:4], 1, mean)


library(datasets)
data(mtcars)
?mtcars
mtcars
sapply(split(mtcars$mpg, mtcars$cyl), mean)
split(mtcars$mpg, mtcars$cyl)

lapply(split(mtcars$hp, mtcars$cyl),mean)

abs(82.63636-209.2143)
# 126.5779 # good!


# exercise 2

complete("specdata", 1:5)
complete("specdata", 1)
complete("specdata", c(2, 4, 8, 10, 12)) 
complete("specdata", 30:25) 
complete("specdata", 3)




# exercise 3 
cor(1:10, 21:30)

cr <- corr("specdata", 150)
head(cr)
summary(cr)

cr <- corr("specdata", 400) 
head(cr) 
summary(cr)

cr <- corr("specdata", 5000) 
summary(cr) 
length(cr) 

cr <- corr("specdata") 
summary(cr) 
length(cr) 
