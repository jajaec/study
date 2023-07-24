library(ggplot2)


diamonds$gprice = cut(diamonds$price, breaks=c(0, 5000, 10000, 15000, 20000))
diamonds$gprice = cut(diamonds$price, breaks=seq(from=0, to=20000, by=5000))

table(diamonds$gprice)

round(prop.table(table(diamonds$gprice)) * 100, digits = 1)

hist(diamonds$price)
hist(diamonds$price, breaks=seq(from=0, to=20000, by=5000))
hist(diamonds$price, breaks=10)

boxplot(diamonds$price)
boxplot(diamonds$price, range=1)
#           �����ڷ�       �����ڷ�
boxplot(diamonds$price ~ diamonds$cut)



# ------------------------------------------------------------

# ���
mean(diamonds$price, na.rm = TRUE)

age = c(10, 20, 20, 30)
mean(age, na.rm = TRUE)

# 5% ���� ���
mean(diamonds$price, trim = 0.05)

# ������ �߾Ӱ�
table(diamonds$price)[median(diamonds$price)]

index = which.max(table(diamonds$price))
which.max(table(age))

table(diamonds$price)[index]



library(prettyR)

Mode(diamonds$price)

range(diamonds$price)
diff(range(diamonds$price))

IQR