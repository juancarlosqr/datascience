x <- data.frame(foo = 1:4, bar = c(T, T, F, F))
x
nrow(x)
ncol(x)
names(x)

x <- 1:3
names(x)
names(x) <- c("foo","bar","baz")
x
y <- list(a = 2 , b = 4 , c = 6)
y <- list(2 , 4 , 6)
y
y[[1]]

# subsetting

# vectors

x <- c("a","c","b","d","c","b","b")
x[2]
x[[2]]
x$foo
x["bar"]
x[["bar"]]
x[1:3]
x[x == "b"]
x[x >= "c"]

# matrix
xm <- matrix(1:6, 2, 3)
xm
xm[1, 2, drop=FALSE]
xm[1, ]
xm[1, , drop=FALSE]

#list
xl <- list(foo = 1:4, bar = 0.6)
xl
xl[1]
xl[2]
xl$bar
xl[[1]]
xl <- list(foo = 1:4, bar = 0.6, baz = "hello")
xl
xl[c(1,3)]

name <- "foo"
xl[[name]]
xl <- list(a = list(10, 12, 14), b = c(3.14, 2.81))
xl[[c(1, 3)]]
xl
library(help = "datasets")
library("datasets")
initial <- airquality
initial

