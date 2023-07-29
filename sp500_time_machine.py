import os, sys, time
import datetime
import argparse
import statistics
import math

first_year = 1928 # This is the first year of data from the dataset
current_year = datetime.date.today().year # Grab this from the OS

# TODO Should I calculate based on monthly returns instead? How will this affect contributions and dividends?
# TODO Need to compile this data
#http://www.econ.yale.edu/~shiller/data.htm

# Year over year growth for the S&P 500 starting in 1928
# 	First data value is from 1928, 1929, ..., 2022
# 	https://www.macrotrends.net/2526/sp-500-historical-annual-returns
growth = [ 37.88, -11.91, -28.48, -47.07, -15.15,  46.59,  -5.94,  41.37,  27.92, -38.59, 
           25.21,  -5.45, -15.29, -17.86,  12.43,  19.45,  13.80,  30.72, -11.87,   0.00, 
           -0.65,  10.26,  21.78,  16.46,  11.78,  -6.62,  45.02,  26.40,   2.62, -14.31, 
           38.06,   8.48,  -2.97,  23.13, -11.81,  18.89,  12.97,   9.06, -13.09,  20.09, 
            7.66, -11.36,   0.10,  10.79,  15.63, -17.37, -29.72,  31.55,  19.15, -11.50, 
            1.06,  12.31,  25.77,  -9.73,  14.76,  17.27,   1.40,  26.33,  14.62,   2.03, 
           12.40,  27.25,  -6.56,  26.31,   4.46,   7.06,  -1.54,  34.11,  20.26,  31.01, 
           26.67,  19.53, -10.14, -13.04, -23.37,  26.38,   8.99,   3.00,  13.62,   3.53, 
          -38.49,  23.45,  12.78,   0.00,  13.41,  29.60,  11.39,  -0.73,   9.54,  19.42, 
           -6.24,  28.88,  16.26,  26.89, -18.26, 19.10]

# https://www.slickcharts.com/sp500/returns
# growth = [ 43.61, -8.42, -24.9, -43.34,  -8.19,  53.99,  -1.44, 47.67,  33.92, -35.03,
# 				   31.12, -0.41, -9.78, -11.59,  20.34,   25.9,  19.75, 36.44,  -8.07,   5.71, 
# 				     5.5, 18.79, 31.71,  24.02,  18.37,  -0.99,  52.62, 31.56,   6.56, -10.78, 
# 				   43.36, 11.96,  0.47,  26.89,  -8.73,   22.8,  16.48, 12.45, -10.06,  23.98, 
# 				   11.06,  -8.5,  4.01,  14.31,  18.98, -14.66, -26.47,  37.2,  23.84,  -7.18, 
# 				    6.56, 18.44, 32.42,  -4.91,  21.55,  22.56,   6.27, 31.73,  18.67,   5.25, 
# 				   16.61, 31.69,  -3.1,  30.47,   7.62,  10.08,   1.32, 37.58,  22.96,  33.36, 
# 				   28.58, 21.04,  -9.1, -11.89,  -22.1,  28.68,  10.88,  4.91,  15.79,   5.49,
# 				   -37.0, 26.46, 15.06,   2.11,   16.0,  32.39,  13.69,  1.38,  11.96,  21.83,
# 				   -4.38, 31.49,  18.4,  28.71, -18.11, 19.10]


# Different data set...I don't know why they are different...maybe dividends?
#   https://www.officialdata.org/us/stocks/s-p-500/
# growth = [ 43.81,  -8.3, -25.12, -43.84,  -8.64,  49.98, -1.19, 46.74, 31.94, -35.34, 
#            29.28,  -1.1, -10.67, -12.77,  19.17,  25.06, 19.03, 35.82, -8.43,    5.2, 
#              5.7,  18.3,  30.81,  23.68,  18.15,  -1.21, 52.56,  32.6,  7.44, -10.46, 
#            43.72, 12.06,   0.34,  26.64,  -8.81,  22.61, 16.42,  12.4, -9.97,   23.8, 
#            10.81, -8.24,   3.56,  14.22,  18.76, -14.31, -25.9,  37.0, 23.83,  -6.98, 
#             6.51, 18.52,  31.74,   -4.7,  20.42,  22.34,  6.15, 31.24, 18.49,   5.81, 
#            16.54, 31.48,  -3.06,  30.23,   7.49,   9.97,  1.33,  37.2, 22.68,   33.1, 
#            28.34, 20.89,  -9.03, -11.85, -21.97,  28.36, 10.74,  4.83, 15.61,   5.48, 
#           -36.55, 25.94,  14.82,    2.1,  15.89,  32.15, 13.52,  1.36, 11.96,  21.83, 
#            -4.38, 31.49,   18.4,  30.92, -18.26,  19.10]

# Given an initial investment, an annual contribution and a span in years, show how the investment would mature 
# based on historical trends of the S&P 500
def sp500_time_machine(starting_balance, span, annual_contribution):
	gain_list = []
	average_gain = 0
	total_years = (current_year - first_year - span) + 1

	# Calculate and store the data
	for j in range(total_years):
		principle = starting_balance
		index = 0
		index = index + j
		for i in range(span):
			principle = principle * (1 + growth[i + index] / 100) + annual_contribution
			principle = principle * 1.015 # dividend reinvestment of 1.5%
		gain_list.append(principle)
		print("S&P gain from %s to %s for %s starting balance = %s" % ((first_year + j), (first_year + j + span), f'{starting_balance:,}', f'{int(principle):,}'))
		average_gain = average_gain + principle

	# Display the average, minimum and maximum gain over the requested time span
	mean = int(average_gain / total_years)
	print("Average %s year gains over %d years is %s" % (span, total_years, f'{mean:,}'))

	# Calculate the standard deviation
	std_dev = statistics.stdev(gain_list)
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
	upper_interval = mean + 2.58 * (std_dev / math.sqrt(total_years))
	print("99%% Confidence Interval (Upper) = %s" % f'{int(upper_interval):,}')

	lower_interval = mean - 2.58 * (std_dev / math.sqrt(total_years))
	print("99%% Confidence Interval (Lower) = %s" % f'{int(lower_interval):,}')

	# Find the min/max values
	min_gain = min(gain_list)
	min_gain_index = gain_list.index(min_gain)
	print("Minimum gain over %d years occurred from %s to %s with a final balance of %s" % 
		(span, min_gain_index + first_year, min_gain_index + first_year + span, f'{int(min_gain):,}'))

	max_gain = max(gain_list)
	man_gain_index = gain_list.index(max_gain)
	print("Maximum gain over %d years occurred from %s to %s with a final balance of %s" % 
		(span, man_gain_index + first_year, man_gain_index + first_year + span, f'{int(max_gain):,}'))

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--span", help="The number of consecutive years (span) to iterate over")
	parser.add_argument("-p", "--principle", help="The initial investment amount")
	parser.add_argument("-a", "--annual", help="The annual contribution amount")
	args = parser.parse_args()

	sp500_time_machine(int(args.principle), int(args.span), int(args.annual))


