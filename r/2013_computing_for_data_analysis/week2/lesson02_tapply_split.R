library(datasets)
head(airquality)

s <- split(airquality, airquality$Month)
s
lapply(s, function(x) colMeans(x[,c("Ozone","Solar.R","Wind")]))
sapply(s, function(x) colMeans(x[,c("Ozone","Solar.R","Wind")], na.rm = TRUE))