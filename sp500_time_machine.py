import os, sys, time
import datetime
import argparse
import statistics
import math
from sp500_data import growth

MONTHS_PER_YEAR = 12
FIRST_YEAR = 1928 # This is the first year of data from the dataset

# Given an initial investment, an annual contribution and a span in years, show how the investment would mature 
# based on historical trends of the S&P 500
def sp500_time_machine(starting_balance, span, annual_contribution):
	realized_gain_list = []
	average_gain = 0
	current_year = datetime.date.today().year # Grab this from the OS
	total_spans = (current_year - FIRST_YEAR - span) + 1

	# Adjust the starting year for each span
	for base_year in range(total_spans):
		realized_gains = starting_balance
		# Loop through each span, month by month
		for month in range(span * MONTHS_PER_YEAR):
			realized_gains = (realized_gains + (annual_contribution / MONTHS_PER_YEAR)) * (1 + growth[month + base_year] / 100)

		# Store each realized gain over the requested span in a list for later processing
		realized_gain_list.append(realized_gains)
		print("S&P realized gains plus principle from %s to %s for %s starting balance = %s" % ((FIRST_YEAR + base_year), (FIRST_YEAR + base_year + span), f'{starting_balance:,}', f'{int(realized_gains):,}'))
		average_gain = average_gain + realized_gains

	# Display the average, minimum and maximum gain over the requested time span
	mean = int(average_gain / total_spans)
	print("Average %s year realized gains plus principle over %d years is %s" % (span, total_spans, f'{mean:,}'))

	# Calculate the standard deviation
	std_dev = statistics.stdev(realized_gain_list)
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
	upper_interval = mean + 2.58 * (std_dev / math.sqrt(total_spans))
	print("99%% Confidence Interval (Upper) = %s" % f'{int(upper_interval):,}')

	lower_interval = mean - 2.58 * (std_dev / math.sqrt(total_spans))
	print("99%% Confidence Interval (Lower) = %s" % f'{int(lower_interval):,}')

	# Find the min/max values
	min_gain = min(realized_gain_list)
	min_gain_index = realized_gain_list.index(min_gain)
	print("Minimum realized gain plus principle over %d years occurred from %s to %s with a final balance of %s" % 
		(span, min_gain_index + FIRST_YEAR, min_gain_index + FIRST_YEAR + span, f'{int(min_gain):,}'))

	max_gain = max(realized_gain_list)
	man_gain_index = realized_gain_list.index(max_gain)
	print("Maximum realized gain plus principle over %d years occurred from %s to %s with a final balance of %s" % 
		(span, man_gain_index + FIRST_YEAR, man_gain_index + FIRST_YEAR + span, f'{int(max_gain):,}'))

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--span", help="The number of consecutive years (span) to iterate over")
	parser.add_argument("-p", "--principle", help="The initial investment amount")
	parser.add_argument("-a", "--annual", help="The annual contribution amount")
	args = parser.parse_args()

	sp500_time_machine(int(args.principle), int(args.span), int(args.annual))


