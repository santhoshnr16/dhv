# Set 4 - Q3: Scatter plot - product price vs quantity available
product_name <- c("Product A","Product B","Product C","Product D","Product E")
quantity <- c(250, 175, 300, 200, 220)
price <- c(20, 35, 15, 28, 22)   # sample data ($)

plot(price, quantity,
     main = "Product Price vs Quantity Available",
     xlab = "Price (in $)", ylab = "Quantity Available",
     pch = 19, col = "brown")
abline(lm(quantity ~ price), col = "blue", lwd = 2)

# Calculate and print the correlation
correlation <- cor(price, quantity)
cat("Correlation between Price and Quantity Available:", round(correlation, 3), "\n")

# Auto-generated finding based on the correlation value
if (correlation < -0.5) {
  cat("Finding: There is a strong negative correlation between price and quantity available.\n")
  cat("This suggests that lower-priced products tend to be stocked in higher quantities,\n")
  cat("possibly because they have higher turnover or are prioritized for bulk inventory.\n")
} else if (correlation > 0.5) {
  cat("Finding: There is a strong positive correlation between price and quantity available.\n")
  cat("This suggests that higher-priced products are being stocked in larger quantities.\n")
} else {
  cat("Finding: There is a weak or negligible correlation between price and quantity available.\n")
  cat("This suggests that price alone does not strongly determine how much of a product is stocked.\n")
}