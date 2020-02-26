plt.savefig("PLOT_NAME.png")
plt.show
__________________________________________________
sns.countplot('VOL',data=var)
sns.scatterplot(x='HP',y='WT',data=var)
sns.pairplot(var)
sns.catplot(x="VOL", y="SP", data=var);
sns.heatmap(var)
sns.lmplot(data=var, x='HP', y='SP')
sns.clustermap(data=var)

import statsmodels.api as sm
sm.qqplot(var)
__________________________________________________
var.plot.bar(x='HP', y='VOL')
var.plot.barh(x='HP', y='VOL')
var.plot.box()
var.plot.density()
var.plot.hexbi(x='HP', y='VOL')
var.plot.kde(ind=None)
var.plot.line(x='HP', y='VOL')
var.plot.pie(x='HP', y='WT')
var.plot.scatter(x='HP', y='WT')
var.plot.area(x='HP',y='SP')
var.plot.hist(bins=10)
