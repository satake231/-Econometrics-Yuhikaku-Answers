x <- c(1, 5, 6, 7)
P <- c(1/5, 1/4, 3/10, 1/4)

Ex <- sum(x * P)
Var <- sum((x - Ex) ^ 2 * P )

df <- data.frame(Values=x, Possibility=P)

library(ggplot2)
ggplot(df, aes(x=Values, y=Possibility)) +
  geom_col()