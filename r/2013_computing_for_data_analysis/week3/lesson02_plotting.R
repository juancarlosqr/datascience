
library(datasets)
airquality

good <- complete.cases(airquality)
x <- airquality[good,][,]
x
plot(x$Temp,x$Wind)
plot(x$Temp,x$Month)

promedio <- lapply(split(x$Temp,x$Month),mean)
promedio
xs <- lapply(split(x$Month,x$Month),mean)
xs

plot(xs, promedio)


sep <- x[x(5) = 9,]
sep
plot(x$)

hist(promedio)
hist(as.numeric(promedio))

dev.off()

x <- rnorm(100)
hist(x)

y <- rnorm(50)
hist(y)

dev.set(3)

graphics.off()

?par


# exercise

x <- rnorm(100)
y <- x + rnorm(100)
par(las = 1)
plot(x, y,pch = 16, col = "coral")

par(las = 2)
plot(x, y,pch = 16, col = "coral")

demo("colors")

# params of plot function
# pch
# lty
# lwd
# col
# las
# bg
# mar
# oma
# mfrow
# mfcol
# 

par("lty")
par("lwd")
par("col")
par("pch")


# exercise 2 

x <- rnorm(100)
y <- x + rnorm(100)
plot(x, y,pch = 16, col = "coral")
x1 <- rnorm(10)
y1 <- rnorm(10)
points(x1, y1, pch = 16, col = "blue1")

x2 <- rnorm(100)
y2 <- rep.int(2, 100)
y2
lines(x2,y2)


?Devices



pdf(file = "testRplot.pdf")
x <- rnorm(100)
hist(x)
dev.off()

# crea y abre un archivo para graficar
pdf(file = "testRplot2.pdf")
x <- rnorm(100)
y <- x + rnorm(100)
plot(x, y,pch = 16, col = "coral")
# cierra el archivo
dev.off()

dev.list()

graphics.off()

rm(list = ls())