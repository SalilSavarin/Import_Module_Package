import application
import datetime 



if __name__ == '__main__':
    date_now = datetime.date.today()
    print(date_now)
    application.calculate_salary()
    application.get_employees()
    print(dir(application))