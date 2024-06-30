import numpy as np
import pandas as pd
import math
from scipy import optimize
from data import download_sector_returns

class Portfolio:
    def __init__(
            self,
            sectors = ['Communication Services',
               'Consumer Discretionary',
               'Consumer Staples',
               'Energy',
               'Financials',
               'Health Care',
               'Industrials',
               'Information Technology',
               'Materials',
               'Real Estate',
               'Utilities',
               ],
            weights = np.array([0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.10, 0.09, 0.09, 0.09]).reshape(-1, 1),
            riskTolerance = 3, # From 1-10
            cov_matrix = None
        ):
        self.sectors = sectors
        self.weights = weights
        self.riskTolerance = riskTolerance
        self.cov_matrix = cov_matrix

        if self.cov_matrix == None:
            sector_data = download_sector_returns()
            adj_close_df = pd.concat(sector_data.values(), axis=1)
            adj_close_df.columns = sector_data.keys()
            self.cov_matrix = adj_close_df.cov()

        self.returns = self.riskTolerance * (self.cov_matrix @ self.weights)
    
class BlackLitterman:
    def __init__(
            self,
            priorPortfolio,
            Q, # np array input
            P, # np array input
            tau,
        ):
        self.priorPortfolio = priorPortfolio
        
        # N = number of assets
        # K = number of views
        
        self.Q = Q # Kx1 view vector (np array)
        self.P = P # KxN picking matrix (np array)
        self.Pi = priorPortfolio.returns # Nx1 prior expected returns (np array)
        self.tau = tau # scalar tuning constant

        self.Sigma = priorPortfolio.cov_matrix.values # NxN covariance matrix (.values return np array)
        self.Omega = self.calculate_omega() # KxK uncertainty matrix (np array)

        self.E = self.calculate_expected_returns() # Nx1 vector of expected returns --> Black-Litterman Formula Output
    
    def calculate_omega(self):
        # Omega = tau * P * Sigma * P.T
        return np.diag(np.diag((self.P @ self.Sigma @ self.P.T) * self.tau))
    
    def calculate_expected_returns(self):
        """
         E = [(tau * Sigma)^-1 + P.T * Omega^-1 * P]^-1 * [(tau * Sigma)^-1 * Pi + P.T * Omega^-1 * Q]
             [<-----term1----> + <------term2----->]      [<-------term3-------> + <-----term4------>]
             [--------------matrix1----------------]^-1 * [-----------------matrix2------------------]
        """

        tauSigma = self.tau * self.Sigma
        term1 = np.linalg.inv(tauSigma)
        term2 = self.P.T @ np.linalg.inv(self.Omega) @ self.P
        term3 = np.linalg.inv(tauSigma) @ self.Pi
        term4 = self.P.T @ np.linalg.inv(self.Omega) @ self.Q
        
        matrix1 = term1 + term2
        matrix2 = term3 + term4

        expected_returns = np.linalg.inv(matrix1) @ matrix2
        
        return np.array(expected_returns) # returns np array

portfolio = Portfolio()

Q = np.array([0.05, -0.10, 0.15]).reshape(-1, 1)
P = np.array(
    [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]
)
tau = 0.05

bl = BlackLitterman(portfolio, Q, P, tau)
print(bl.E)