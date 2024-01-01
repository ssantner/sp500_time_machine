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

# Nice online calculator to see historical returns of ETF's
# https://dqydj.com/etf-return-calculator/

"""
Display the results of the statistical analysis of the historical realized gains of the S&P 500
"""
def sp500_display_results(analysis_results: list) -> None:
    print("Average %s year realized gains plus principle over %d years is %s" % (analysis_results["span_in_years"], analysis_results["gain_list_len"], f'{analysis_results["mean"]:,}'))
    print("Standard Deviation = %s" % f'{int(analysis_results["std_dev"]):,}')
    print("99%% Confidence Interval (Upper) = %s" % f'{int(analysis_results["upper_confidence_interval"]):,}')
    print("99%% Confidence Interval (Lower) = %s" % f'{int(analysis_results["lower_confidence_interval"]):,}')
    print("Minimum realized gain plus principle over %d years occurred from %s to %s with a final balance of %s" % 
        (analysis_results["span_in_years"], analysis_results["min_year"], analysis_results["min_year"] + analysis_results["span_in_years"], f'{int(analysis_results["min_gain_over_span"]):,}'))
    print("Maximum realized gain plus principle over %d years occurred from %s to %s with a final balance of %s" % 
        (analysis_results["span_in_years"], analysis_results["max_year"], analysis_results["max_year"] + analysis_results["span_in_years"], f'{int(analysis_results["max_gain_over_span"]):,}'))

"""
Return a dictionary containing relevant statistics from the historical realized gains
"""
def sp500_data_analysis(realized_gains: list, span_in_years: int):
    realized_gain_stats_dict = {}

    realized_gain_stats_dict["span_in_years"] = span_in_years

    """Determine the mean value"""
    mean = int(sum(realized_gains) / (len(realized_gains)))
    realized_gain_stats_dict.update({"mean":mean})

    """Calculate the standard deviation"""
    std_dev = statistics.stdev(realized_gains)
    realized_gain_stats_dict.update({"std_dev":std_dev})

    """Determine the 99% confidence interval
    
       Stock market returns are not normally distributed, so this is a simplification of actual real-world data
       https://klementoninvesting.substack.com/p/the-distribution-of-stock-market
       
       z-score values are based on normal distributions
       The value of 1.96 is based on the fact that 95% of the area of a normal distribution is within 1.96 standard deviations of the mean
       Likewise, 2.58 standard deviations contain 99% of the area of a normal distribution
       90% confidence z-value = 1.65
       95% confidence z-value = 1.96
       99% confidence z-value = 2.58"""
    upper_confidence_interval = mean + 2.58 * (std_dev / math.sqrt(len(realized_gains)))
    realized_gain_stats_dict.update({"upper_confidence_interval":upper_confidence_interval})

    lower_confidence_interval = mean - 2.58 * (std_dev / math.sqrt(len(realized_gains)))
    realized_gain_stats_dict.update({"lower_confidence_interval":lower_confidence_interval})

    """Find the min/max values"""
    min_gain_over_span = min(realized_gains)
    min_year = realized_gains.index(min_gain_over_span) + FIRST_YEAR
    realized_gain_stats_dict.update({"min_gain_over_span":min_gain_over_span})
    realized_gain_stats_dict.update({"min_year":min_year})

    max_gain_over_span = max(realized_gains)
    max_year = realized_gains.index(max_gain_over_span) + FIRST_YEAR
    realized_gain_stats_dict.update({"max_gain_over_span":max_gain_over_span})
    realized_gain_stats_dict.update({"max_year":max_year})

    realized_gain_stats_dict.update({"gain_list_len":len(realized_gains)})

    return realized_gain_stats_dict

"""
Return a list containing the historical gains of the S&P 500
"""
def sp500_historical_returns(starting_balance: int, span_in_years: int, annual_contribution: int, total_spans, dividend: float):
    realized_gain_list = []

    # Adjust the starting year for each span
    for base_year in range(total_spans):
        realized_gains = starting_balance
        # Loop through each span, month by month
        for month in range(span_in_years * MONTHS_PER_YEAR):
            realized_gains = (realized_gains + (annual_contribution / MONTHS_PER_YEAR)) * (1 + growth[month + base_year] / 100) + (realized_gains * dividend) / MONTHS_PER_YEAR

        # Store each realized gain over the requested span in a list for later processing
        realized_gain_list.append(realized_gains)
        print("S&P realized gains plus principle from %s to %s for %s starting balance = $%s" % ((FIRST_YEAR + base_year), (FIRST_YEAR + base_year + span_in_years), f'{starting_balance:,}', f'{int(realized_gains):,}'))

    return realized_gain_list

"""
Given an initial investment, an annual contribution and a span in years, show how the investment would mature based on historical trends of the S&P 500
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--principle", help="The initial investment amount", type=int)
    parser.add_argument("-s", "--span", help="The number of consecutive years (span) to iterate over", type=int)
    parser.add_argument("-a", "--annual", help="The annual contribution amount",type=int)
    parser.add_argument("-d", "--dividend", help="The dividend return as a percent",type=float)
    args = parser.parse_args()

    """Determine the total number of spans within the requested data set (years)"""
    total_spans = (datetime.date.today().year - FIRST_YEAR - args.span) + 1

    list_of_realized_gains = sp500_historical_returns(args.principle, args.span, args.annual, total_spans, args.dividend)
    stats_dictionary = sp500_data_analysis(list_of_realized_gains, args.span)
    sp500_display_results(stats_dictionary)

