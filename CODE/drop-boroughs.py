def drop_bor(nn,bb,colA):
    for i in nn.index:
         if len(bb[nn.colA[i]==bb.colA].index)==0:
                     bb.drop([i])
    return bb
