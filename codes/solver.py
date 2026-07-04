import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution
from scipy.interpolate import PchipInterpolator

df=pd.read_csv("data/xy_data.csv")
x,y=df["x"].values,df["y"].values
def inv_loss(p):
    theta,X=p
    r=np.radians(theta)
    t=(x - X)*np.cos(r)+(y-42)*np.sin(r)
    A=-(x-X)*np.sin(r)+(y-42)*np.cos(r)
    s=np.sin(0.3 * t)
    ok=(t>6)&(t<60)&(abs(s)>0.15)&(A*s>0)
    if ok.sum()<1000:
        return 1e9
    z=np.log(A[ok]/s[ok])
    M=np.sum(t[ok]*z)/np.sum(t[ok]**2)
    if not -0.05 < M < 0.05:
        return 1e9
    return np.mean(abs(A[ok]-np.exp(M*t[ok])*s[ok]))

init=differential_evolution(inv_loss,[(0,50),(0,100)],seed=42,tol=1e-12,maxiter=500)
theta0,X0=init.x
r0=np.radians(theta0)
t_raw=(x-X0)*np.cos(r0)+(y-42)*np.sin(r0)
print("recovered t range:",t_raw.min(),"to",t_raw.max())

order=np.argsort(t_raw)
ts=t_raw[order]
xs=x[order]
ys=y[order]
ts,idx=np.unique(ts,return_index=True)
xs=xs[idx]
ys=ys[idx]
tu=np.linspace(6,60,1502)[1:-1]
xe=PchipInterpolator(ts,xs,extrapolate=True)(tu)
ye=PchipInterpolator(ts,ys,extrapolate=True)(tu)

print("uniform samples:",len(tu))

