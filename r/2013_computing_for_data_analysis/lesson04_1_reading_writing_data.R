fileA <- "datasets/us_baby_names_1880_2012/yob1880.txt"
initial <- read.table(fileA, nrows = 100)
classes <- sapply(initial, class)
tabAll <- read.table(fileA, colClasses = classes)
tabAll