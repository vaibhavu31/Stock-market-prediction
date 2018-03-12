import pandas as pd;
from sklearn.cluster import KMeans
from sklearn import svm
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
f = pd.ExcelFile('tele_stocks.xlsx')
df = f.parse('Sheet1')

X = pd.DataFrame(df.iloc[:,5:8])
#X.drop(['Government Policies'], axis = 1, inplace = True)
s = df.iloc[:,0]
rival = pd.DataFrame(df.iloc[:,1:4])
rival = rival.mean(axis=1)
rival,s = rival.diff(),s.diff()
rival.iloc[0],s.iloc[0] = 0,0
X.iloc[:,0] = rival
X.iloc[:,1] = s
plt.scatter(rival,s)
plt.show()
print(X.iloc[:,:2])
#self1 = df.iloc[:,0]



def km():
    f = pd.read_excel('tele_stocks.xlsx')
    #print(f.head())
    f1 = f.drop(["Idea Cellular","Tata Communications","Reliance Communications","Days","Rival","Self Performance"],axis=1)
    #f1 = s
    #print(f1.head())
    km = KMeans(n_clusters=4, init='k-means++', n_init=10)
    km.fit(f1)
    KMeans(copy_x=True,init='k-means++',max_iter=300,n_clusters=4,n_init=10,n_jobs=1,precompute_distances='auto',random_state=None,tol=0.0001,verbose=0)
    x = km.fit_predict(f1)
    #print(x)
    f["Cluster"]= x
   # print(f.head())
    f1 = f.sort_values(by=['Cluster'])
    #print(f1)
    formean=pd.DataFrame(f1.iloc[:,[0,7]])
    print(formean)
    cluster0=formean[formean.Cluster==0]
    print(cluster0)
    selfmean1=cluster0[['Bharti Airtel']].mean(axis=0)
    print(selfmean1)
    cluster1=formean[formean.Cluster==1]
    print(cluster1)
    selfmean2=cluster1[['Bharti Airtel']].mean(axis=0)
    print(selfmean2)
    cluster2=formean[formean.Cluster==2]
    print(cluster2)
    selfmean3=cluster2[['Bharti Airtel']].mean(axis=0)
    print(selfmean3)
    cluster3=formean
    [formean.Cluster==3]
    print(cluster3)
    selfmean4=cluster3[['Bharti Airtel']].mean(axis=0)
    print(selfmean4)
    s1=float(selfmean1)
    s2=float(selfmean2)
    s3=float(selfmean3)
    s4=float(selfmean4)
    if s1>s2 and s1>s3 and s1>s4:
        highest=s1
    elif s2>s1 and s2>s3 and s2>s4:
        highest=s2
    elif s3>s1 and s3>s2 and s3>s4:
        highest=s3
    else:
        highest=s4
    print(highest)
    x = []
    for i in range(1,52):
        x.append(highest)
    X['Self Performance'] = x

    print(X)
        
k = km()

y = []
for i in range(len(s)):
    if s[i]>=0:
        y.append(1)
    else:
        y.append(0)
model=svm.SVC(kernel='linear',C=1000,gamma=1)
model.fit(X,y)
model.score(X,y) 
x = [[3,2],[-4,2],[1,-8]]
#x = x.values.reshape(1,-1)
predicted=model.predict(x)
print("predicted =",predicted)
