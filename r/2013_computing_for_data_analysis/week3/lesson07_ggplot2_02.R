
testdata <- data.frame(x = 1:100, y = rnorm(100))
testdata[50,2] = 100
plot(testdata$x, testdata$y, type="l", ylim=c(-3,3))

g <- ggplot(testdata, aes(x = x, y = y))
g + geom_line()

g + geom_line() + ylim(-3,3)

g + geom_line() + coord_cartesian(ylim = c(-3,3))

