# Marketing-Mixed-Model-
Marketing Mix Model (OLS Regression) using sample data, in preparation for my role as Data Science Intern at Hallam Digital Marketing

My first project as Data Science Intern at Hallam is to develop a Marketing Mix Model for a client. 

In preparation for this, I used Sagidur Rahman's Kaggle - made public on Kaggle. 
Using this data set, I performed Exploratory Data Analysis; developing a correlation matrix, pariplot, contribution plot and conducting feature importance. 
The correlation maps showed that sales showed a strong correlation between TV and sales (0.78), there was a moderate correlation between radio and sales (0.58), and a weak correlation between newspaper and sales (0.23). The other EDA also acted in support of these findings. 

I then developed the predicted values model and then compared predicted sales values with the actual sales values to visually see how the model performed.
The model, appeared to be a good estimator of sales values. 

Interpreting the Marketing Mix Model:
- The Adj. R-squared is 0.896, therefore approximately 90% of the total variation in the data can be explained by the model. This also means that the model doesn’t   account for 10% of the data used — this could be due to omitted variables, for example if there was another marketing channel that wasn’t included.

- Prob (F-statistic): 1.58e-96. This indicates that, overall, the regression is meaningful.

- Looking at P>|t|, the p-values for TV and radio are less than 0.000, but the p-value for newspapers is 0.86, which indicates that newspaper spend has no             significant impact on sales. 

EDA: 

Correlation Map

![Correlation_Map](https://user-images.githubusercontent.com/93582626/144768103-d7d1bf5b-7047-4ba5-82a6-659b1e16b097.png)

PairPlot

![Pair_Plot](https://user-images.githubusercontent.com/93582626/144768120-a2d20b18-ce56-4ffd-ae25-ad6ecd7a3251.png)

Feature Importance

![Feature Importance](https://user-images.githubusercontent.com/93582626/144768128-22d7cb65-7f0f-4bf9-937c-fe660781d06b.png)

Contribution Plot

![Contribution_Plot](https://user-images.githubusercontent.com/93582626/144768138-ae7daa46-877d-4501-8c4f-4d72c47c6a77.png)

Predicted vs Atual Sales 

![Actual vs Predicted MMM](https://user-images.githubusercontent.com/93582626/144768153-9585c700-8922-4ff4-afb8-ded74b649d38.png)

Marketing Mixed Model Summary 

![MMM_Example_Model_Summary](https://user-images.githubusercontent.com/93582626/144768051-c96278d5-2a7f-4acf-b400-5031444d7f16.png)

Acknowledgements

The work produced was inspired by the first project assigned by my new employer and the work done by Terence Shin and Dr. Robert Kübler
