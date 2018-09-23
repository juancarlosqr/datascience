#
x <- seq(1, 5, 0.1)
y <- sin(x)
x
y
plot(x,y)

#
plank <- 1:9
plank
matrix(plank,3,3)

#
elev <- matrix(1:10,10,10)
elev
elev[4,5] <- 5
#contorno
contour(elev)

persp(elev, expand=0.1)
elev
elev[1:5,] <- 10:6


# real data
volcano
str(volcano)
contour(volcano)
persp(volcano, expand=0.2)
image(volcano)

# 
help(mean)
x <- c(0:10, 50)
x <- c(0:10,25,"50")
x
xm <- mean(x)
xm
c(xm, mean(x, trim = 0.10))

mean(c(17,15,14,18,12,11,16))
median


#
chests <- c('gold', 'silver', 'gems', 'gold', 'gems')
tipos <- factor(chests)
chests
tipos
chests[tipos]
table(tipos)
print(chests)
print(tipos)
levels(tipos)
