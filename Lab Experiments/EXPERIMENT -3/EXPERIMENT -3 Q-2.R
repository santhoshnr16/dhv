# Set 3 - Q2: Bar chart of employee count by department
department <- c("Sales", "HR", "Marketing", "Sales", "HR")

dept_table <- table(department)

barplot(dept_table,
        main = "Distribution of Employees Across Departments",
        xlab = "Department", ylab = "Number of Employees",
        col = "coral", ylim = c(0, max(dept_table) + 1))