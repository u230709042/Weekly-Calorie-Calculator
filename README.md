# Weekly Calorie Calculator

A simple command-line program that estimates how many calories you need each day, then tracks your calorie deficit over a week and shows roughly how much weight that adds up to.

## Features

- Calculates your daily calorie requirement from your gender, weight, height, age, and activity level
- Asks what you ate each day, Monday through Sunday, and shows the daily deficit as you go
- Adds up the weekly deficit and estimates how many kilos it equals
- Lets you track as many weeks in a row as you like, without re-entering your details
- Checks every input and asks again if something doesn't look right

## How It Works

**1. Daily calorie requirement.** The program uses the Mifflin-St Jeor equation to estimate your basal metabolic rate (BMR), then multiplies it by an activity factor:

```
Men:    BMR = 10 × weight (kg) + 6.25 × height (cm) − 5 × age + 5
Women:  BMR = 10 × weight (kg) + 6.25 × height (cm) − 5 × age − 161
```

| Activity level | Multiplier |
|----------------|------------|
| low            | 1.2        |
| light          | 1.375      |
| moderate       | 1.55       |
| heavy          | 1.725      |

**2. Daily and weekly deficit.** For each day, the deficit is your daily requirement minus the calories you actually ate. A negative number simply means you ate more than you need that day.

**3. Estimated weight change.** The total weekly deficit is divided by 7,700, which is roughly the number of calories in 1 kg of body fat.

## Getting Started

You only need Python 3.6 or newer. There are no extra packages to install.

```bash
https://github.com/u230709042/Weekly-Calorie-Calculator.git
cd Weekly-Calorie-Calculator
python weekly_calorie_calculator.py
```