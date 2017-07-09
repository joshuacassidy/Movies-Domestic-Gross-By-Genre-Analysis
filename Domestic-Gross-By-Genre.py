import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movieData = pd.read_csv('Data.csv', encoding = 'latin1')
genre_filters = ['action', 'adventure','animation','comedy','drama' ]
movieFilters = movieData[movieData.Genre.isin(genre_filters)]
data = movieFilters[(movieFilters.Studio == 'Buena Vista Studios') | (movieFilters.Studio == 'Fox') | (movieFilters.Studio == 'Paramount Pictures') | (movieFilters.Studio == 'Sony') | (movieFilters.Studio == 'Universal') | (movieFilters.Studio == 'WB')]

ax = plt.subplot()

sns.boxplot(data=data, x='Genre', y='Gross % US',orient='v',  showfliers=False)

sns.stripplot(data=data, x='Genre', y='Gross % US',jitter=True,size=6, linewidth=0, hue = 'Studio', alpha=0.5)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)

plt.show()