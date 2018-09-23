install.packages("ggplot2")

library(ggplot2)
str(mpg)
?mpg
mpg

qplot(displ, hwy, data=mpg)
qplot(displ, hwy, data=mpg, color = drv)
qplot(displ, hwy, data=mpg, geom=c("point","smooth"))
# histogram
qplot(hwy, data=mpg, fill = drv)

qplot(displ, hwy, data=mpg, facets = .~drv)

qplot(hwy, data=mpg, facets = drv~., binwidth=2)

graphics.off()
