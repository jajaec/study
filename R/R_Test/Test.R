library("csv", lib.loc="C:/Program Files/R/R-3.6.0/library")

setwd("C:/Users/XKJR/Documents/업무관련")
dat<-read.csv(file="2016년+교통+사망사고+데이터.csv", header=T)

bar <- table(dat$발생지시도)
bar <- sort(bar, decreasing=T)
barplot(bar)



