library(shiny)

ui <- fluidPage(
  titlePanel("Shiny R 테스트"),
  sidebarLayout(
    sidebarPanel(
      textInput(inputId = "in_caption",
                label="caption",
                value = "Data Summary"),
      selectInput(inputId="in_dataset",
                  label="Choose a dataset",
                  choices = c("v_rock", "v_pressure", "v_cars")),
      numericInput(inputId="in_obs",
                   label="Number....",
                   value=10),
      img(src="test.jpg", width=100, height=200)
      ),
    mainPanel(
      textOutput(outputId = "out_caption"),
      verbatimTextOutput(outputId = "out_summary"),
      tableOutput(outputId = "out_view")
    )
  )
)

server <- function(input, output, session) {
  datasetInput <- reactive({
    switch(input$in_dataset,
           "v_rock" = rock,
           "v_pressure" = pressure,
           "v_cars" = cars)
  })
  
  output$out_caption <- renderText({
    input$in_caption
  })
  
  output$out_summary <- renderPrint({
    dataset<-datasetInput()
    summary(dataset)
  })
  
  output$out_view <- renderTable({
    head(datasetInput(), n=input$in_obs)
  })
}

shinyApp(ui, server)
