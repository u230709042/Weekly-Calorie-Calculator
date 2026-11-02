DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

ACTIVITY_MULTIPLIERS = {
    "low": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "heavy": 1.725,
}

KCAL_PER_KG = 7700  # Rough number of calories in 1 kg of body fat


def ask_choice(prompt, options):
    """Keep asking until the user types one of the allowed options."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in options:
            return answer
        print("You entered an invalid word\nPlease try again")


def ask_number(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        answer = input(prompt).strip()
        if answer.isdigit():
            return int(answer)
        print("You entered an invalid word\nPlease try again")


def average_calories():
    """Ask for the user's details and return their daily calorie requirement."""
    gender = ask_choice("Please enter your gender (male or female): ", ["male", "female"])
    weight = ask_number("Please enter your weight (kg): ")
    height = ask_number("Please enter your height (cm): ")
    age = ask_number("Please enter your age: ")
    activity = ask_choice(
        "Enter your activity level (low, light, moderate, heavy): ",
        ACTIVITY_MULTIPLIERS,
    )

    # Mifflin-St Jeor equation
    bmr = 10 * weight + 6.25 * height - 5 * age
    bmr += 5 if gender == "male" else -161

    return int(bmr * ACTIVITY_MULTIPLIERS[activity])


def calculate_week(daily_calorie):
    """Ask for each day's calories and return the total deficit for the week."""
    total_deficit = 0

    for day in DAYS:
        eaten = ask_number(f"Enter your daily calories for {day}: ")
        deficit = daily_calorie - eaten
        total_deficit += deficit
        print(f"Your calorie deficit for {day} is {deficit} calories.")

    return total_deficit


def main():
    daily_calorie = average_calories()
    print(f"\nYour average daily calorie requirement is {daily_calorie} calories.")

    while True:
        total_deficit = calculate_week(daily_calorie)
        print(f"\n\nYOUR TOTAL CALORIE DEFICIT IS {total_deficit}.")
        print(f"You lost about {total_deficit / KCAL_PER_KG:.2f} kilos")

        answer = ask_choice("\nWould you like to calculate next week's calories (yes/no): ", ["yes", "no"])
        if answer == "no":
            break

    print("\nThe program has ended :)")


if __name__ == "__main__":
    main()