from datetime import datetime, timedelta


class DatesBr:
    def __init__(self):
        self.register_time = datetime.today()

    def __str__(self):
        return self.br_format_data()

    def mont_register(self):
        year_months = [
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"
        ]

        year_month = self.mont_register.month - 1
        return year_months[year_month]

    def week_day(self):
        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        week_day = self.register_time.weekday()
        return week_days[week_day]

    def br_format_data(self):
        formated_data = self.register_time.strftime("%d/%m/%Y %H:%M")
        return formated_data
