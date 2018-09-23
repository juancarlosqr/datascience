class(1)

class(TRUE)

class(NA)

class(rnorm(10))

class("foo")

x <- rnorm(100)
y <- x + rnorm(100)
fit <- lm(x ~ y)
class(fit)

# S3 classes
mean
print

# S4 classes
show

# to view the methods of S3
methods("mean")
methods("print")
methods("plot")
# to view the methods of S4
showMethods("show")
showMethods("plot")

head(getS3method("mean","Date"))
tail(getS3method("mean","default"))

set.seed(10)
x <- rnorm(100)
x <- as.ts(x)
plot(x)


# defining a class
setClass("polygon", 
         representation(x = "numeric",
                        y = "numeric"))
# defining a method
setMethod("plot",
          "polygon",
          function(x, y, ...){
            plot(x@x, x@y, type = "n", ...)
            xp <- c(x@x, x@x[1])
            yp <- c(x@y, x@y[1])
            lines(xp, yp)
          })

p <- new("polygon", x = c(1,2,3,4), y = c(1,2,3,1))
plot(p)

