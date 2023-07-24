#read.table(
#    file="C:/Users/XKJR/Documents/업무관련/Workspaces/R/test.txt", 
#    header=TRUE,
#    sep=","
#)


save(iris, file="c:/20190722.RData")

load(file="c:/20190722.RData")

write.table(iris, file="C:/iris.txt", sep=",", row.names=TRUE)

write.csv(iris, file="C:/iris.csv", row.names=FALSE)

ls()

# 2019-07-23 
install.packages("ggplot2")

library(ggplot2)

diamonds
View(diamonds)

head(diamonds, n=10)
tail(diamonds, n=10)

diamonds[, c(2,3, 7), drop=FALSE]
diamonds[, 7:10]
diamonds[, seq(from=2, to=10, by=2)]

diamonds[, "cut", drop=FALSE]
diamonds[, c("cut", "price")]

diamonds[, grep("c", colnames(diamonds))]

colnames(diamonds)


diamonds[diamonds$cut == "Fair", ]

diamonds[diamonds$price >= 18000, ]

diamonds[(diamonds$cut == "Fair")|(diamonds$price >= 18000), ]

diamonds$xyz.sum = (diamonds$x+diamonds$y+diamonds$z)


diamonds[diamonds$price >= 18000, "price"] = 18000


diamonds[-c(10,20,30), ]

diamonds$table = NULL



subset(diamonds, select=-c(2,3))


diamonds[order(diamonds$cut, diamonds$color, decreasing = FALSE), ]

rowMeans()
