# Импорт библиотек
lapply(c("psych", "ggplot2", "gridExtra", "grid", "metan",
         "xtable", "stargazer"), require, character.only = TRUE)

# =====================================================
#           Проведение регрессионного анализа         #
#           (множественная линейная регрессия)        #
# =====================================================
# Вывод первых 3 строк df без выбросов и названия судов
head(df_no_outliers[, -1], 3)
# Типы данных df
str(df_no_outliers[, -1])

# Проверим оказываемый эффект на
# зависимую переменную от номинативных переменных
# 1. cargo_type=
cargo_type_effect <- lm(target ~ cargo_type,
                        df_no_outliers[, -1])
# Результаты регрессионного анализа для переменной cargo_type
summary(cargo_type_effect)

# Взаимодействие переменной cargo_type с другими числовыми переменными
cargo_type_numeric_vars <- lm(target ~ .,
                              cbind(df_no_outliers["cargo_type"], df_no_outliers[, sapply(df_no_outliers, is.numeric) == T]))
# Результаты регрессионного анализа для переменной wind_direction + numeric_vars
summary(cargo_type_numeric_vars)
#=============================================================
# 2. wind_direction
wind_direction_effect <- lm(target ~ wind_direction,
                            df_no_outliers[, -1])
# Результаты регрессионного анализа для переменной wind_direction
summary(wind_direction_effect)

# Взаимодействие переменной wind_direction с другими числовыми переменными
wind_dir_plus_numeric_vars <- lm(target ~ .,
                                 cbind(df_no_outliers["wind_direction"], df_no_outliers[, sapply(df_no_outliers, is.numeric) == T]))
# Результаты регрессионного анализа для переменной wind_direction + numeric_vars
summary(wind_dir_plus_numeric_vars)

#=============================================================
# 3. vessel_type
# Взаимодействие переменной vessel_type с другими числовыми переменными
vessel_type_plus_numeric_vars <- lm(target ~ .,
                                    cbind(df_no_outliers["vessel_type"], df_no_outliers[, sapply(df_no_outliers, is.numeric) == T]))
# Результаты регрессионного анализа для переменной vessel_type + numeric_vars
summary(vessel_type_plus_numeric_vars)


#==================================================#
# Удаление не информативных переменных из данных   #
#   (vessel_title, cargo_type, wind_direction)     #
#==================================================#
data <- df_no_outliers[!colnames(df_no_outliers) %in% c("vessel_title", "cargo_type", "wind_direction")]
# Типы переменных
str(data)
# Размер данных
dim(data)

#==================================================#
#           Построение и выбор наилучшей           #
#               регрессионной модели               #
#             (с номинативными переменными)        #
#==================================================#
# Модель в которой 0 предикторов
model_null <- lm(target ~ 1, data = data) # В данной модели есть только Intercept. Значение intercept - это просто среднее значение зависимой переменной
model_full <- lm(target ~ ., data = data) # В данной модели есть все 15 предикторов + target

scope <- list(lower=model_null, upper=model_full)
best_model <- step(model_null, scope, direction="forward")

# Информация о модели и предикторах в модели
summary(best_model)

# Экспорт результатов регрессионного анализа в html формат
stargazer(best_model, type = "html",
          title = "Результаты регрессионного анализа",
          dep.var.labels = "target",
          covariate.labels = c("cargo\\_amount", "cargo\\_value1", "cargo\\_value2", 
                               "cost\\_per\\_mile", "cargo\\_fragility1", "cargo\\_demand1",
                               "cargo\\_demand1", "cargo\\_danger2", "cargo\\_danger3",
                               "cargo\\_danger4", "cargo\\_danger6", "cargo\\_danger8",
                               "cargo\\_danger9", "sea\\_route", "B", "L"),
          out = "RA_results_1.html")

#==================================================#
#       Построение и выбор наилучшей               #
#           регрессионной модели                   #
#     (номинативные переменные как числовые)       #
#==================================================#
# Данные только с числовыми переменными (номинативные переведены в числовой тип)
data_numeric <- data.frame(lapply(cbind(as.numeric(data$vessel_type), data[-1]), function(x) as.numeric(as.character(x))))
names(data_numeric)[names(data_numeric)=="as.numeric.data.vessel_type."] <- "vessel_type"
# Модель в которой 0 предикторов
model_null_2 <- lm(target ~ 1, data = data_numeric) # В данной модели есть только Intercept. Значение intercept - это просто среднее значение зависимой переменной
model_full_2 <- lm(target ~ ., data = data_numeric) # В данной модели есть все 15 предикторов + target

scope_2 <- list(lower=model_null_2, upper=model_full_2)
best_model_2 <- step(model_null_2, scope_2, direction="forward")

# Информация о модели и предикторах в модели
summary(best_model_2)

# Экспорт результатов регрессионного анализа в html формат
stargazer(best_model_2, type = "html",
          title = "Результаты регрессионного анализа",
          dep.var.labels = "target",
          covariate.labels = c("cargo\\_amount", "cargo\\_value", "cost\\_per\\_mile",
                               "cargo\\_fragility", "cargo\\_demand", "cargo\\_danger",
                               "vessel\\_type", "sea\\_route", "B", "L"),
          out = "RA_results_2.html")
