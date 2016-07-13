#Below is my patsy formula to predict delays.
formula = 'dep_binary_delay ~ C(month) + C(day_of_week) + distance + C(dep_time_blk) + C(origin_airport_id) + C(carrier) -1'

#I use patsy to split up my target (binary delay) and the rest of my predictor, and I do so in a dataframe format. 
Y, X = patsy.dmatrices(formula, data=bay, return_type='dataframe')

#After finding some general parameters I run another gridsearch with more a more specific parameter set 
#This will help me hone in on the best parameters. 
sgdc = SGDClassifier()

sgdc_params = {
    'loss':['log'],
    'penalty':['elasticnet'],
    'n_iter':[5],
    'alpha':np.logspace(-4, 4, 10),
    'l1_ratio':[0.05,0.06,0.07,0.08,0.09,0.1,0.12,0.13,0.14,0.15,0.2]
}

sgdc_gs = GridSearchCV(sgdc, sgdc_params, cv=5, verbose=1, n_jobs=1)

#Here I fit the model to my dataset
sgdc_gs.fit(Xn,Y)

#Best parameters from the above gridsearch
best_params = {'n_iter': 5, 'alpha': 0.046415888336127774, 'loss': 'log', 'penalty': 'elasticnet', 'l1_ratio': 0.1}
