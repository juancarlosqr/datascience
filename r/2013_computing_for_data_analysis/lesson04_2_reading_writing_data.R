y <- data.frame(a = 1, b = "z")
y
# dput vacia en un archivo la estructura e informacion de un objeto R
# para su posterior reutilizacion
dput(y)
dput(y, file = "y.R")
# dget carga nuevamente el objeto desde un archivo
newY <- dget("y.R")
newY

# remover objetos de la memoria
rm(y)

x <- "foo"
x
# guardamos varios objetos a un archivo
dump(c("x", "y"), file = "data.R")
# los eliminamos
rm(y,x)
# luego los cargamos nuevamente en los objetos previamente borrados
source("data.R")
# y podemos acceder a ellos nuevamente por las variables
y
x

# podemos leer datos desde otras fuentes

# creamos la conexion
conn <- url("http://net.tutsplus.com", "r")
# cargamos la informacion
web <- readLines(conn)
# leemos la informacion
head(web)
tail(web)

dir()
getwd()

summary(y)
str(y)