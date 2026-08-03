# Set 2 - Q1: Histogram of customer ages
age <- c(25, 30, 35, 28, 40)

hist(age,
     main = "Distribution of Customer Ages",
     xlab = "Age", ylab = "Frequency",
     col = "lightblue", border = "black",
     breaks = 5)