#install.packages("XML")

library(httr)
library(XML)

web = GET('https://ridibooks.com/bestsellers/general?order=monthly')

web = htmlParse(web)

xpath1 = '//*[@id="page_bast"]/div[2]/div['
xpath2 = ']/div[2]/h3/a/span'

title = c()

for(i in 1:10) {
    xpath = paste0(xpath1, i+1, xpath2)
    x = xpathSApply(web, xpath, xmlValue)
    x = gsub("/n", "", x)
    x = gsub("  ", "", x)
    title[i] = x
}


