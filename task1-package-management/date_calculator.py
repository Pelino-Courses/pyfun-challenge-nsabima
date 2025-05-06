import datetime

def diference(date1,date2):
 """
    Calculates the number of days between two dates.
    Parameters:
    - date1 (datetime.date): The first date.
    - date2 (datetime.date): The second date.
    Returns:
    - The difference in days between date1 and date2.
    """
 return(date2-date1).days
date1=input("please enter date 1(yyyy-mm-dd):")
date2=input("pleasea enter date 2(yyyy-mm-dd):")
try:
    date1=datetime.datetime.strptime(date1,"%Y-%m-%d").date()
    date2=datetime.datetime.strptime(date2,"%Y-%m-%d").date()
    print(diference(date1,date2))
except ValueError:
    print("Please enter date in the format yyyy-mm-dd")
    
