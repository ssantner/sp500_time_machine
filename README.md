# sp500_time_machine
Calculate Potential Future Returns with Confidence Intervals Based on Past Performance

The following example shows information related to historical gains on $100,000 over a 20 year span with a yearly investment of $0. Statistics (min/max/mean/stddev/confidence intervals) are displayed for futher analysis.
<pre>
| => python3 sp500_time_machine.py -s20 -p100000 -a0
S&P realized gains plus principle from 1928 to 1948 for 100,000 starting balance = 247,283
S&P realized gains plus principle from 1929 to 1949 for 100,000 starting balance = 238,257
S&P realized gains plus principle from 1930 to 1950 for 100,000 starting balance = 229,628
S&P realized gains plus principle from 1931 to 1951 for 100,000 starting balance = 232,921
S&P realized gains plus principle from 1932 to 1952 for 100,000 starting balance = 237,177
S&P realized gains plus principle from 1933 to 1953 for 100,000 starting balance = 259,943
S&P realized gains plus principle from 1934 to 1954 for 100,000 starting balance = 252,100
S&P realized gains plus principle from 1935 to 1955 for 100,000 starting balance = 237,304
S&P realized gains plus principle from 1936 to 1956 for 100,000 starting balance = 219,512
S&P realized gains plus principle from 1937 to 1957 for 100,000 starting balance = 221,292
S&P realized gains plus principle from 1938 to 1958 for 100,000 starting balance = 196,121
S&P realized gains plus principle from 1939 to 1959 for 100,000 starting balance = 194,446
S&P realized gains plus principle from 1940 to 1960 for 100,000 starting balance = 183,504
S&P realized gains plus principle from 1941 to 1961 for 100,000 starting balance = 175,968
S&P realized gains plus principle from 1942 to 1962 for 100,000 starting balance = 175,002
S&P realized gains plus principle from 1943 to 1963 for 100,000 starting balance = 176,248
S&P realized gains plus principle from 1944 to 1964 for 100,000 starting balance = 172,820
S&P realized gains plus principle from 1945 to 1965 for 100,000 starting balance = 160,797
S&P realized gains plus principle from 1946 to 1966 for 100,000 starting balance = 156,468
S&P realized gains plus principle from 1947 to 1967 for 100,000 starting balance = 153,825
S&P realized gains plus principle from 1948 to 1968 for 100,000 starting balance = 150,328
S&P realized gains plus principle from 1949 to 1969 for 100,000 starting balance = 172,890
S&P realized gains plus principle from 1950 to 1970 for 100,000 starting balance = 238,805
S&P realized gains plus principle from 1951 to 1971 for 100,000 starting balance = 236,219
S&P realized gains plus principle from 1952 to 1972 for 100,000 starting balance = 238,075
S&P realized gains plus principle from 1953 to 1973 for 100,000 starting balance = 228,877
S&P realized gains plus principle from 1954 to 1974 for 100,000 starting balance = 222,854
S&P realized gains plus principle from 1955 to 1975 for 100,000 starting balance = 215,961
S&P realized gains plus principle from 1956 to 1976 for 100,000 starting balance = 237,843
S&P realized gains plus principle from 1957 to 1977 for 100,000 starting balance = 269,290
S&P realized gains plus principle from 1958 to 1978 for 100,000 starting balance = 255,694
S&P realized gains plus principle from 1959 to 1979 for 100,000 starting balance = 275,148
S&P realized gains plus principle from 1960 to 1980 for 100,000 starting balance = 285,486
S&P realized gains plus principle from 1961 to 1981 for 100,000 starting balance = 345,102
S&P realized gains plus principle from 1962 to 1982 for 100,000 starting balance = 371,688
S&P realized gains plus principle from 1963 to 1983 for 100,000 starting balance = 396,966
S&P realized gains plus principle from 1964 to 1984 for 100,000 starting balance = 414,024
S&P realized gains plus principle from 1965 to 1985 for 100,000 starting balance = 399,360
S&P realized gains plus principle from 1966 to 1986 for 100,000 starting balance = 385,747
S&P realized gains plus principle from 1967 to 1987 for 100,000 starting balance = 432,459
S&P realized gains plus principle from 1968 to 1988 for 100,000 starting balance = 479,066
S&P realized gains plus principle from 1969 to 1989 for 100,000 starting balance = 486,597
S&P realized gains plus principle from 1970 to 1990 for 100,000 starting balance = 479,617
S&P realized gains plus principle from 1971 to 1991 for 100,000 starting balance = 516,310
S&P realized gains plus principle from 1972 to 1992 for 100,000 starting balance = 621,887
S&P realized gains plus principle from 1973 to 1993 for 100,000 starting balance = 712,978
S&P realized gains plus principle from 1974 to 1994 for 100,000 starting balance = 682,936
S&P realized gains plus principle from 1975 to 1995 for 100,000 starting balance = 863,969
S&P realized gains plus principle from 1976 to 1996 for 100,000 starting balance = 904,749
S&P realized gains plus principle from 1977 to 1997 for 100,000 starting balance = 893,162
S&P realized gains plus principle from 1978 to 1998 for 100,000 starting balance = 889,718
S&P realized gains plus principle from 1979 to 1999 for 100,000 starting balance = 1,161,107
S&P realized gains plus principle from 1980 to 2000 for 100,000 starting balance = 1,315,197
S&P realized gains plus principle from 1981 to 2001 for 100,000 starting balance = 1,549,834
S&P realized gains plus principle from 1982 to 2002 for 100,000 starting balance = 1,508,818
S&P realized gains plus principle from 1983 to 2003 for 100,000 starting balance = 1,005,679
S&P realized gains plus principle from 1984 to 2004 for 100,000 starting balance = 901,075
S&P realized gains plus principle from 1985 to 2005 for 100,000 starting balance = 1,021,626
S&P realized gains plus principle from 1986 to 2006 for 100,000 starting balance = 1,062,734
S&P realized gains plus principle from 1987 to 2007 for 100,000 starting balance = 1,140,779
S&P realized gains plus principle from 1988 to 2008 for 100,000 starting balance = 1,101,724
S&P realized gains plus principle from 1989 to 2009 for 100,000 starting balance = 1,232,099
S&P realized gains plus principle from 1990 to 2010 for 100,000 starting balance = 1,239,835
S&P realized gains plus principle from 1991 to 2011 for 100,000 starting balance = 1,064,738
S&P realized gains plus principle from 1992 to 2012 for 100,000 starting balance = 831,569
S&P realized gains plus principle from 1993 to 2013 for 100,000 starting balance = 685,242
S&P realized gains plus principle from 1994 to 2014 for 100,000 starting balance = 643,859
S&P realized gains plus principle from 1995 to 2015 for 100,000 starting balance = 681,265
S&P realized gains plus principle from 1996 to 2016 for 100,000 starting balance = 656,416
S&P realized gains plus principle from 1997 to 2017 for 100,000 starting balance = 749,858
S&P realized gains plus principle from 1998 to 2018 for 100,000 starting balance = 749,202
S&P realized gains plus principle from 1999 to 2019 for 100,000 starting balance = 745,687
S&P realized gains plus principle from 2000 to 2020 for 100,000 starting balance = 724,177
S&P realized gains plus principle from 2001 to 2021 for 100,000 starting balance = 690,102
S&P realized gains plus principle from 2002 to 2022 for 100,000 starting balance = 743,599
S&P realized gains plus principle from 2003 to 2023 for 100,000 starting balance = 761,311
Average 20 year realized gains plus principle over 76 years is 544,631
Standard Deviation = 371,518
99% Confidence Interval (Upper) = 654,580
99% Confidence Interval (Lower) = 434,681
Minimum realized gain plus principle over 20 years occurred from 1948 to 1968 with a final balance of 150,328
Maximum realized gain plus principle over 20 years occurred from 1981 to 2001 with a final balance of 1,549,834
</pre>
