main_dish={"poori":5,"dosa":5,"ideyapam":5,"parota":10}
side_dish={"vegkurma":10,"vadakari":20,"chennamasala":15}
dish1=(input("---ENTER MAIN DISH:---"))
quan=int(input("QUANTITY:"))
dish2=(input("---ENTER SIDE DISH:---"))
tot_tm1=[]
tot_tm2=[]
for item in main_dish:
    if dish1==item:
        it=(main_dish.get(item)*quan)
        tot_tm1.append(it)
        print(f"{item}-----Rs:",it)
for item in side_dish:
    if dish2==item:
        it2=side_dish.get(item)
        tot_tm2.append(it2)
        print(f"{item}-----Rs:",it2)
total=list(tot_tm1)+(tot_tm2)
fi_total=sum(total)
print("-----TOTAL AMOUNT TO BE PAID Rs:",fi_total)
print("------THANK YOU!...VISIT AGAIN------")

    
