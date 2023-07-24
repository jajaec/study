library(ggplot2)

mean(diamonds$price, na.rm=TRUE, trim=0.05)


median(diamonds$price)


index = which.max(table(diamonds$price))
table(diamonds$price)[index]

age = c(20, 20, 25, 17, 20)

# 빈도 계산하여 저장
table(age)
which.max(table(age))

install.packages("prettyR")
library(prettyR)

Mode(diamonds$price)


diff(c(0, 10, 20))

# 범위
diff(range(diamonds$price))

# 사분위수
# 제3사분위수에서 제1사분위수의 값을 뺀값
IQR(diamonds$price)

# 표본의 분산 
var(diamonds$price)
var(age)

# 표본의 표준편차
sd(diamonds$price)
sd(age)

# 중위수 절대편차
mad(diamonds$price)
mad(age)
