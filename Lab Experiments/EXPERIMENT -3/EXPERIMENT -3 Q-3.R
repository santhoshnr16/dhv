# Set 3 - Q3: Scatter plot - years of service vs performance score
years_of_service <- c(5, 3, 7, 4, 2)
performance_score <- c(85, 92, 78, 90, 76)

plot(years_of_service, performance_score,
     main = "Years of Service vs Performance Score",
     xlab = "Years of Service", ylab = "Performance Score",
     pch = 19, col = "purple")
abline(lm(performance_score ~ years_of_service), col = "blue", lwd = 2)

correlation <- cor(years_of_service, performance_score)
cat("Correlation between Years of Service and Performance Score:", round(correlation, 3), "\n")

if (correlation < -0.5) {
  cat("Finding: There is a strong negative correlation between years of service and performance score.\n")
  cat("This suggests that employees with more years of service tend to have lower performance scores\n")
  cat("in this sample, indicating performance may depend more on individual factors than tenure alone.\n")
} else if (correlation > 0.5) {
  cat("Finding: There is a strong positive correlation between years of service and performance score.\n")
  cat("This suggests that longer-serving employees tend to perform better, possibly due to experience.\n")
} else {
  cat("Finding: There is a weak or negligible correlation between years of service and performance score.\n")
  cat("This suggests tenure alone does not strongly predict performance in this sample.\n")
}