rm(list=ls())
rm("good")

dfile <- "../datasets/calidad-aire-2013.csv"
initial <- read.csv2(dfile)
initial
classes <- sapply(initial, class)
classes
tfinal <- read.csv2(dfile, colClasses = classes)
tfinal

summary(tfinal)
str(tfinal)
split(tfinal,tfinal$contaminante)


