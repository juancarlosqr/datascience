homicides <- readLines("../datasets/homicides.txt")
homicides[1]
homicides[1000]
str(homicides)
length(homicides)

# start matching with regex
# shootings
length(grep("iconHomicideShooting",homicides))
length(grep("iconHomicideShooting|icon_homicide_shooting",homicides))
length(grep("Cause: shooting",homicides))
length(grep("Cause: [Ss]hooting",homicides))
length(grep("[Ss]hooting",homicides))

length(grep("[21]+ year[s]* old",homicides))
indices <- grep("[:,] 21 year(s)* old</dd>",homicides)
indices <- grep(", 21 year(s)* old</dd>",homicides)
homicides[indices]
homicides[1:50]

grep("[21]+ year[s]* old",homicides)
i <- grep("[Cc]ause: [Ss]hooting",homicides)
j <- grep("[Ss]hooting",homicides)
setdiff(i,j)
setdiff(j,i)
homicides[c(318,859)]
length(grep("[Cc]ause:",homicides))

i <- grep("[Cc]ause:",homicides)
j <- grep(".*",homicides)
length(j)
setdiff(j,i)
homicides[c( 212, 213, 236, 238, 515)]

r <- regexpr("<dd>[F|f]ound(.*?)</dd>", homicides[1:5])
regmatches(homicides[1:5],r)

x <- substr(homicides[1], 177, 177 + 33 - 1)
x
gsub("<dd>[F|f]ound on |</dd>","",x)


r <- regexec("<dd>[F|f]ound on (.*?)</dd>", homicides)
r
m <- regmatches(homicides, r)
m
dates <- sapply(m, function(x) x[2])
dates <- as.Date(dates, "%B %d, %Y")
dates
hist(dates, "month", freq = TRUE)
hist(dates, "year", freq = TRUE)

