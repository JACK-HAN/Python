import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

labels = ['Major Match', '']
sizes = [273, 727]
colors = ['#E2E2E2', '#6392BF']
explode = (0, 0.08)
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%',
        colors=colors, startangle=270, shadow=True)
# plt.savsfig('major-match-job.png',transparent=True)
plt.show()

# data from:
# https://libertystreeteconomics.newyorkfed.org/2013/05/do-big-cities-help-college-graduates-find-better-jobs.html
