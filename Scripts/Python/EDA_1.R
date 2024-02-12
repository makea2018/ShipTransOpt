# Импорт библиотек
lapply(c("psych", "ggplot2", "gridExtra"), require, character.only = TRUE)


# =========================================================================
#       EDA - Понимание структуры и характеристик набора данных           #
# =========================================================================
# Чтение данных
df <- read.csv("Data/ship_voyages.csv", sep=",", header=T)[,-1]

# Вывод первых 5-ти строк данных
head(df, 5)

# Типы переменных в данных
df_classess <- data.frame(sapply(df, class))

# Размер данных
rows <- dim(df)[1]
cols <- dim(df)[2]

# Кол-во пропущенных значений для всех переменных
is_na_df <- data.frame(lapply(df, function (x) length(df[is.na(x) == T])))
if (sum(is_na_df) > 0) {
  print("В данных есть пропуски")
} else {
  print("В данных нет пропусков")
}

# Кол-во дубликатов в данных
if (sum(duplicated(df)) == 0) {
  print("В данных нет дубликатов")
} else {
  print("В данных есть дубликаты")
}

# Кол-во уникальных судов
cat("Данные представлены по", dim(unique(df[1]))[1], "разным судам")

# Описательные статистики df
df_describe_stats <- data.frame(describe(df, fast = T))[, 3:8]

# Описательные статистики для каждого судна
StatsByVesselType <- data.frame(describeBy(df, df$vessel_type))

# Переменные, которые следует привести к категориальному виду
colnames(df[, sapply(df, class) == 'character'])[-1]

# Приведение переменных 'chr' к категориальному виду 
# vessel_type
df$vessel_type <- factor(df$vessel_type)
#cargo_type
df$cargo_type <- factor(df$cargo_type)
# cargo_demand
df$cargo_demand <- factor(df$cargo_demand, levels = c("маленький", "большой"),
                          labels = c(0, 1))
# cargo_value
df$cargo_value <- factor(df$cargo_value, levels = c("обычный", "ценный", "очень ценный"),
                          labels = c(0, 1, 2))
# cargo_fragility
df$cargo_fragility <- factor(df$cargo_fragility,
                             levels = c("не хрупкий", "хрупкий"),
                             labels = c(0, 1))
# cargo_danger
df$cargo_danger <- factor(df$cargo_danger)

# wind_strength
df$wind_strength <- factor(df$wind_strength,
                             levels = c("штиль", "тихий ветер", "легкий ветер",
                                        "слабый ветер", "умеренный ветер", "свежий ветер",
                                        "сильный ветер", "крепкий ветер",
                                        "очень крепкий ветер", "шторм"),
                             labels = 0:9)
# sea_state
df$sea_state <- factor(df$sea_state, 
                       levels = c("полный штиль", "штиль", "очень слабое",
                                  "слабое", "умеренное", "значительное",
                                  "очень бурное", "сильное"),
                       labels = 0:7)

# wind_direction
df$wind_direction <- factor(df$wind_direction)

# Проверка типов переменных
str(df)

#=====================================================#
# Визуализация распределений переменных (гистограммы) #
#=====================================================#
draw_all_hists <- function(df){
  # Названия переменных
  vars_names <- colnames(df)
  # Сетка для графиков
  par(mfrow= c(3,3))
  
  # Построение графиков
  for (i in 1:(length(df) - 1)) {
    res <- shapiro.test(df[,i])$p.value
    hist(df[, i], col=alpha("blue", 0.5), ylab="Частота", xlab=vars_names[i],
         main="", freq = F)
    title(paste("p =", res), font.main=1,
          line=0.4)
  }
  
  # Название графика
  #title("Распределения числовых переменных", outer = T, line=-1.2)
}

# Построение всех распределений
draw_all_hists(df[, sapply(df, is.numeric) == T])

print("Все числовые переменные не имеют нормального распределения")

#=====================================================#
# Визуализация распределений категориальных данных    #
#=====================================================#
draw_all_bars <- function(df){
  # vessel_type
  plot_1 <- ggplot(df, aes(vessel_type)) +
    geom_bar(fill=alpha('#20B2AA', 1.0), stat = 'count')
  # cargo_type
  plot_2 <- ggplot(df, aes(x=reorder(cargo_type, cargo_type, function (x)length(x)))) +
    geom_bar(fill=alpha('#20B2AA', 1.0), stat = 'count') +
    coord_flip() +
    labs(x="cargo_type")
  # cargo_demand
  plot_3 <- ggplot(df, aes(cargo_demand)) +
    geom_bar(fill=alpha('#20B2AA', 1.0), stat = 'count')
  # cargo_value
  plot_4 <- ggplot(df, aes(cargo_value)) +
    geom_bar(fill=alpha('#20B2AA', 1.0), stat = 'count')
  # cargo_fragility
  plot_5 <- ggplot(df, aes(cargo_fragility)) +
    geom_bar(fill=alpha('#20B2AA', 1.0), stat = 'count')
  # cargo_danger
  plot_6 <- ggplot(df, aes(cargo_danger)) +
    geom_bar(fill=alpha('#20B2AA', 1.0), stat = 'count')
  # wind_strength
  plot_7 <- ggplot(df, aes(wind_strength)) +
    geom_bar(fill=alpha('#20B2AA', 1.0), stat = 'count')
  # sea_state
  plot_8 <- ggplot(df, aes(sea_state)) +
    geom_bar(fill=alpha('#20B2AA', 1.0), stat = 'count')
  # wind_direction
  plot_9 <- ggplot(df, aes(wind_direction)) +
    geom_bar(fill=alpha('#20B2AA', 1.0), stat = 'count')
  
  # Размещение графиков на сетке
  grid.arrange(plot_1, plot_2, plot_3,
               plot_4, plot_5, plot_6,
               plot_7, plot_8, plot_9,
               ncol=3)
  
}

# Построение всех барплотов для категор. переменных
draw_all_bars(df[, sapply(df, is.factor) == T])
