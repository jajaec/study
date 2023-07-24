library(ggplot2)

sort(table(diamonds$clarity), decreasing=TRUE)


sort(round(prop.table(table(diamonds$cut)) * 100, digits = 1), decreasing = TRUE)

install.packages("prettyR")
library(prettyR)


prettyR::freq(diamonds$clarity, display.na = F)
