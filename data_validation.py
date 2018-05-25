import pandas as pd
import numpy as np
from time import strftime
import re
from datetime import datetime


def remove_whitespace(x):
    '''
    Helper function to remove any blank space from a string
    x: a string
    '''

    try:
        # remove spaces inside and outside of string
        x = "".join(x.split())

    except:
        pass
    return x


def standardize_date(the_date):
    """
    Standardizes a date
    :param the_date: the date to standardize
    :return formatted_date
    """
    global formatted_date

    # Convert what we have to a string, just in case
    the_date = str(the_date)

    # Handle missing dates, however pandas should have filled this in as missing
    if not the_date or the_date.lower() == "missing" or the_date == "nan":
        formatted_date = "MISSING"

    # 03/03/15
    try:
        formatted_date = str(datetime.strptime(the_date, '%m/%d/%y').strftime('%m/%d/%y'))
    except:
        pass

    # 03/03/2015
    try:
        formatted_date = str(datetime.strptime(the_date, '%m/%d/%Y').strftime('%m/%d/%y'))
    except:
        pass

    return formatted_date


def date_validation(date):
    try:
        match = re.search(r'\d{4}-\d{2}-\d{2}[T]\d{2}:\d{2}:\d{2}[+]\d{2}:\d{2}', date)
        match.group(0)
    except:
        match = "BAD_FORMAT"
    return match


'''
WRAP IN FUNCTION
# 1. Find Missing Values
 print("Checking CSV File...\n")
 print("Finding Missing Values...\n")
'''

def compile(date):
    try:
        if df.isnull().values.any():
            print('There are missing values in the file.\n')
            dx = np.where(pd.isnull(df))
            print(df.loc[df.iloc[dx].index, :])

        else:
            print('No values are missing. OK')
    except:
        pass

    try:
        for zip in df.zipCode:
            if len(str(zip)) <= 5:
                print('True')
            else:
                print('False')
    except:
        pass

    try:
        for country in df.Country:
            if len(str(country)) == 2:
                print('True')
            else:
                print('False')
    except:
        pass

    try:
        for state in df.State:
            if len(str(state)) == 2:
                print('True')
            else:
                print('False')
    except:
        pass



# if __name__ == '__main__':

df = pd.read_csv("test.csv")

# compile()
# Applies remove_whitespace() to the entire DF
df = df.applymap(remove_whitespace)
# Applies validate_date() to promiseDate column only
# df.primiseDate = df.primisedate.apply(standardize_date)
df.createDateTime = df.createDateTime.apply(compile)

print(df)  # debug
