x <- rnorm(10)
x
x <- rnorm(10,20,2)
x
summary(x)


x <- rnorm(10)
print(x)
x <- rnorm(10, 20, 2)
print(x)
summary(x)


# important for reproduce a simulation is always set the same seed
set.seed(2)
rnorm(5)

rpois(10,1)


set.seed(20)
x <- rnorm(100)
e <- rnorm(100, 0, 2)
y <- 0.5 + 2 * x + e
summary(y)
plot(x,y)

# exercise

e <- rnorm(100, 0, 1)
x <- 1:100 
y <- 1.5 - 3 * x + e
plot(x,y)

# binary

set.seed(10)
x <- rbinom(100,1,0.5)
e <- rnorm(100, 0, 2)
y <- 0.5 + 2 * x + e
summary(y)
plot(x,y)

# poisson model

set.seed(1)
x <- rnorm(100)
log.mu <- 0.5 + 0.3 * x
y <- rpois(100, exp(log.mu))
summary(y)
plot(x,y)

# sampling

set.seed(1)
sample(1:10, 4)

# permutation
sample(1:10)

# replacement
sample(1:10, 4, replace = TRUE)

