file1 <- "datasets/number_of_policies_by_program_by_state_feb_2012.csv"
file1
initial <- read.csv(file1, nrows = 20)
initial[8,1, drop = FALSE]
initial[,1, drop = FALSE]
classes <- sapply(initial, class)
classes
tabAll <- read.csv(file1, colClasses = classes)
tabAll[,8, drop = F]
tabAll[,c(1,2,8), drop = F]
tabAll
# calculando el total
length(tabAll)
nrow(tabAll)
tabAll[c(1: nrow(tabAll) - 1),8, drop = F]
sum(tabAll[c(1: nrow(tabAll) - 1),8]) # \o/ :)
# calculando el total en todas las columnas
tabAll[c(1: nrow(tabAll) - 1),8, drop = F]
sumas <- c(sum(tabAll[c(1: nrow(tabAll) - 1),c(2:8)]))
sumas
sumas[,,drop = F]
sumas <- tabAll[c(1:nrow(tabAll)-1),2:8]
sumas
totales <- sum(sumas)
completa <- complete.cases(tabAll)
completa
tabAll[completa,]
matrix(completa)
sum(tabAll[c(1: nrow(tabAll) - 1),6])