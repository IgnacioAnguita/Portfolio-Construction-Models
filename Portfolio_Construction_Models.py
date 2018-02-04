#Portfolio construction models

###################### By Ignacio Anguita Espadaler ########################

import numpy as np 
import pandas as pd

#Variables we suppose we only go short or long
Name_of_the_position =[] #name of the position
Positions=[] #positions we want to open
Type_of_the_position=[]#long or short
Risk=[] #risk of every positions
Alpha_expected=[] #alpha expected for every position
Weight_Position=[] #how big is going to be every position
Volatility=[]#volatility of every position
Position_Sector= [] #the sector of every position
position_constraint = 0.03 #constraint about the max size of a position
sector_constraint= 0.2 #constraint about the max size of the positions open in a sector


#for the more complex portfolios
Data=[] #all the data of the price stocks
data=pd.DataFrame(data=Data) #all the data converted into a panda data frame
returns = data.pct_change() #calculation of the change
mean_daily_returns = returns.mean() #calculation of the daily mean
cov_matrix = returns.cov() #calculation of the covariance matrix
num_portfolios=20000 #number of combinations, the more combinations the more opportunities to find an optimal combination
time_frame=200 #number of days of our time frame
Volatility=[]#volatility of every position
Market_capitalization_weights=[] #the name is really descriptive
Market_capitalization_weights_np=np.array(Market_capitalization_weights)
rf=0.03 #risk free ratio
P_original=[0,0]#Vector of views about asset returns
P=np.array(P_original) 
Q=np.zeros((len(P_original),len(Positions))) #we put zeros because this is just a frameworks we don't have any perspectives views
 #Matrix linking views to the portfolio assets

#these array is for the Markowitz model
results=np.zeros((3+len(Positions),num_portfolios))#in this results array the first will be the expected returns of the portfolio, the second array the 
#volatility of the portfolio and the third row is the sharpe ratio and the other are the weights for each position


########################################## Simple Models #################################################



def equal_weighting(Positions): #equally weighted
	return 1/len(positions)



def equal_risk_weighting(Risk): #same level of risk for every position
	Total_Risk=0
	i=0
	Weight_Position=[] #how big is going to be every position
	while i<=len(Risk): #calculation of the total risk
		Total_Risk=Risk(i)+Total_Risk
		i=i+1
	average_Risk=Total_Risk/len(Risk) #calculation of the average risk
	i=0
	while i<=len(Risk): #calculation of the weight of every position in order to have the same risk
		Weight_Position.append=average_Risk/(Risk(i)*len(Risk))
		i=i+1
	return Weight_Position



def alpha_driven_weighting_simple(Alpha_expected):
	Total_alpha=0
	Weight_Position=[] #how big is going to be every position
	i=0
	while i<=len(Alpha_expected): #calculation of the total alpha
		Total_alpha=Alpha_expected(i)+Total_alpha
		i=i+1
	i=0
	while i<=len(Alpha_expected): #calculation of the weights
		Weight_Position.append=Alpha_expected(i)/Total_alpha
		i=i+1


		
def alpha_driven_weighting_with_constraints(Alpha_expected,position_constraint,sector_constraint):
	Total_alpha=0
	Weight_Position=[] #how big is going to be every position
	i=0
	Excessive_Weight_Positions=[]
	while i<=len(Alpha_expected): #calculation of the total alpha
		Total_alpha=Alpha_expected(i)+Total_alpha
		i=i+1
	i=0
	while i<=len(Alpha_expected): #calculation of the weights
		Weight_Position.append=Alpha_expected(i)/Total_alpha
		i=i+1
	#now we apply the constraint
	j=0
	while j<=100: # we will limit the size and then recalculate the weights, some will be overweighted, so in order to compensate it we will repeat the process a big amount of time until everything is correctly weighted

		i=0
		while i<=len(Alpha_expected):
			if Weight_Position(i)>position_constraint:
				Weight_Position[i]=position_constraint				
			i=i+1
		i=0
		TotaL_Weight=0
		while i<=len(Alpha_expected):
			Total_Weight=Total_Weight+Weight_Position(i)
		i=0
		while i<=len(Alpha_expected):
			Weight_Position[i]=Weight_Position(i)+(1-Total_Weight)/len(Alpha_expected)
		j=j+1
	return Weight_Position


