import pandas as pd
import numpy as np
def drop_bor(nn,bb,colA):
     kk=(nn.columns==colA).tolist().index(True)
     pp=(bb.columns==colA).tolist().index(True)
    
     for i in nn.index:
         if nn.loc[i,nn.columns[kk]] not in bb[bb.columns[pp]].tolist():
         #if any(nn[nn.columns[kk]][i]==bb[bb.columns[pp]].tolist())==False:
                 nn=nn.drop([i])
     return nn
 
aa=np.array([[1,2],[2,4],[3,5],[4,2],[5,4],[6,2]])
aa=pd.DataFrame(aa,index=range(aa.shape[0]),columns=['pe','ge'])
bb=pd.DataFrame([2,5,3],index=[0,1,2],columns=['ge'])


if __name__ == '__main__':
      print(aa)
      print(bb)
      cc=drop_bor(aa,bb,'ge')
      print(cc)
      print(aa.shape)
      print(cc.shape)
