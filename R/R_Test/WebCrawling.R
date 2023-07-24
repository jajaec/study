library(rvest)
library(wordcloud)
library(RColorBrewer)

#-------------------------------- address --------------------------------#
css = "a._sp_each_url._sp_each_title"
add = "https://search.naver.com/search.naver?&where=news&query=%EB%A1%9C%EC%96%84%ED%86%A0%ED%86%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=22&start="
add_number = which(11:5000 %% 10 ==1)[-1]; n = tail(add_number, 1)

#-------------------------------- title --------------------------------#
title = list()

for (i in add_number) {
  url = paste0(add, i)
  html = read_html(url)
  node = html_node(html, css)
  text = html_text(node)
  print(text)
  title[i] = list(text)
  print(i/n)
}

#-------------------------------- word --------------------------------#
title = title[which(!duplicated(title))]
title = sapply(title, function(x) { x = gsub("[^[:alnum:] ]", " ", x) } )
word = unlist(strsplit(unlist(title), " "))
word = word[word!=""]
tbls = table(word)

#-------------------------------- wordcloud --------------------------------#
col = brewer.pal(7, "Set2")
wordcloud(names(tbls), freq=tbls, random.order=F, colors=col, random.color=F)




