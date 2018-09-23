search()

make.power <- function(n) 
{
  pow <- function(x){
    x ^ n
  }
  pow
}

cube <- make.power(3)
cube(3)
square <- make.power(2)
square(4)

ls(environment(cube))
ls(environment(square))
ls(environment(make.power))

get("n", environment(square))
get("n", environment(cube))
get("pow", environment(square))


y <- 10

f <- function(x){
  y <- 2
  y^2 + g(x)
}

g <-function(x){
  x * y
}

f(3)