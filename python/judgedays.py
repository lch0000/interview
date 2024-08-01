# 输入年月日，判断这个日期是这一年的第几天
def is_leap_year(year):
    '''判断制定的年份是不是闰年，平年返回False，闰年返回True'''
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    '''一段传入的日期是这一年的第几天'''
    # 用嵌套的列表保存平年和闰年每个月的天数
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]
    days = days_of_month[is_leap_year(year)][0:month - 1]
    return sum(days) + date

print(which_day(2024, 2, 12))

# 使用标准库来判断
import datetime

def which_day(year, month, date):
    end = datetime.date(year, month, date)
    start = datetime.date(year, 1, 1)
    return (end - start).days + 1

print(which_day(2024, 2, 12))