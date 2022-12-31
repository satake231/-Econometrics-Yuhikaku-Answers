x <- c(0, 2, 3, 2, 5, 1, 5, 2, 4, 6)
y <- c(2, 5, 4, 3, 4, 3, 4, 3, 5, 7)

cova <- cov(x, y)

corr <- cor(x, y)

paste("covariance = ", cova)
paste("correlation = ", corr)