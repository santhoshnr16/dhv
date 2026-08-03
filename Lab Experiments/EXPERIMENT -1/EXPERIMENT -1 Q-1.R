# Set 1 - Q1: Line chart of monthly sales
months <- c("January","February","March","April","May")
sales <- c(15000,18000,22000,20000,23000)

# Keep month order correct (not alphabetical)
months <- factor(months, levels = months)

plot(months, sales, type = "n",
     main = "Monthly Sales Trend",
     xlab = "Month", ylab = "Sales (in $)")
lines(1:5, sales, type = "o", col = "blue", lwd = 2, pch = 16)
axis(1, at = 1:5, labels = months)
grid()