# if
good <- F
if (good) {
  x <- 1
} else {
  x <- 0
}
x

# different syntax
good <- T
x <- if (good) {
  x <- 1
} else {
  x <- 0
}
x


# for
x <- c(1:6)

for (i in 1:6) {
  print(x[i])
}

for (i in seq_along(x)) {
  print(x[i])
}

for (number in x) {
  print(number)
}

for (i in 1:6)
  print(x[i])


# while
x <- 0
while (x < 10) {
  print(x)
  x <- x + 1
}

# repeat
x <- 1
repeat {
  print(x)
  if (x == 10) {
    break
  } else {
    x <- x + 1
  }
}


rm(x, i, good, number)
