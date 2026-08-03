# Set 1 - Q4: Enhanced Interactive Dashboard
library(tcltk)

months <- c("January","February","March","April","May")
sales <- c(15000,18000,22000,20000,23000)
products <- c("Product A","Product B","Product C","Product D","Product E")
product_sales <- c(45000, 38000, 52000, 30000, 41000)

draw_dashboard <- function(n_months, highlight_product) {
  par(mfrow = c(1, 2))
  
  # Line chart
  plot(1:n_months, sales[1:n_months], type = "o", col = "blue", lwd = 2, pch = 16,
       xaxt = "n", main = "Monthly Sales Trend",
       xlab = "Month", ylab = "Sales (in $)",
       xlim = c(1, 5), ylim = c(0, max(sales) + 2000))
  axis(1, at = 1:5, labels = months)
  
  # Bar chart with highlighted product
  bar_colors <- rep("steelblue", length(products))
  bar_colors[products == highlight_product] <- "darkorange"
  barplot(product_sales, names.arg = products,
          main = "Top-Selling Products", xlab = "Product", ylab = "Sales (in $)",
          col = bar_colors)
  
  par(mfrow = c(1, 1))
  
  # Update total sales label
  total <- sum(sales[1:n_months])
  tkconfigure(total_label, text = paste("Total Sales (selected months): $", total))
}

# --- Build the Tk window ---
tt <- tktoplevel()
tkwm.title(tt, "Sales Dashboard")

tkgrid(tklabel(tt, text = "Select number of months to display:"))
month_choice <- tclVar("5")
slider <- tkscale(tt, from = 1, to = 5, orient = "horizontal", variable = month_choice,
                   command = function(...) {
                     draw_dashboard(as.numeric(tclvalue(month_choice)), tclvalue(product_choice))
                   })
tkgrid(slider)

tkgrid(tklabel(tt, text = "Highlight a product:"))
product_choice <- tclVar("Product A")
product_menu <- tk2combobox <- ttkcombobox(tt, textvariable = product_choice, values = products, state = "readonly")
tkgrid(product_menu)
tkbind(product_menu, "<<ComboboxSelected>>", function(...) {
  draw_dashboard(as.numeric(tclvalue(month_choice)), tclvalue(product_choice))
})

reset_btn <- tkbutton(tt, text = "Reset", command = function() {
  tclvalue(month_choice) <- "5"
  tclvalue(product_choice) <- "Product A"
  draw_dashboard(5, "Product A")
})
tkgrid(reset_btn)

total_label <- tklabel(tt, text = "Total Sales (selected months): $")
tkgrid(total_label)

draw_dashboard(5, "Product A")  # initial view