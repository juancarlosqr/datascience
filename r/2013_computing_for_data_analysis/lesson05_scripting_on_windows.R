getRandom <- function()
  {
    x <- rnorm(100)
    mean(x)
  }

getSecond <- function(x)
{
  x <- rnorm(length(x))
}
getRandom() # not found
ls()
rm(x)
z <- getSecond(5)
z
source("x.R")

# summary 

summary(z)
str(z)