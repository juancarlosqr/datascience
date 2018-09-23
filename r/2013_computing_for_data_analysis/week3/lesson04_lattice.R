
library(lattice)
library(nlme)
xyplot(distance ~ age | Subject, data = Orthodont)

?Orthodont

Orthodont

xyplot(distance ~ age | Subject, data = Orthodont, type = "b")