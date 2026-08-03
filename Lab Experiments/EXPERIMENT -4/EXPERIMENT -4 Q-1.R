# Set 4 - Q1: Bar chart of quantity available per product
product_name <- c("Product A","Product B","Product C","Product D","Product E")
quantity <- c(250, 175, 300, 200, 220)

barplot(quantity, names.arg = product_name,
        main = "Quantity Available by Product",
        xlab = "Product", ylab = "Quantity Available",
        col = "seagreen", ylim = c(0, max(quantity) + 50))