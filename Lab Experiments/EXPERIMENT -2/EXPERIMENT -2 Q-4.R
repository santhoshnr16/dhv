# Set 2 - Q4: Word cloud from open-ended feedback
# Needs: wordcloud, tm (text mining) packages - install once
install.packages("wordcloud")
install.packages("tm")

library(wordcloud)
library(tm)

feedback <- c(
  "Great service and friendly staff",
  "Delivery was late but product quality is good",
  "Excellent support, very happy with the experience",
  "Product broke after a week, poor quality",
  "Fast delivery and great customer service"
)

corpus <- Corpus(VectorSource(feedback))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeWords, stopwords("english"))

wordcloud(corpus, min.freq = 1, scale = c(3, 0.5),
          colors = brewer.pal(8, "Dark2"), random.order = FALSE)