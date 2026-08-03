# Set 4 - Q2: Stacked bar chart - quantity by product category
product_name <- c("Product A","Product B","Product C","Product D","Product E")
quantity <- c(250, 175, 300, 200, 220)
category <- c("Electronics", "Clothing", "Electronics", "Grocery", "Clothing")

# Build a matrix: rows = product, columns = category
tab <- tapply(quantity, list(product_name, category), sum)
tab[is.na(tab)] <- 0

barplot(t(tab), beside = FALSE,
        main = "Product Quantity by Category",
        xlab = "Product", ylab = "Quantity Available",
        col = rainbow(ncol(tab)),
        legend.text = colnames(tab),
        args.legend = list(title = "Category", x = "topright"))