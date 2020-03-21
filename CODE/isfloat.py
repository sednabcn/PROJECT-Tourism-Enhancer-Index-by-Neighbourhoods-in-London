class isfloat(object):
    def __init__(self,number):
        self.number=number
    def isfloat(self):
            chain=self.number.split('.')
            ii=0
            while chain[ii].isdigit():
                ii+=1
                if ii==len(chain):
                    break
            if ii==len(chain):
                   return 'True'
            else:
                   return 'False'
