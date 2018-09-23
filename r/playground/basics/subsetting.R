data <- read.csv("datasets/hw1_data.csv")

# 11 
# what are the column names of the dataset?
names(data)

# 12
# Extract the first 2 rows of the data frame and print them to the console. 
# What does the output look like?
data[1:2,]
head(data, n = 2)

# 13
# How many observations (i.e. rows) are in this data frame?
dim(data)
nrow(data)

# 14 
# Extract the last 2 rows of the data frame and print them to the console.
# What does the output look like?
data[c(nrow(data)-1, nrow(data)),]
tail(data, n = 2)

# 15
# What is the value of Ozone in the 47th row?
data[47, 1]

# 16
# How many missing values are in the Ozone column of this data frame?
missing <- is.na(data$Ozone)
length(data$Ozone[missing])

# 17
# What is the mean of the Ozone column in this dataset? 
# Exclude missing values (coded as NA) from this calculation.
mean(data$Ozone, na.rm = TRUE)

# 18
# Extract the subset of rows of the data frame 
# where Ozone values are above 31 and Temp values are above 90.
# What is the mean of Solar.R in this subset?

# # removing NA - option 1
# bad <- is.na(data)
# full <- data[!bad]
# str(full)
# rm(bad)
# 
# # removing NA - option 2
# full <- na.omit(data)
# str(full)

# removing NA - option 3 (best)
good <- complete.cases(data)
full <- data[good, ]
str(full)

temp <- full[full$Ozone > 31,]
temp <- full[full$Temp > 90,]
mean(temp$Solar.R)
rm(good, temp)

# 19
# What is the mean of "Temp" when "Month" is equal to 6?
temp <- full[full$Month == 6,]
temp
full[,1]
mean(temp$Temp)
rm(temp)

# 20
# What was the maximum ozone value in the month of May (i.e. Month = 5)?
temp <- full[full$Month == 5,]
max(temp$Ozone)
rm(temp)

