file2 <- "datasets/us_baby_names_1880_2012/yob1880.txt"
classes <- c("character","character","integer")
tableNames <- read.table(
  file2,
  nrows = 2000,
  header=F,
  sep = ",",
  comment.char = "",
  colClasses = classes
)

names(tableNames) <- c("Name","Gender","Records")
tableNames[1:50,,drop = F]
tableNames[1000:1050,]