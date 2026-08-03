# Set 2 - Q2: Pie chart of satisfaction scores
satisfaction <- c(4, 5, 3, 4, 5)

score_table <- table(satisfaction)
pct <- round(100 * score_table / sum(score_table), 1)
labels <- paste(names(score_table), " (", pct, "%)", sep = "")

pie(score_table, labels = labels,
    main = "Distribution of Customer Satisfaction Scores",
    col = rainbow(length(score_table)))