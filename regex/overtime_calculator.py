def otc(hours, weeks_worked):
    """
    A calculator that determines how many PTO days accrued using bonus hours
    :param hours: Extra hours worked per week
    :param weeks_worked: How many weeks worked at additional hours
    :return: None
    """

    hours_per_week = (hours * 5)  # How many bonus hours per week
    bonus_hours = weeks_worked * hours_per_week  # Total bonus hours for how many weeks worked
    pto_days = bonus_hours / 8  # PTO days accrued
    print(f"You will receive {pto_days} PTO days if you work {hours_per_week} extra hours per week.")


otc(7/5, 12)


def otc_days_wanted(days, weeks):
    """
    A calculator that determines how many hours extra needed to work per week to gain desired days of PTO
    :param days: Days of PTO desired
    :param weeks: Number of weeks until you would like the received PTO
    :return: None
    """
    days_to_pto_hours = days * 8
    hours_per_week = days_to_pto_hours / weeks
    print(f"You will need approximately an extra {round(hours_per_week, 2)} hours per week to receive {days} days of "
          f"pto")
    print(f"\tThat is approximately {round(hours_per_week / 5, 2)} hours per day.")


otc_days_wanted(10, 12)
