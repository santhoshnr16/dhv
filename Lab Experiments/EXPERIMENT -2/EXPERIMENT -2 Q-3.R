# Set 2 - Q3: Stacked bar chart - satisfaction by age group
customer_id <- 1:5
age <- c(25, 30, 35, 28, 40)
satisfaction <- c(4, 5, 3, 4, 5)

# Group ages into ranges
age_group <- cut(age, breaks = c(20, 30, 40, 50),
                  labels = c("21-30", "31-40", "41-50"))

# Build a table: rows = satisfaction score, columns = age group
tab <- table(satisfaction, age_group)

barplot(tab,
        main = "Customer Satisfaction Scores by Age Group",
        xlab = "Age Group", ylab = "Number of Customers",
        col = rainbow(nrow(tab)),
        legend.text = rownames(tab),
        args.legend = list(title = "Satisfaction Score", x = "topright"))