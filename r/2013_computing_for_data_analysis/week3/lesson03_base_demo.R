x <- rnorm(100)
hist(x)

y <- rnorm(100)

plot(x ,y)

par(mar = c(4,4,2,2))
plot(x, y, pch = 20)

example(points)

title("Scatterplot")
text(2, -2, "Plot")
legend("topright", legend = "Data", pch = 20)

# to change the numbers of plot in the screen
par(mfrow = c(1, 2))

z<-rpois(100,1)
plot(x,z,pch=15)

# points function

x <- rnorm(100)
y <- x + rnorm(100)
g <- gl(2, 50, labels = c("Male", "Female"))
str(g)
plot(x, y, type="n")
points(x[g == "Female"], y[g == "Female"], col = "red", pch = 19)
points(x[g == "Male"], y[g == "Male"], col = "blue", pch = 19)