############################################# Markowitz Models ##################################################################################




#markowitz models these make a lot of different portfolios and let you choose the best combination, they are not optimized using a function for that


def Markowitz_portfolio_simple (mean_daily_returns,cov_matrix,num_portfolios,results,Positions,time_frame):
	for i in xrange(num_portfolios):
		weights = np.array(np.random.random(len(Positions))) #here we create random weight for each position
		weights /= np.sum(weights) #we convert the weights to a number from 0 to 1
		portfolio_return = np.sum(mean_daily_returns * weights) * time_frame #we calculate the expected return in a time frame
		portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights))) * np.sqrt(time_frame) #we calculate the volatility in a time frame
 
    	#We store the results in the results matrix
		results[0,i] = portfolio_return #first the portfolio return
		results[1,i] = portfolio_std_dev #then the volatility
		results[2,i] = results[0,i] / results[1,i] #the sharpe ratio (return/volatility)
		for j in range(len(weights)):
			results[j+3,i] = weights[j] #here we store the weights
	return results 

def Constraint_selection_max_sharpe_Markowitz_simple(position_constraint,mean_daily_returns,cov_matrix,num_portfolios,results,Positions,time_frame):
	Markowitz_portfolio_simple (mean_daily_returns,cov_matrix,num_portfolios,results,Positions,time_frame) #we get the values for the Markowitz model
	#first we find the ones that satisfy the constraint
	Max_size=False
	i=0
	for i in xrange(num_portfolios):
		j=0
		while j<=xrange(Positions) and Max_size==False: #here we apply the constrain condition, if the position is bigger than the constrain it will ot go to the list
			if results[3+j,i]>position_constraint:
				Max_size=True
			else:
				j=j+1
		if Max_size==False:
			np.append(results_correct,results[:,i]) #here we put the correct positions
		Max_size=False
	return results_correct





######################################################## Black Litterman Model ######################################################################




#Black-Litterman Model, the also calculates different portfolios and then you choose one, using the criteria you prefer 

#this first model has no constraints

def Black_Litterman_portfolio_model_simple(mean_daily_returns,cov_matrix,num_portfolios,results,Positions,time_frame,Market_capitalization_weights_np,rf,P,Q): 
	results_Black_Litterman=np.zeros((1+len(Positions),num_portfolios))#here we will store all the results
	for i in xrange(num_portfolios):
		weights = np.array(np.random.random(len(Positions))) #here we create random weight for each position
		weights /= np.sum(weights) #we convert the weights to a number from 0 to 1
		portfolio_return = np.sum(mean_daily_returns * weights) * time_frame #we calculate the expected return in a time frame
		portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights))) * np.sqrt(time_frame) #we calculate the volatility in a time frame
		#until here everything is similar to the Markowitz model, here starts the Black-Litterman part
		
		Risk_return_trade_off=(portfolio_return-rf)/(portfolio_std_dev)#calculation of the risk return trade off 
		pi=Risk_return_trade_off*cov_matrix*Market_capitalization_weights #calculation of the Equilibrium excess returns
		Thau=0.025 #this is just a constant
		Omega=np.dot(Thau,P,cov_matrix,P.transpose()) #calculation of the uncertain matrix
		view_adjusted_equilibrium_excess_returns=np.dot(inv(inv(Thau*cov_matrix)+np.dot(P.transpose(),inv(Omega),P)), (np.dot(inv(Thau*cov_matrix),pi)+np.dot(P.transpose(),inv(Omega),Q)))
		results_Black_Litterman[0,i]=view_adjusted_equilibrium_excess_returns #here we store the pi'
		j=0
		for j in range(len(weights)):
			results_Black_Litterman[j+1,i] = weights[j] #here we store the weights
	#now we have all the pi' and weights for every portfolio is time to choose the optimal weights

	optimal_weights=np.zeros(len(positions)+1)#the first index  is the pi' the others are just the weights
	optimal_weights[0]=np.amax(results_Black_Litterman,0)
	#some conditions for the search loop
	Cond=False
	i=0
	while Cond==False:
		if results_Black_Litterman[0,i]==optimal_weights[0]:
			j=0
			for j in range(len(weights)): #here we store the optimal weights
				optimal_weights[j+1]=results_Black_Litterman[j+1,i]
			Cond=True
		else:
			i=i+1

	return optimal_weights



		
