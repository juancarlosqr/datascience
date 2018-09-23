x <- as.Date("1970-01-01")
x
unclass(x)
x
unclass(as.Date("1970-01-02"))

x <- Sys.time()
x
p <- as.POSIXlt(x)
names(unclass(p))
p$sec
p$min

x <- Sys.time()
unclass(x)
x$sec
p <- as.POSIXlt(x)
p$sec

?strptime

