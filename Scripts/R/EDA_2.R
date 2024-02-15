# Импорт библиотек
lapply(c("psych", "ggplot2", "gridExtra", "grid"), require, character.only = TRUE)

# =====================================================
#       EDA - Выявление аномалий и выбросов           #
# =====================================================
# Чтение данных
df <- read.csv("Data/ship_voyages.csv", header = T)[, -1]

# Конвертирование кат. переменных в корректный вид
df <- convert_to_factor(df)
# Проверка типов данных
str(df)

# Удалим колонку с названием судов (vessel_title)
dfNoTitles <- df[, cbind(2:length(df))]

#===================================================#
#         Обнаружение выбросов (z-оценка)           #
#===================================================#
# Функция для расчета z-статистики
z_score <- function(x){
  if (class(x) != "numeric"){
    x <- rep(1, length(x))
    part_down <- 1
  } else {
    part_down <- sd(x)
  }
  
  part_top <- x - mean(x)
  return (abs(part_top / part_down))
}
z_scores <- as.data.frame(sapply(df, z_score))
# Функция для подсчета кол-ва значений, которые > 3σ
count_z_more_than_3sd <- function(df, val=3){
  col_names <- colnames(df)
  for (i in 1:length(col_names)){
    cat(col_names[i], "=", sum(sapply(df[, i], function (x) x >= val)), "\n")
  }
}
# Вывод кол-ва значений в каждой переменной превышающей 3σ
count_z_more_than_3sd(z_scores)

# Выбросы в данных через z-оценку
no_outliers_z_score <- z_scores[!rowSums(sapply(z_scores, function (x) ifelse(x > 3, 1, 0))) > 1, ]
cat("Кол-во выбросов через z-оценку =", dim(z_scores[rowSums(sapply(z_scores, function (x) ifelse(x > 3, 1, 0))) > 1, ])[1])

# Визуализация кол-ва выбросов в каждой переменной через z-оценку
z_scores_ForVisual_df <- as.data.frame(sapply(as.data.frame(sapply(z_scores, function (x) x > 3)), sum)); colnames(z_scores_ForVisual_df) <- "count"
z_scores_ForVisual_df <- subset(z_scores_ForVisual_df, count != 0)
ggplot(z_scores_ForVisual_df, aes(x=row.names(z_scores_ForVisual_df), y=z_scores_ForVisual_df$count)) + 
  geom_bar(stat = "identity", fill="#FDD0FF") + 
  labs(y="Количество", x="Переменные", title = "Кол-во выбросов в переменных через z-оценку") + 
  theme(plot.title = element_text(hjust = 0.5, face="bold",
                                  size=16),
        axis.title.x = element_text(size=12),
        axis.title.y = element_text(size=12))


#===================================================#
#   Обнаружение выбросов (Межквартильный диапозон)  #
#===================================================#
find_IQR_stat <- function (x) {
  if (class(x) == "numeric") {
    IQR_ <- IQR(x)
    top <- quantile(x, 0.75) + 1.5*IQR_
    low <- quantile(x, 0.25) - 1.5*IQR_
    return (ifelse(x > top | x < low, 1, 0))
  } else {
    return (rep(0, length(x)))
  }
}

# Построение вспом. данных по условию
no_outliers_IQR_stat <- df[!rowSums(sapply(df, find_IQR_stat)) > 1, ]
cat("Кол-во выбросов через IQR-диапозон =", dim(df[rowSums(sapply(df, find_IQR_stat)) > 1, ])[1])

# Визуализация кол-ва выбросов в каждой переменной через IQR-диапозон
IQR_stat_ForVisual_df <- as.data.frame(sapply(as.data.frame(sapply(df, find_IQR_stat)), sum)); colnames(IQR_stat_ForVisual_df) <- "count"
IQR_stat_ForVisual_df <- subset(IQR_stat_ForVisual_df, count != 0)
ggplot(IQR_stat_ForVisual_df, aes(x=row.names(IQR_stat_ForVisual_df), y=IQR_stat_ForVisual_df$count)) + 
  geom_bar(stat = "identity", fill="#4CCD8D") + 
  labs(y="Количество", x="Переменные", title = "Кол-во выбросов в переменных через IQR-диапозон") + 
  theme(plot.title = element_text(hjust = 0.5, face="bold",
                                  size=16),
        axis.title.x = element_text(size=12),
        axis.title.y = element_text(size=12))


#===================================================#
#       Обнаружение выбросов (Визуализация)
#             через Boxplot
#===================================================#
df_numeric_only <- cbind(df["vessel_type"], df[, sapply(df, is.numeric) == T])
# Функция для построения графиков "Ящик с усами"
draw_all_boxplots <- function (df, col, title="") {
  
  # Графики
  # L
  plot_1 <- ggplot(df, aes(y=L)) + 
    geom_boxplot(fill=col) + 
    labs(x= "L",
         y= "")
  # B
  plot_2 <- ggplot(df, aes(y=B)) + 
    geom_boxplot(fill=col) + 
    labs(x= "B",
         y= "")
  # d
  plot_3 <- ggplot(df, aes(y=d)) + 
    geom_boxplot(fill=col) + 
    labs(x= "d",
         y= "")
  # DW
  plot_4 <- ggplot(df, aes(y=DW)) + 
    geom_boxplot(fill=col) + 
    labs(x= "DW",
         y= "")
  # speed
  plot_5 <- ggplot(df, aes(y=speed)) + 
    geom_boxplot(fill=col) + 
    labs(x= "speed",
         y= "")
  # cargo_amount
  plot_6 <- ggplot(df, aes(y=cargo_amount)) + 
    geom_boxplot(fill=col) + 
    labs(x= "cargo_amount",
         y= "")
  # cost_per_mile
  plot_7 <- ggplot(df, aes(y=cost_per_mile)) + 
    geom_boxplot(fill=col) + 
    labs(x= "cost_per_mile",
         y= "")
  # sea_route
  plot_8 <- ggplot(df, aes(y=sea_route)) + 
    geom_boxplot(fill=col) + 
    labs(x= "sea_route",
         y= "")
  # target
  plot_9 <- ggplot(df, aes(y=target)) + 
    geom_boxplot(fill=col) + 
    labs(x= "target",
         y= "")
  
  # Размещение графиков на сетке
  grid.arrange(plot_1, plot_2, plot_3,
               plot_4, plot_5, plot_6,
               plot_7, plot_8, plot_9,
               ncol=3, top = textGrob(title,
                                      gp=gpar(fontsize=16,font=2)))
}

# График для всех числовых переменных (не учитывая тип судна)
draw_all_boxplots(df_numeric_only[, -1], col = "#88b63a",
                  title="Визуализация выбросов")

# График для всех числовых переменных (только "сухогруз")
draw_all_boxplots(subset(df_numeric_only, vessel_type=="сухогруз")[, -1], col = alpha("blue", 0.5),
                  title="Визуализация выбросов для сухогрузов")

# График для всех числовых переменных (только "танкер")
draw_all_boxplots(subset(df_numeric_only, vessel_type=="танкер")[, -1], col = alpha("pink", 0.7),
                  title="Визуализация выбросов для танкеров")
