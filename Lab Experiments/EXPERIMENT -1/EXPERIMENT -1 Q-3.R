# Set 1 - Q3: Scatter plot - Advertising Budget vs Sales
ad_budget <- c(2000, 2500, 3200, 2800, 3500)   # sample data ($)
sales <- c(15000, 18000, 22000, 20000, 23000)

plot(ad_budget, sales,
     main = "Advertising Budget vs Monthly Sales",
     xlab = "Advertising Budget (in $)", ylab = "Sales (in $)",
     pch = 19, col = "darkred")
abline(lm(sales ~ ad_budget), col = "blue", lwd = 2)

correlation <- cor(ad_budget, sales)
cat("Correlation between Advertising Budget and Sales:", round(correlation, 3), "\n")

if (correlation < -0.5) {
  cat("Finding: There is a strong negative correlation between advertising budget and sales.\n")
  cat("This would suggest higher ad spend is associated with lower sales, which is unusual\n")
  cat("and may indicate other factors are influencing sales more strongly.\n")
} else if (correlation > 0.5) {
  cat("Finding: There is a strong positive correlation between advertising budget and sales.\n")
  cat("This suggests that increased advertising spend is associated with higher monthly sales,\n")
  cat("indicating advertising is likely an effective driver of revenue.\n")
} else {
  cat("Finding: There is a weak or negligible correlation between advertising budget and sales.\n")
  cat("This suggests advertising spend alone does not strongly explain changes in sales.\n")
}