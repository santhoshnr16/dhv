# Set 3 - Q1: Line chart of performance scores by employee, grouped by department
emp_id <- 1:5
department <- c("Sales", "HR", "Marketing", "Sales", "HR")
years_of_service <- c(5, 3, 7, 4, 2)
performance_score <- c(85, 92, 78, 90, 76)

plot(emp_id, performance_score, type = "o", col = "darkgreen", lwd = 2, pch = 16,
     main = "Employee Performance Trend",
     xlab = "Employee ID", ylab = "Performance Score",
     xaxt = "n", ylim = c(70, 100))
axis(1, at = emp_id, labels = emp_id)

legend("bottomright", legend = "Performance Score",
       col = "darkgreen", lty = 1, pch = 16, lwd = 2)