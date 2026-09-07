MENU ={
    "espresso":{
        "incredents":{
            "water":100,
            "coffee":50

        },
        "cost":2.5
    },
    "latte":{
        "incredents":{
            "water":200,
            "milk":100,
            "coffee":20
        },
        "cost":1.5

    },
    "cappuccino":{
        "incredents":{
            "water":300,
            "milk":150,
            "coffee":80
        },
        "cost":1.2
    }
}

profit=0
resources={
    "water":500,
    "milk":400,
    "coffee":200

}

is_on=True
while is_on:
    choice=input("DO you want to have drink?(espresso,latte)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}ml")