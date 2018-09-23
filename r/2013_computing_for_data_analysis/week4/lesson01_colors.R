colors()

# function colorRampPalette
pal <- colorRampPalette(c("red", "yellow", "blue","green"))
x <- rnorm(100)
plot(x, col = pal(10))

# package RColorBrewer
library(RColorBrewer)
cols <- brewer.pal(3, "BuGn")
cols
pal <- colorRampPalette(cols)
image(volcano, col = pal(20))

# function smoothScatter
x <- rnorm(10000)
y <- rnorm(10000)
smoothScatter(x,y)

# transparency
x <- rnorm(1000)
y <- rnorm(1000)
plot(x,y,pch=19)
# black
plot(x,y,col=rgb(0,0,0,0.2),pch=19)
# red
plot(x,y,col=rgb(1,0,0,0.2),pch=19)
# green
plot(x,y,col=rgb(0,1,0,0.2),pch=19)
# blue
plot(x,y,col=rgb(0,0,1,0.2),pch=19)
# yellow
plot(x,y,col=rgb(1,1,0,0.2),pch=19)
# magenta
plot(x,y,col=rgb(1,0,1,0.2),pch=19)
# cyan
plot(x,y,col=rgb(0,1,1,0.2),pch=19)
