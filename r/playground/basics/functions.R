# my means implementation
columnMean <- function(data){
  # print(data)
  len <- length(data)
  if (len == 0) {
    print("Great! no data so i don't have to do anything")
  } else {
    print("Great! lets do some work")
    len <- dim(data)[2]
    for (i in 1:len){
      sum <- 0
      column <- data[,i]
      totalItems <- length(column)
      for (j in 1:totalItems){
        sum <- sum + column[j]
      }
      print(sum/totalItems)
    }
  }
}

# Roger Peng means implementation
rogerPengMeans <- function(d, removeNA = TRUE){
  nc <- ncol(d)
  means <- numeric(nc)
  for(i in 1:nc){
    means[i] <- mean(d[,i], na.rm = removeNA)
  }
  means
}

m <- matrix(1:20, 5, 4)

library("datasets")

columnMean(m)
columnMean(airquality)

print(rogerPengMeans(m))
print(rogerPengMeans(airquality))

data <- rnorm(100)
head(data)
sd(data)
