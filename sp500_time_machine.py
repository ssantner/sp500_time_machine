import argparse
import datetime
import math
import os
import statistics
import sys
import time

from sp500_data import growth

MONTHS_PER_YEAR = 12
FIRST_YEAR = 1928 # This is the first year of data from the dataset

realized_gain_list = []

# todo Have this function return a data structure which contains the analytical data, then create another function for printing out the information
def sp500_data_analysis(realized_gains: list, span_in_years: int) -> None:
    # Display the average, minimum and maximum gain over the requested time span
    mean = int(sum(realized_gains) / (len(realized_gains)))
    print("Average %s year realized gains plus principle over %d years is %s" % (span_in_years, len(realized_gains), f'{mean:,}'))

    """Calculate the standard deviation"""
    std_dev = statistics.stdev(realized_gains)
    print("Standard Deviation = %s" % f'{int(std_dev):,}')

    # Determine the 99% confidence interval
    #
    # Stock market returns are not normally distributed, so this is a simplification of actual real-world data
    # https://klementoninvesting.substack.com/p/the-distribution-of-stock-market
    # 
    # z-score values are based on normal distributions
    # The value of 1.96 is based on the fact that 95% of the area of a normal distribution is within 1.96 standard deviations of the mean
    # Likewise, 2.58 standard deviations contain 99% of the area of a normal distribution
    # 90% confidence z-value = 1.65
    # 95% confidence z-value = 1.96
    # 99% confidence z-value = 2.58
    upper_interval = mean + 2.58 * (std_dev / math.sqrt(len(realized_gains)))
    print("99%% Confidence Interval (Upper) = %s" % f'{int(upper_interval):,}')

    lower_interval = mean - 2.58 * (std_dev / math.sqrt(len(realized_gains)))
    print("99%% Confidence Interval (Lower) = %s" % f'{int(lower_interval):,}')

    # Find the min/max values
    min_gain = min(realized_gains)
    min_gain_index = realized_gains.index(min_gain)
    print("Minimum realized gain plus principle over %d years occurred from %s to %s with a final balance of %s" % 
        (span_in_years, min_gain_index + FIRST_YEAR, min_gain_index + FIRST_YEAR + span_in_years, f'{int(min_gain):,}'))

    max_gain = max(realized_gains)
    man_gain_index = realized_gains.index(max_gain)
    print("Maximum realized gain plus principle over %d years occurred from %s to %s with a final balance of %s" % 
        (span_in_years, man_gain_index + FIRST_YEAR, man_gain_index + FIRST_YEAR + span_in_years, f'{int(max_gain):,}'))

def sp500_historical_returns(starting_balance: int, span_in_years: int, annual_contribution: int, total_spans) -> None:
    # Adjust the starting year for each span
    for base_year in range(total_spans):
        realized_gains = starting_balance
        # Loop through each span, month by month
        for month in range(span_in_years * MONTHS_PER_YEAR):
            realized_gains = (realized_gains + (annual_contribution / MONTHS_PER_YEAR)) * (1 + growth[month + base_year] / 100)

        # Store each realized gain over the requested span in a list for later processing
        realized_gain_list.append(realized_gains)
        print("S&P realized gains plus principle from %s to %s for %s starting balance = $%s" % ((FIRST_YEAR + base_year), (FIRST_YEAR + base_year + span_in_years), f'{starting_balance:,}', f'{int(realized_gains):,}'))

"""Given an initial investment, an annual contribution and a span in years, show how the investment would mature based on historical trends of the S&P 500"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--principle", help="The initial investment amount", type=int)
    parser.add_argument("-s", "--span", help="The number of consecutive years (span) to iterate over", type=int)
    parser.add_argument("-a", "--annual", help="The annual contribution amount",type=int)
    args = parser.parse_args()

    """Determine the total number of spans within the requested data set (years)"""
    total_spans = (datetime.date.today().year - FIRST_YEAR - args.span) + 1

    sp500_historical_returns(args.principle, args.span, args.annual, total_spans)
    sp500_data_analysis(realized_gain_list, args.span)

