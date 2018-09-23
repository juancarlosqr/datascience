fnGetTableClasses <- function(filename) {
  temp <- read.table(file = filename, nrows = 100, sep = ",", header = TRUE)
  classes <- sapply(temp, class)
  rm(temp)
  classes
}

cl <- fnGetTableClasses("datasets/nobel_prizes.csv")
cl

source("data.R")

mydata <- read.csv(fullname)



m <- matrix(1:6, 2, 3)
m
m[1,2]
m[2,3]


rm(fnGetTableClasses, cl, mydata, datadir, filename, fullname, m)
