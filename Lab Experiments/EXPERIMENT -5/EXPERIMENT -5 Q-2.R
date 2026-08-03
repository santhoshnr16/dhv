# Set 5 - Q2: Bar chart of top N days by click-through rate
date <- c("2023-01-01","2023-01-02","2023-01-03","2023-01-04","2023-01-05")
ctr <- c(2.3, 2.7, 2.0, 2.4, 2.6)   # click-through rate in %

# Choose top N (e.g. top 3 days)
N <- 3
top_idx <- order(ctr, decreasing = TRUE)[1:N]
top_dates <- date[top_idx]
top_ctr <- ctr[top_idx]

barplot(top_ctr, names.arg = top_dates,
        main = paste("Top", N, "Days by Click-Through Rate"),
        xlab = "Date", ylab = "Click-Through Rate (%)",
        col = "tomato", ylim = c(0, max(top_ctr) + 1))