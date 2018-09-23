archivo <- "../datasets/hw1_data.csv"

tabla <- read.csv(archivo)

str(tabla[[1]],)

tabla[1:2,]

tabla[c(nrow(tabla)-1,nrow(tabla)),]

tabla[47,1]

col1 <- tabla[,1]
col1
length(col1)

nulos1 <- is.na(col1)
nonulos1 <- complete.cases(col1)
col1[1:10]
col1[nonulos1][1:10]
length(nulos1)
length(col1) -  length(col1[nonulos1])
mean(col1[nonulos1])


tabla[1:10,]
complete.cases(tabla[1:10,])



##################

good <- complete.cases(tabla)
good
tabla[good,][,]
full <- tabla[good,][,]

full1 <- full[full[1]>31,]
full1
full2 <- full1[full1[4]>90,]
full2
mean(full2[[2]])

full1 <- full[full[[5]]==6,]
full1
mean(full1[[4]])


full1 <- tabla[tabla[[5]]==6,]
full1
mean(full1[[4]])


full1 <- tabla[tabla[[5]]==5,]
full1
max(full1[[1]])


