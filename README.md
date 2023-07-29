# sp500_time_machine
Calculate Potential Future Returns with Confidence Intervals Based on Past Performance

The following example shows information related to historical gains on $100,000 over a 20 year span with a yearly investment of $0. Statistics (min/max/mean/stddev/confidence intervals) are displayed for futher analysis.
<pre>
| => python3 sp500_time_machine.py -s20 -p100000 -a0
S&P gain from 1928 to 1948 for 100,000 starting balance = 116,691
S&P gain from 1929 to 1949 for 100,000 starting balance = 84,082
S&P gain from 1930 to 1950 for 100,000 starting balance = 105,244
S&P gain from 1931 to 1951 for 100,000 starting balance = 179,203
S&P gain from 1932 to 1952 for 100,000 starting balance = 394,295
S&P gain from 1933 to 1953 for 100,000 starting balance = 519,438
S&P gain from 1934 to 1954 for 100,000 starting balance = 330,889
S&P gain from 1935 to 1955 for 100,000 starting balance = 510,160
S&P gain from 1936 to 1956 for 100,000 starting balance = 456,138
S&P gain from 1937 to 1957 for 100,000 starting balance = 365,923
S&P gain from 1938 to 1958 for 100,000 starting balance = 510,600
S&P gain from 1939 to 1959 for 100,000 starting balance = 563,001
S&P gain from 1940 to 1960 for 100,000 starting balance = 645,948
S&P gain from 1941 to 1961 for 100,000 starting balance = 739,893
S&P gain from 1942 to 1962 for 100,000 starting balance = 1,109,119
S&P gain from 1943 to 1963 for 100,000 starting balance = 869,992
S&P gain from 1944 to 1964 for 100,000 starting balance = 865,913
S&P gain from 1945 to 1965 for 100,000 starting balance = 859,598
S&P gain from 1946 to 1966 for 100,000 starting balance = 717,164
S&P gain from 1947 to 1967 for 100,000 starting balance = 707,237
S&P gain from 1948 to 1968 for 100,000 starting balance = 849,321
S&P gain from 1949 to 1969 for 100,000 starting balance = 920,361
S&P gain from 1950 to 1970 for 100,000 starting balance = 739,895
S&P gain from 1951 to 1971 for 100,000 starting balance = 608,174
S&P gain from 1952 to 1972 for 100,000 starting balance = 578,564
S&P gain from 1953 to 1973 for 100,000 starting balance = 598,492
S&P gain from 1954 to 1974 for 100,000 starting balance = 529,593
S&P gain from 1955 to 1975 for 100,000 starting balance = 256,652
S&P gain from 1956 to 1976 for 100,000 starting balance = 267,109
S&P gain from 1957 to 1977 for 100,000 starting balance = 310,135
S&P gain from 1958 to 1978 for 100,000 starting balance = 320,306
S&P gain from 1959 to 1979 for 100,000 starting balance = 234,464
S&P gain from 1960 to 1980 for 100,000 starting balance = 242,742
S&P gain from 1961 to 1981 for 100,000 starting balance = 314,641
S&P gain from 1962 to 1982 for 100,000 starting balance = 230,672
S&P gain from 1963 to 1983 for 100,000 starting balance = 300,169
S&P gain from 1964 to 1984 for 100,000 starting balance = 296,079
S&P gain from 1965 to 1985 for 100,000 starting balance = 265,756
S&P gain from 1966 to 1986 for 100,000 starting balance = 307,839
S&P gain from 1967 to 1987 for 100,000 starting balance = 405,989
S&P gain from 1968 to 1988 for 100,000 starting balance = 344,934
S&P gain from 1969 to 1989 for 100,000 starting balance = 360,120
S&P gain from 1970 to 1990 for 100,000 starting balance = 516,982
S&P gain from 1971 to 1991 for 100,000 starting balance = 482,586
S&P gain from 1972 to 1992 for 100,000 starting balance = 550,189
S&P gain from 1973 to 1993 for 100,000 starting balance = 497,040
S&P gain from 1974 to 1994 for 100,000 starting balance = 643,992
S&P gain from 1975 to 1995 for 100,000 starting balance = 902,213
S&P gain from 1976 to 1996 for 100,000 starting balance = 919,770
S&P gain from 1977 to 1997 for 100,000 starting balance = 928,339
S&P gain from 1978 to 1998 for 100,000 starting balance = 1,374,256
S&P gain from 1979 to 1999 for 100,000 starting balance = 1,722,512
S&P gain from 1980 to 2000 for 100,000 starting balance = 1,833,246
S&P gain from 1981 to 2001 for 100,000 starting balance = 1,309,815
S&P gain from 1982 to 2002 for 100,000 starting balance = 1,261,787
S&P gain from 1983 to 2003 for 100,000 starting balance = 842,547
S&P gain from 1984 to 2004 for 100,000 starting balance = 908,000
S&P gain from 1985 to 2005 for 100,000 starting balance = 975,965
S&P gain from 1986 to 2006 for 100,000 starting balance = 795,729
S&P gain from 1987 to 2007 for 100,000 starting balance = 788,787
S&P gain from 1988 to 2008 for 100,000 starting balance = 800,383
S&P gain from 1989 to 2009 for 100,000 starting balance = 438,003
S&P gain from 1990 to 2010 for 100,000 starting balance = 424,923
S&P gain from 1991 to 2011 for 100,000 starting balance = 512,873
S&P gain from 1992 to 2012 for 100,000 starting balance = 406,043
S&P gain from 1993 to 2013 for 100,000 starting balance = 440,832
S&P gain from 1994 to 2014 for 100,000 starting balance = 533,643
S&P gain from 1995 to 2015 for 100,000 starting balance = 603,723
S&P gain from 1996 to 2016 for 100,000 starting balance = 446,883
S&P gain from 1997 to 2017 for 100,000 starting balance = 407,048
S&P gain from 1998 to 2018 for 100,000 starting balance = 371,038
S&P gain from 1999 to 2019 for 100,000 starting balance = 274,639
S&P gain from 2000 to 2020 for 100,000 starting balance = 296,122
S&P gain from 2001 to 2021 for 100,000 starting balance = 383,120
S&P gain from 2002 to 2022 for 100,000 starting balance = 559,040
S&P gain from 2003 to 2023 for 100,000 starting balance = 596,319
Average 20 year gains over 76 years is 587,907
Standard Deviation = 342,569
99% Confidence Interval (Upper) = 689,289
99% Confidence Interval (Lower) = 486,524
Minimum gain over 20 years occurred from 1929 to 1949 with a final balance of 84,082
Maximum gain over 20 years occurred from 1980 to 2000 with a final balance of 1,833,246
</pre>
