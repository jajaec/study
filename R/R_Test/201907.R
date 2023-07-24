#shiny����ϱ�
install.packages("shiny")
library(shiny)
ui<-fluidPage(
    sliderInput(inputId="num_1",
                label="���ڸ� ��������",
                value=25, min=1, max=80, step=1),
    plotOutput("hist")
)
server<-function(input, output) {
    output$hist <- renderPlot({
        title <- "80 random normal values "
        hist(rnorm(input$num_1),main=title)
    })
}
shinyApp(ui=ui, server=server)


install.packages("car")

searchpaths()
.libPaths()

help(package="shiny")