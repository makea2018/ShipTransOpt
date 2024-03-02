# Импорт библиотек
lapply(c("psych", "ggplot2",
         "gridExtra", "grid",
         "metan", "caret"), require, character.only = TRUE)

# =====================================================
#            EDA - Предобработка данных               #
# =====================================================
head(df)
str(df)

# =========================================
#            Удаление выбросов            #
# =========================================
# через Z-оценку
z_scores <- as.data.frame(sapply(df, z_score))

# Данные без выбросов через z-оценку
df_no_outliers <- df[!rowSums(sapply(z_scores, function (x) ifelse(x > 3, 1, 0))) > 1, ]
# Данные без выбросов через IQR диапазон
df_no_outliers <- df[!rowSums(sapply(df, find_IQR_stat)) > 1, ]

cat("До удаления выбросов, размер данных:", dim(df)[1], "x", dim(df)[2])
cat("После удаления выбросов, размер данных:", dim(df_no_outliers)[1], "x", dim(df_no_outliers)[2])


# =========================================
#     Приведение данных к нормальному     #
#             распределению               #
# =========================================
# Оставим только числовые данные + тип_судна в данных без выбросов
df_numeric_only <- cbind(df_no_outliers["vessel_type"], df_no_outliers[, sapply(df_no_outliers, is.numeric) == T])

colnames(df_numeric_only[, -1])
# Корреляция переменных до преобразования ряда переменных
# к более нормальному распределению
pairs.panels(df_numeric_only[, -1],
             stars=T, hist.col="steelblue",
             scale=T)
#=========================================================
# L
par(mfrow=c(1, 2))
# До преобразования
hist(df_numeric_only$L, main = paste("ДО\np value =", shapiro.test(df_numeric_only$L)$p.value),
     xlab = "L", ylab = "Количество",
     col=alpha("darkgreen", 0.7))
# После преобразования
hist(sqrt(df_numeric_only$L), main = paste("ПОСЛЕ\np value =", shapiro.test(sqrt(df_numeric_only$L))$p.value),
     xlab = "L", ylab = "Количество",
     col=alpha("darkgreen", 0.35))
cat("Распределение стало более нормальным")

#=========================================================
# B
par(mfrow=c(1, 2))
# До преобразования
hist(df_numeric_only$B, main = paste("ДО\np value =", shapiro.test(df_numeric_only$B)$p.value),
     xlab = "B", ylab = "Количество",
     col=alpha("blue", 0.7))
# После преобразования
hist(sqrt(df_numeric_only$B), main = paste("ПОСЛЕ\np value =", shapiro.test(sqrt(df_numeric_only$B))$p.value),
     xlab = "B", ylab = "Количество",
     col=alpha("blue", 0.35))
cat("Распределение не стало более нормальным, нет смысла использовать преобразование")

#=========================================================
# d
par(mfrow=c(1, 2))
# До преобразования
hist(df_numeric_only$d, main = paste("ДО\np value =", shapiro.test(df_numeric_only$d)$p.value),
     xlab = "d", ylab = "Количество",
     col=alpha("red", 0.7))
# После преобразования
hist(sqrt(df_numeric_only$d), main = paste("ПОСЛЕ\np value =", shapiro.test(sqrt(df_numeric_only$d))$p.value),
     xlab = "d", ylab = "Количество",
     col=alpha("red", 0.35))
cat("Распределение не стало более нормальным, нет смысла использовать преобразование")

#=========================================================
# DW
par(mfrow=c(1, 2))
# До преобразования
hist(df_numeric_only$DW, main = paste("ДО\np value =", shapiro.test(df_numeric_only$DW)$p.value),
     xlab = "DW", ylab = "Количество",
     col=alpha("pink", 0.7))
# После преобразования
hist(log10(df_numeric_only$DW), main = paste("ПОСЛЕ\np value =", shapiro.test(log10(df_numeric_only$DW))$p.value),
     xlab = "DW", ylab = "Количество",
     col=alpha("pink", 0.35))
cat("Распределение стало более нормальным")

#=========================================================
# speed
par(mfrow=c(1, 2))
# До преобразования
hist(df_numeric_only$speed, main = paste("ДО\np value =", shapiro.test(df_numeric_only$speed)$p.value),
     xlab = "speed", ylab = "Количество",
     col=alpha("yellow", 0.7))
# После преобразования
hist(sqrt(df_numeric_only$speed), main = paste("ПОСЛЕ\np value =", shapiro.test(sqrt(df_numeric_only$speed))$p.value),
     xlab = "speed", ylab = "Количество",
     col=alpha("yellow", 0.35))
