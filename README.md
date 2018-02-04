# Portfolio-Construction-Models
This is just a framework of different Portfolio Construction Models. Those models require some data you will need feed in.
The main data is just the historical close prices although you can improve these basic models by adding some fundamental data
about the stocks you want to pick. 

Keep in mind that you have to adapt this code (the models you want to use) to your data or your program, the only purpose,
of this code is to simplify the writting of a quantitative trading system.

The most simplistic models are:

The equal weighted: that assigns the same weight for every stock.

The equal risk: that assigns the same risk for every stock, here you will need the risk for every stock it could be the
Standard Deviation for example.

The alpha driven model: that assigns the same amount of alpha*weight for every stock, here you will have to feed the alphas
that could possibly be the historical returns. You can choose to use other different alphas.

The alpha driven model with restrictions: here we apply a restriction of the maximum size of every position.

From here we find more complex models, such as the Markowitz with or without restrictions and the 
Black-Litterman without restrictions.

The Markowitz model creates a number of random portfolios and returns the returns, the volatility, the sharpe ratio and the 
weights of every portfolio. With that data afterwars you can choose wheter you want a low risk portfolio 
or a high sharpe ratio portfolio. There is also a variant that selects only the portfolios that satisfy the max size constraint


The Black-Litterman model has the same approach creating the porfolios but after that part it calculates the pi' or 
view_adjusted_equilibrium_excess_returns that depends on the trader's forecast, using some complex mathematical formulas
it calculates the optimal weights according to the forecast, the historical data and the risk free return. 
It returns the pi' number and  the weights.

If you want to know more about this model here you will find an interesting article about it: https://corporate.morningstar.com/ib/documents/MethodologyDocuments/IBBAssociates/BlackLitterman.pdf


