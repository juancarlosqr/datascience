initial <- read.csv("datasets/gapminder.csv")
attach(initial)
# 1.  "country"
# 2.  "incomeperperson"
# 3.  "alcconsumption"
# 4.  "armedforcesrate"
# 5.  "breastcancerper100th"
# 6.  "co2emissions"
# 7.  "femaleemployrate"
# 8.  "hivrate"
# 9.  "internetuserate"
# 10. "lifeexpectancy"
# 11. "oilperperson"
# 12. "polityscore"
# 13. "relectricperperson"
# 14. "suicideper100th"
# 15. "employrate"
# 16. "urbanrate"
str(initial)
head(initial, n = 10)
initial[initial$country == "Venezuela", c("country", "lifeexpectancy", "polityscore")]
dimnames(initial)
head(initial[order(lifeexpectancy,polityscore),c(1, 10, 12)], n = 20)
nrow(initial)
row.names(initial)

good <- complete.cases(initial)
full <- initial[good, ]
