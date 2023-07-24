library(DBI)
library(odbc)

con <- dbConnect(odbc::odbc(), "as400", UID="CSPRO", PWD= rstudioapi::askForPassword("User Password"))

b2cstlh <- dbGetQuery(con, "SELECT * FROM DEVSAMPLE.B2CSTLH")

#table : 빈도
barplot(sort( table(diamonds$cut), decreasing = TRUE), 
        col="purple", 
        main="다이아몬드의 품질 현황", 
        ylab="빈도", 
        ylim=c(0, 30000))

barplot(sort( table(diamonds$cut), decreasing = FALSE), 
        col="purple", 
        main="다이아몬드의 품질 현황", 
        xlab="빈도", 
        xlim=c(0, 30000),
        horiz=TRUE)


install.packages("plotly")
library(plotly)

plotly::plot_ly(data=diamonds, 
                x=~levels(cut), 
                y=~table(cut), 
                type="bar")

ggplot(data=diamonds, 
       mapping = aes(x=cut)) +geom_bar()




pie(table(diamonds$cut),
    radius=0.9, # 크기
    init.angle = 30)    # 회전

plotly::plot_ly(data=diamonds, 
                values=~table(cut),
                levels= ~levels(cut),
                type="pie")

ggplot(data=diamonds, 
       aes(x="", fill=cut)) + geom_bar(width = 1) + coord_polar("y")