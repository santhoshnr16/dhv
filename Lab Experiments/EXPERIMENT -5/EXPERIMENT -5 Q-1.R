# Set 5 - Q1: Line chart of daily page views
date <- as.Date(c("2023-01-01","2023-01-02","2023-01-03","2023-01-04","2023-01-05"))
page_views <- c(1500, 1600, 1400, 1650, 1800)

plot(date, page_views, type = "o", col = "blue", lwd = 2, pch = 16,
     main = "Trend in Daily Page Views",
     xlab = "Date", ylab = "Page Views")
grid()