import ROUGE_L as rouge
import time

start = time.time()
inputs = [line.rstrip('\n') for line in open("input_test.txt")]
target_content = [line.rstrip('\n') for line in open("target_test.txt")]
targes=[]
for i in target_content:
    temp=[]
    temp.append(i)
    targes.append(temp)
r1=rouge.ROUGE_L(0.8,0.2,15,0.01)
end = time.time()
print("load time:",end-start)

for i in range(len(inputs)):
    print("begin exec")
    r1.set_inputs(inputs[i])
    r1.set_targes(targes[i])
    start = time.time()
    a=r1.Caculate_ROUGE_L()
    end = time.time()
    print("[",i+1,"] time: ",end-start,"score: ",a)