cat("Распределение не стало более нормальным, нет смысла использовать преобразование")

#=========================================================
# cargo_amount
par(mfrow=c(1, 2))
# До преобразования
hist(df_numeric_only$cargo_amount, main = paste("ДО\np value =", shapiro.test(df_numeric_only$cargo_amount)$p.value),
     xlab = "cargo_amount", ylab = "Количество",
     col=alpha("grey", 0.7))
# После преобразования
hist(log10(df_numeric_only$cargo_amount), main = paste("ПОСЛЕ\np value =", shapiro.test(log10(df_numeric_only$cargo_amount))$p.value),
     xlab = "cargo_amount", ylab = "Количество",
     col=alpha("grey", 0.35))
cat("Распределение стало более нормальным")

#=========================================================
# cost_per_mile
par(mfrow=c(1, 2))
# До преобразования
hist(df_numeric_only$cost_per_mile, main = paste("ДО\np value =", shapiro.test(df_numeric_only$cost_per_mile)$p.value),
     xlab = "cost_per_mile", ylab = "Количество",
     col=alpha("orange", 0.7))
# После преобразования
hist(log10(df_numeric_only$cost_per_mile), main = paste("ПОСЛЕ\np value =", shapiro.test(log10(df_numeric_only$cost_per_mile+1))$p.value),
     xlab = "cost_per_mile", ylab = "Количество",
     col=alpha("orange", 0.35))
cat("Распределение стало более нормальным")

#=========================================================
# sea_route
par(mfrow=c(1, 2))
# До преобразования
hist(df_numeric_only$sea_route, main = paste("ДО\np value =", shapiro.test(df_numeric_only$sea_route)$p.value),
     xlab = "sea_route", ylab = "Количество",
     col=alpha("#993366", 0.7))
# После преобразования
hist(sqrt(df_numeric_only$sea_route), main = paste("ПОСЛЕ\np value =", shapiro.test(sqrt(df_numeric_only$sea_route))$p.value),
     xlab = "sea_route", ylab = "Количество",
     col=alpha("#993366", 0.35))
cat("Распределение стало более ненормальным")

#=========================================================
# target
par(mfrow=c(1, 2))
# До преобразования
hist(df_numeric_only$target, main = paste("ДО\np value =", shapiro.test(df_numeric_only$target)$p.value),
     xlab = "target", ylab = "Количество",
     col=alpha("#00CCCC", 0.7))
# После преобразования
hist(log10(df_numeric_only$target), main = paste("ПОСЛЕ\np value =", shapiro.test(log10(df_numeric_only$target+1))$p.value),
     xlab = "target", ylab = "Количество",
     col=alpha("#00CCCC", 0.35))
cat("Распределение стало более нормальным")


#===========================================
# Преобразование переменных к более нормальному распределению
df_transformed <- df_numeric_only[, -1]
df_transformed$L <- sqrt(df_transformed$L)
df_transformed$B <- sqrt(df_transformed$B)
df_transformed$d <- sqrt(df_transformed$d)
df_transformed$DW <- log10(df_transformed$DW)
df_transformed$speed <- sqrt(df_transformed$speed)
df_transformed$cargo_amount <- log10(df_transformed$cargo_amount)
df_transformed$cost_per_mile <- log10(df_transformed$cost_per_mile+1)
df_transformed$target <- log10(df_transformed$target+1)

# Корреляция переменных после преобразования ряда переменных
# к более нормальному распределению
pairs.panels(df_transformed,
             stars=T, hist.col="steelblue",
             scale=T)

# Проверка точности регрессионной модели до преобразования
summary(lm(target ~ ., data=df_numeric_only[, -1]))
# Проверка точности регрессионной модели после преобразования
summary(lm(target ~ ., data=df_transformed))

if (summary(lm(target ~ ., data=df_numeric_only[, -1]))$r.squared < summary(lm(target ~ ., data=df_transformed))$r.squared){
  print("Преобразование переменных к более нормальному виду дает прирост точности регрессионной модели")
} else {
  print("Преобразование переменных к более нормальному виду снижает точность модели")
}


# =========================================
#            Нормализация данных          #
# =========================================
# Нормализуем данные от 0 до 1
df_normalized <- predict(preProcess(df_numeric_only[, -1], method = c("range")), df_numeric_only[, -1])

# Визуализация числовых переменных
draw_all_hists(df_normalized)
