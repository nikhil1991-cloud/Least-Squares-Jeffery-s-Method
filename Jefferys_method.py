import numpy as np

def generate_alphas(A,y,Initial_a,Sigma_matrix,epochs):
    """Solves for z to the problem Az=y when uncertainties are present in both A and y.
    
    Input parameters:
    
        A: Array of shape (m,n) with m number of observations and n independent variables.
    
        y: Array of shape (m,1) with m number of observations.
    
        Sigma_matrix: Array of shape (mj,mj) where m is the number of observations and j is the total number of measured parameters (both dependent and independent variables). j = n + 1 in this case.
    
        epochs: Number of iterations over which the optimization is performed.
        
    Output parameters:
    
        z: Array of shape (1,n) which are the coefficients for n independent variables.
    """
    X_d = np.c_[y,A]#initialize model parameters
    x_d = X_d.flatten()#flatten model parameters
    a_g = Initial_a#guess values of coefficients from nnls
    DfDx = np.zeros((X_d.shape[0],X_d.shape[0]*X_d.shape[1]))#initialize df/dx array
    e=0
    for e in range (0,epochs):
        X_g = np.c_[np.dot(A,a_g),A] #calculate guessed model parameters
        x_g = X_g.flatten() #flatten guessed model parameters
        delta_x_g = x_d - x_g #calculate delta_xg
        f_xg_ag = y - np.dot(A,a_g) #calculate the f(x,a) at xg,ag
        DfDx_xg_ag = np.insert(-1*a_g,0,1)#fill in the DfDx matrix
        i=0
        for i in range (0,DfDx.shape[0]):
            DfDx[i,i*X_g.shape[1]:i*(2*X_g.shape[1])] = DfDx_xg_ag
        DfDa = (-1)*X_g[:,1:] #DfDa matrix
        #iterations in section 14.9
        W = np.linalg.inv(np.matmul(DfDx,np.matmul(Sigma_matrix,DfDx.T)))
        alpha_double_dashed = np.matmul(DfDa.T,np.matmul(W,DfDa))
        phi_g_dashed = f_xg_ag + np.matmul(DfDx,delta_x_g)
        delta_a = np.matmul(np.matmul(np.linalg.inv(alpha_double_dashed),-DfDa.T),np.matmul(W,phi_g_dashed))
        delta_x = np.matmul(np.matmul(-Sigma_matrix,DfDx.T),np.matmul(W,(phi_g_dashed + np.matmul(DfDa,delta_a))))
        a_g = a_g + delta_a
        x_g = x_d + delta_x_g
    return a_g
