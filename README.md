# Projects

## [Project: Algorithmic Trading Bots](https://github.com/Seniorveiga/CV/tree/main/Algorythmic%20Trading)
Ellaborating my own trading bots to operating in the stock market and the crypto market, which are my main interest.
Right now I´m developing more advanced bots in other areas such as Natural Language Processing. Meanwhile you can check my bot that trades based on **volume changes** and **price changes** in the pair **BTCUSDT**:

* Data has been extracted with the Yahoo! Finance package for Python called [Yfinance](https://pypi.org/project/yfinance/)
* For the data that is being streamed in real-time, you need to connect to [Binance](https://www.binance.com) and obtain the permissions for the **API keys**.
* It includes a [Blockchain data anlysis](https://github.com/Seniorveiga/CV/blob/main/Algorythmic%20Trading/2.prep_trading_strategy.ipynb) for this pair where I use to ackages **pandas**, **matplotlib** and **seaborn**, together with other fundamental packages such as **NumPy**, **datetime** and **timedelta**.
* You can go directly to the robot [here](https://github.com/Seniorveiga/CV/blob/main/Algorythmic%20Trading/3.trading_bot_LongOnlyTrader.ipynb). I will be preparing an updated version for short positions!

## [Project: Manual Trading and extraction to Excel in SP500](https://github.com/Seniorveiga/CV/tree/main/Strategies%20for%20Manual%20Trading%20in%20SP500%20-%20Approximation)
A brief introduction to the stock market operating system to give traders a spreadsheet to make some operations. It uses some uncommon packages such as the **xlsxwriter** to construct the Excel archives that will be sent to them. It includes:

* An equal weight distribution for the SP500 strategy [to enhance performance en smaller companies](https://github.com/Seniorveiga/CV/blob/main/Strategies%20for%20Manual%20Trading%20in%20SP500%20-%20Approximation/001_equal_weight_S%26P_500.ipynb)
* A momentum strategy dividing them in different sets, similar to the trading bot strategy above. YOu can have a look [here](https://github.com/Seniorveiga/CV/blob/main/Strategies%20for%20Manual%20Trading%20in%20SP500%20-%20Approximation/002_quantitative_momentum_strategy.ipynb)
* Lastly, a more conservative but solid strategy that is rooted in the fundamental analysis with KPIs such as the ROI, ROA or the total returns of the companies. [This project](https://github.com/Seniorveiga/CV/blob/main/Strategies%20for%20Manual%20Trading%20in%20SP500%20-%20Approximation/003_quantitative_value_strategy.ipynb) is a bit harder than the others due to missing data and transcryption of data types for the Excel.

## [Project: Pens and Printers Data Analysis on Sales](https://github.com/Seniorveiga/Pens_and_printers/blob/main/Workspace/pens_and_printers_case_study.ipynb)

The company Pens And Printers had a problem with their customer focus, so I analyze the projects oriented to brainstorming.
* Data was taken from the "product_sales.csv" archive.
* It includes the whole cleaning process of the dataset, with imputation of NaN values, standarization  and data quality improvement.
* For the questions that they asked me to solve, I used visualization with Seaborn and MatPlotLib.
* With pandas I performed both the Exploratory Data Analysis and the import & cleaning data processes.
* I used hypothesis tests and ANOVA tests to determine the best way to deploy offers and product sales in the company.

![](https://github.com/Seniorveiga/Python_Projects/blob/main/Pens%20and%20Printers/Presentation.png)

## [Project: The hypothesis testing Bible](https://github.com/Seniorveiga/Python_Projects/tree/main/Hypothesis%20Testing%20Bible)

I have prepared this document in order to help my colleagues with the concept of *hypothesis testing* with some Notebooks. I already have studied this concept during my degree and I master it in my third year so I thought I could help them!
* It is divided in three notebooks that are classified as:
  1. Hypothesis testing fundamentals
  2. Proportion tests
  3. Non-Parametric tests
* It explains what is hypothesis testing based on the concept **ELI5** from **Reddit**. You can check more about it on [the following link](https://www.reddit.com/r/explainlikeimfive/)
* It includes both the use in the mathematical way and in package way so it´s easily understandable from both perspectives.
* Data was taken from the feather files *"dem_votes_potus_12_16.feather"* and *"late_shipments.feather"*. You can find more information about them in the notebook *"hypothesis_testing_Python.ipynb"*.
* The main packages used are:
  * [Pandas](https://pandas.pydata.org/)
  * [Scipy](https://scipy.org/)
  * [Pingouin](https://pingouin-stats.org/build/html/index.html)
  * [Statsmodels](https://www.statsmodels.org/stable/index.html)
  * Other packages for imports or taking bootstrap samplings.
* The main test that you will learn in this packages are:
  * $\mathit{t}$-test.
  * Two-sample $\mathit{t}$-test.
  * $\mathit{z}$-Proportions test.
  * $\chi^{2}$ independence test.
  * $\chi^{2}$ goodness of fit test.
  * Wilcoxon test.
  * Wilcoxon-Mann-Whitney test.
  * Kruskal-Wallis test.
