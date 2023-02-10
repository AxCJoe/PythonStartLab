#import datetime
#date_a = datetime.date(1989,9,12)
#date_b = datetime.date(2020,2,19)
#days_c = date_b - date_a
#type(days_c)
#   print(days_c)

import datetime
date_a = datetime.date(1989,9,12)
date_b = datetime.date.today()
days_c = date_b - date_a
print(days_c)