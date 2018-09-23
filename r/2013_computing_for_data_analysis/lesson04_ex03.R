file1 <- "datasets/number_of_policies_by_program_by_state_feb_2012.csv"
tablePolicies <- read.csv(file1)
# la columna de nombre y totales
tablePolicies[,c(1,8)]
# longitud de columnas
length(tablePolicies)
# cantidad de columnas
ncol(tablePolicies)
# cantidad de filas
nrow(tablePolicies)
# la suma de los totales
sum(tablePolicies[c(1:nrow(tablePolicies)-1),8])
# extraer solo cifras y sin ultima columnas de totales
cifras <- tablePolicies[c(1:nrow(tablePolicies)-1),c(2:8)]
cifras
# calculando los totales para cada columna, en este caso
# no lo hace, solo columna por columna
totales <- c(sum(cifras[,2]))
totales
tablePolicies[59,3]

###

tablePolicies[c(1:nrow(tablePolicies)-1),8]
totalRate <- c(tablePolicies[c(1:nrow(tablePolicies)-1),8])
totalRate
str(totalRate)
states <- tablePolicies[c(1:nrow(tablePolicies)-1),1]
#states <- factor(c(tablePolicies[c(1:nrow(tablePolicies)-1),1]))
states
str(states)
barplot(totalRate)
names(totalRate) <- states
barplot(totalRate)
mean(totalRate)
abline(h = mean(totalRate))
abline(h = median(totalRate))
under <- totalRate[totalRate < median(totalRate)]
under
barplot(under)
length(under)
upper <- totalRate[totalRate > median(totalRate)]
upper
length(upper)
barplot(upper)
plot(totalRate,states)
plot(states,totalRate)
###
vesselsSunk <- c(4, 5, 1)
str(vesselsSunk)
barplot(vesselsSunk)

barplot(1:100)