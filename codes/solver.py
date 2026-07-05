import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution
from scipy.interpolate import PchipInterpolator

df=pd.read_csv("data/xy_data.csv")
x,y=df["x"].values,df["y"].values
def inv_loss(p):
    theta,X=p
    r=np.radians(theta)
    #After removing the horizontal and vertical offsets, the original.e/quations have the structure of a 2D rotation of the hidden pair (t, A),
    #[x - X][ cos(theta)  -sin(theta) ] [t],[y - 42] = [ sin(theta)   cos(theta) ] [A]
    # where A = exp(M|t|) * sin(0.3t).
    #Applying the inverse rotation gives candidate t and A values directly,from every observed (x, y) point.
    t=(x - X)*np.cos(r)+(y-42)*np.sin(r)
    A=-(x-X)*np.sin(r)+(y-42)*np.cos(r)
    s=np.sin(0.3 * t)
    ok=(t>6)&(t<60)&(abs(s)>0.15)&(A*s>0)
    if ok.sum()<1000:
        return 1e9
    # Since t > 0 in the required domain, A = exp(Mt) * sin(0.3t).Therefore,log(A / sin(0.3t)) = Mt. This changes the exponential, nonlinear relationship to a linear one.
    # line through the origin in (t, z) space.
    z=np.log(A[ok]/s[ok])

    #Estimate M as the least-squares slope through the origin:
    #M=sum(t_i * z_i) / sum(t_i^2)->This gives the value of M that best explains the recovered A values for the current candidate theta and X.
    M=np.sum(t[ok]*z)/np.sum(t[ok]**2)
    # Reject the candidate if the implied M lies outside the allowed range.
    if not -0.05 < M < 0.05:
        return 1e9
    return np.mean(abs(A[ok]-np.exp(M*t[ok])*s[ok]))
init=differential_evolution(inv_loss,[(0,50),(0,100)],seed=42,tol=1e-12,maxiter=500)
theta0,X0=init.x
r0=np.radians(theta0)
t_raw=(x-X0)*np.cos(r0)+(y-42)*np.sin(r0)
print("recovered t range:",t_raw.min(),"to",t_raw.max())
# The csv points are not used in row order. Sorting by the recovered t values,restores the actual progression of points along the parametric curve.
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

def l1(p):
    theta,M,X=p
    r=np.radians(theta)
    A=np.exp(M*np.abs(tu))*np.sin(0.3*tu)
    xp=tu*np.cos(r)-A*np.sin(r)+X
    yp=42+tu*np.sin(r)+A*np.cos(r)
    return np.sum(
        abs(xe-xp)
        + abs(ye-yp)
    )

result = differential_evolution(
    l1,
    [(0, 50),(-0.05, 0.05),(0, 100)],
    seed=42,
    tol=1e-10,
    maxiter=500
)
theta,M,X=result.x
print("theta=",theta)
print("M=",M)
print("X=",X)
print("total uniform L1 =",result.fun)
print("mean uniform L1 =",result.fun / len(tu))
