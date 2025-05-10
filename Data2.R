try(dev.off(), silent = TRUE)
graphics.off()
while (!is.null(dev.list())) dev.off()
rm(list = ls())

windows(width = 10, height = 6)
par(mar = c(6, 4, 4, 2))  # Set margins

rice_data <- data.frame(
  Region = c("NCR", "Region II", "Region III", "Region IV-A", "MIMAROPA",
             "Region V", "Region VI", "Region VII", "Region VIII", "Region IX",
             "Region X", "Region XII", "Region XIII", "BARMM"),
  Price = c(46.05, 52.31, 46.56, 41.18, 43.99, 44.33, 40.91, 46.74, 43.96,
            48.69, 51.10, 45.59, 56.60, 47.78)
)

barplot(rice_data$Price,
        names.arg = rice_data$Region,
        col = "blue",
        border = "white",
        main = "April 2025 Rice Premium Prices",
        ylab = "Price (PhP/kg)",
        las = 2,  
        ylim = c(0, 60))

grid(FALSE)
