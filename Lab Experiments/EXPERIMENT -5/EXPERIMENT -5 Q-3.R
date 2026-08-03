# Set 5 - Q3: Stacked area chart of user interactions (base R, no packages needed)
date <- c("2023-01-01","2023-01-02","2023-01-03","2023-01-04","2023-01-05")
x <- 1:5   # numeric x-axis positions for the dates

likes    <- c(120,150,100,170,200)
shares   <- c(40,55,35,60,70)
comments <- c(25,30,20,35,45)

# Cumulative sums to stack the areas
comments_top <- comments
shares_top   <- comments + shares
likes_top    <- comments + shares + likes

plot(x, likes_top, type = "n",
     main = "Distribution of User Interactions Over Time",
     xlab = "Date", ylab = "Count", xaxt = "n",
     ylim = c(0, max(likes_top) + 20))
axis(1, at = x, labels = date)

# Draw stacked polygons from bottom to top
polygon(c(x, rev(x)), c(rep(0, 5), rev(comments_top)), col = "lightgreen", border = NA)
polygon(c(x, rev(x)), c(comments_top, rev(shares_top)), col = "lightblue", border = NA)
polygon(c(x, rev(x)), c(shares_top, rev(likes_top)), col = "lightcoral", border = NA)

legend("topleft", legend = c("Comments", "Shares", "Likes"),
       fill = c("lightgreen", "lightblue", "lightcoral"))