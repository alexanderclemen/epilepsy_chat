# This script is the logistic regression analysis.
library(tidyverse)
library(lmerTest)

# hardcode home
setwd('/home/alex/Documents/02_study/duesseldorf/MA_Linguistik/23_WS_Python/epilepsy_chat/scripts')

setwd('../data')
getwd()


########### logistic regression for all children ###############

df <- read.csv('cwe_all_selected.csv', sep = ';')
glimpse(df)

# recode vars
df$child_id <- as.factor(df$child_id)
df$gender <- as.factor(df$gender)
df$age_months <- as.integer(df$age_months)

# scale the predictors
df$nr_lines <- scale(df$nr_lines)
df$nr_words_per_line <- scale(df$nr_words_per_line)
df$retraction <- scale(df$retraction)
df$repetition <- scale(df$repetition)
df$unfilled_pause <- scale(df$unfilled_pause)
df$nonword <- scale(df$nonword)
df$filled_pause <- scale(df$filled_pause)
df$error <- scale(df$error)
df$nr_words <- scale(df$nr_words)
df$age_months <- scale(df$age_months)

# full models singular
m1 <- glmer(cwe_sick ~ retraction + unfilled_pause + error + nonword + filled_pause + nr_lines + nr_words_per_line + 
            (1|gender) + (1|child_id) + (1|age_months), family = binomial, data = df)
m2 <- glmer(cwe_sick ~ repetition + unfilled_pause + error + nonword + filled_pause + nr_lines + nr_words_per_line +
              (1|gender) + (1|child_id) + (1|age_months), family = binomial, data = df)

# stepwise model comparison
m1 <- glm(cwe_sick ~ retraction + unfilled_pause + error + nr_lines + nr_words_per_line, family = binomial, data = df)
m1_best <- step(m1)
m2 <- glm(cwe_sick ~ repetition + unfilled_pause + error + nr_lines + nr_words_per_line, family = binomial, data = df)
m2_best <- step(m2)

summary(m1_best)
summary(m2_best)


########### logistic regression for only chonic ###############

df <- read.csv('cwe_chronic_selected.csv', sep = ';')
glimpse(df)

# recode vars
df$child_id <- as.factor(df$child_id)
df$gender <- as.factor(df$gender)
df$age_months <- as.integer(df$age_months)

# scale the predictors
df$nr_lines <- scale(df$nr_lines)
df$nr_words_per_line <- scale(df$nr_words_per_line)
df$retraction <- scale(df$retraction)
df$repetition <- scale(df$repetition)
df$unfilled_pause <- scale(df$unfilled_pause)
df$nonword <- scale(df$nonword)
df$filled_pause <- scale(df$filled_pause)
df$error <- scale(df$error)
df$nr_words <- scale(df$nr_words)
df$age_months <- scale(df$age_months)

# glmer

# full models singular
m_chronic <- glmer(cwe_sick ~ repetition + unfilled_pause + error + nonword + filled_pause + nr_lines + nr_words_per_line +
              (1|gender) + (1|child_id) + (1|age_months), family = binomial, data = df)

# stepwise model comparison
m_chronic <- glm(cwe_sick ~ repetition + unfilled_pause + error + nr_lines + nr_words_per_line, family = binomial, data = df)
m_chronic_best <- step(m_chronic)
summary(m_chronic_best)


###########  logistic regression for new onset and matched peers ###############

df <- read.csv('cwe_newonset_selected.csv', sep = ';')
glimpse(df)

# recode vars
df$child_id <- as.factor(df$child_id)
df$gender <- as.factor(df$gender)
df$age_months <- as.integer(df$age_months)

# scale the predictors
df$nr_lines <- scale(df$nr_lines)
df$nr_words_per_line <- scale(df$nr_words_per_line)
df$retraction <- scale(df$retraction)
df$repetition <- scale(df$repetition)
df$unfilled_pause <- scale(df$unfilled_pause)
df$nonword <- scale(df$nonword)
df$filled_pause <- scale(df$filled_pause)
df$error <- scale(df$error)
df$nr_words <- scale(df$nr_words)
df$age_months <- scale(df$age_months)

# full models singular
m_newonset <- glmer(cwe_sick ~ retraction + unfilled_pause + error + nonword + filled_pause + nr_lines + nr_words_per_line + 
              (1|gender) + (1|child_id) + (1|age_months), family = binomial, data = df)

# stepwise model comparison and model output
m_newonset <- glm(cwe_sick ~ retraction + unfilled_pause + error + nr_lines + nr_words_per_line, family = binomial, data = df)
m_newonset_best <- step(m_newonset)
summary(m_newonset_best)
