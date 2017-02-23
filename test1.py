import ROUGE_L as rouge
import time
import generate_annotations_datas as gd

start = time.time()
gd1=gd.generate_data()
number=20000
inputs,targes=gd1.generate(number)
r1=rouge.ROUGE_L(0.6,0.15,15,0.01)
end = time.time()
print("load time:",end-start)
print("\n\nenter \n\n")
count=0
start_time=time.time()
for i in range(len(inputs)):
    print("\ntest:",i)
    print(inputs[i],"\n",targes[i])
    r1.set_inputs(inputs[i])
    r1.set_targes(targes[i])
    start = time.time()
    a=r1.Caculate_ROUGE_L()
    end = time.time()
    print("[",i+1,"] time: ",end-start,"score: ",a,"\n")
    if a<=50:
        count+=1
end_time=time.time()
print("total time: ",end_time-start_time," acc: ",count*1.0/len(inputs))
