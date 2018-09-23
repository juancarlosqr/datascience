x <- list(a = 1:5, b = rnorm(10))

lapply(x, mean)

x <- 1:4
lapply(x, runif, min = 0, max = 10)


x <- matrix(rnorm(200), 20, 10)
x
apply(x, 2, mean)
# el segundo parametro es el MARGIN o el margen que se quiere mantener
# usar 1 si se quiere realizar la operacion sobre las filas
# y 2 si se quiere sobre las columnas
apply(x, 1, sum)

rowSums(x)
rowMeans(x)
colSums(x)
colMeans(x)


x <- matrix(rnorm(200), 20, 10)
apply(x, 1, quantile, probs = c(0.25, 0.75))

