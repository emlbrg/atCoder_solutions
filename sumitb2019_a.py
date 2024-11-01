"""A - November 30
url: https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_a
"""

from datetime import datetime
from calendar import monthrange

def is_last_day_of_month(m1, d1):
    date = datetime(year=2019, month=m1, day=d1)

    last_day = monthrange(date.year, date.month)[1]

    return d1 == last_day

m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

if is_last_day_of_month(m1, d1):
    print(1)
else:
    print(0)
