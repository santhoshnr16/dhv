# Set 1 - Q2: Bar chart of top-selling products
products <- c("Product A","Product B","Product C","Product D","Product E")
product_sales <- c(45000, 38000, 52000, 30000, 41000)

barplot(product_sales, names.arg = products,
        main = "Top-Selling Products of the Year",
        xlab = "Product", ylab = "Sales (in $)",
        col = "steelblue", ylim = c(0, max(product_sales) + 5000))