import json


class generate_data:
    def __init__(self):
        return 
    def load_data(self):
        with open("captions_val2014.json",'r') as f:
            reads=json.load(f)
        self.data=reads['annotations']
    def generate(self,number):
        self.load_data()
        inputs=[]
        targets=[]
        hashtable=[[] for i in range(number)]
        for i in range(len(self.data)):
            hashtable[(self.data[i]['image_id'])%number].append(self.data[i])
        for i in range(number):
            if len(hashtable[i])>1:
                id1=hashtable[i][0]['image_id']
                s1=hashtable[i][0]['caption']
                flag=0
                temp=[]
                for j in range(1,len(hashtable[i])):
                    id2=hashtable[i][j]['image_id']
                    if id1==id2:
                        flag=1
                        s2=hashtable[i][j]['caption']
                        temp.append(s2)
                if flag==1:
                    targets.append(temp)
                    inputs.append(s1)
        return inputs,targets
