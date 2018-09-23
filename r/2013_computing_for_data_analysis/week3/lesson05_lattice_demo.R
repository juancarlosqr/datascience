library(lattice)
package ? lattice
library(help = lattice)

data(environmental)
?environmental
environmental
head(environmental)
xyplot(ozone ~ radiation, data = environmental)
xyplot(ozone ~ radiation, data = environmental, main = "Ozone vs. Radiation")
xyplot(ozone ~ temperature, data = environmental, main = "Ozone vs. Temperature")

temp.cut <- equal.count(environmental$temperature, 4)
xyplot(ozone ~ radiation | temp.cut, data = environmental)
xyplot(ozone ~ radiation | temp.cut, data = environmental, layout=c(1,4), as.table=TRUE)

xyplot(ozone ~ radiation | temp.cut, data = environmental, as.table=TRUE,
       panel = function(x,y,...){
         panel.xyplot(x,y,...)
         fit <- lm(y ~ x)
         panel.abline(fit)
       })


xyplot(ozone ~ radiation | temp.cut, data = environmental, as.table=TRUE,
       panel = function(x,y,...){
         panel.xyplot(x,y,...)
         panel.loess(x,y)
       }, xlab="Solar Radiation", ylab="Ozone", main="Ozone vs. Solar Radiation")



wind.cut <- equal.count(environmental$wind, 4)
wind.cut 
xyplot(ozone ~ radiation | temp.cut * wind.cut, 
       data = environmental, as.table=TRUE,
       panel = function(x,y,...){
         panel.xyplot(x,y,...)
         panel.loess(x,y)
       }, xlab="Solar Radiation", ylab="Ozone", main="Ozone vs. Solar Radiation")

splom(~environmental)
histogram(~wind, data = environmental)
histogram(~temperature, data = environmental)
histogram(~ozone, data = environmental)
histogram(~radiation, data = environmental)

histogram(~temperature | wind.cut, data = environmental)
histogram(~ozone | wind.cut, data = environmental)
histogram(~ozone | temp.cut * wind.cut, data = environmental)

