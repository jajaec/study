library(ggplot2)
summary(diamonds)
summary(diamonds$price)

str(diamonds)

by(diamonds$price, diamonds$cut, summary)



install.packages("psych")
library(psych)

describe(diamonds$price)

describe(diamonds$price, trim=0)

describeBy(diamonds$price, diamonds$cut)

diamonds[, c(1, 2:3)]

diamonds[, c(1, 5:10)]
describe(diamonds[, c(1, 5:10)])







# 교차표
table(diamonds$cut, diamonds$color)

# 전체 백분율
prop.table(table(diamonds$cut, diamonds$color)) * 100
# 행 백분율
prop.table(table(diamonds$cut, diamonds$color), margin=1) * 100
# 열 백분율
prop.table(table(diamonds$cut, diamonds$color), margin=2) * 100



install.packages("gmodels")
library(gmodels)

CrossTable(diamonds$cut, diamonds$color, 
           prop.r=TRUE, # 행 백분율
           prop.c=TRUE, # 열 백분율
           prop.t = TRUE, #전체백분율
           digits = 1
           )

# 막대 그래프
barplot(
  table(diamonds$cut, diamonds$color), 
  beside = TRUE,  # 묶음 (기본: 펼침)
  legend.text = levels(diamonds$cut), # 범례출력
  args.legend = list(x="topright")   # 범례 위치
)



plot(diamonds$carat, diamonds$price)

plot(diamonds[, c("x", "y", "z")])
pairs(diamonds[, c("x", "y", "z")])



install.packages("corrplot")
library(corrplot)


cor.result = cor(diamonds[, c("x", "y", "z")])

corrplot(cor.result, method = "circle")
corrplot(cor.result, method = "square")
corrplot(cor.result, method = "ellipse")
corrplot(cor.result, method = "number")
corrplot(cor.result, method = "shade")
corrplot(cor.result, method = "color")
corrplot(cor.result, method = "pie")

corrplot(cor.result, type = "full")
corrplot(cor.result, type = "upper")
corrplot(cor.result, type = "lower")



corrplot.mixed(cor.result)

corrplot.mixed(cor.result, lower="number", upper="circle")



install.packages("scatterplot3d")
library(scatterplot3d)

scatterplot3d(diamonds$x, diamonds$y, diamonds$z)

install.packages("rgl")
library(rgl)

# 회전도 가능
rgl::plot3d(diamonds$x, diamonds$y, diamonds$z)

install.packages("Rcmdr")
library(Rcmdr)

# 회전및 더 다양한 기능
scatter3d(diamonds$x, diamonds$y, diamonds$z)
