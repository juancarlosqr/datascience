getmonitor <- function(id, directory, summarize = FALSE) {
  ## 'id' is a vector of length 1 indicating the monitor ID
  ## number. The user can specify 'id' as either an integer, a
  ## character, or a numeric.
  
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'summarize' is a logical indicating whether a summary of
  ## the data should be printed to the console; the default is
  ## FALSE
  
  ## Your code here.
  idn <- as.integer(id) 
  
  file <- sprintf("%s/%003i.csv",directory,idn)
  
  mydata <- read.csv(file)
  
  if(summarize)
  {
    summ <- summary(mydata)
    print(summ)
  }
  return( mydata )
}


traceback()
getmonitor.testscript()
summary
data <- getmonitor(322,"specdata")
data <- getmonitor(101, "specdata", TRUE)
data



data <- getmonitor(1, "specdata") 
head(data)
data <- getmonitor(101, "specdata", TRUE)
head(data)
data <- getmonitor("200", "specdata", TRUE) 
