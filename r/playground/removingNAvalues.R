
# how to remove NA values
temp <- c(1, 4, 2, NA, 6, NA)

# method 1

# create a logical operator to check NA values
bad <- is.na(temp)

bad

#subset without the na values
temp[!bad]


# method 2

# use complete.cases function to check existing values in multiple things
# returns a logical vector of existing values for all objects

# complete.cases is good to removing NA values of data.frames

tempY <- c(NA, "a", "b", NA, NA, "c")

good <- complete.cases(temp, tempY)
good

temp[good]
tempY[good]

rm(temp, bad, tempY, good)
