data=[
   {"acno":1000,"name":"jhon","balance":30000,"transactions":{
       "credit":[
           
           {"from":1002,"mode":"gpay","amount":1000},
           {"from":1002,"mode":"gpay","amount":2000},
           {"from":1003,"mode":"phonepay","amount":1000},
           {"from":1004,"mode":"imps","amount":1000},
           
       ],
       "debit":[
           {"to":1002,"mode":"imps","amount":1000}
       ]
       
   }  
   
   } ,
    {"acno":1001,"name":"abhijith","balance":590000,"transactions":{
            "credit":[
                
                {"from":1016,"mode":"gpay","amount":1500},
                {"from":1021,"mode":"imps","amount":2020},
                {"from":1016,"mode":"phonepay","amount":10000},
                {"from":1009,"mode":"imps","amount":2400},
                {"from":1039,"mode":"gpay","amount":3600},
            ],
            "debit":[
                {"to":1032,"mode":"imps","amount":500},
                {"to":1021,"mode":"gpay","amount":2700},
                {"to":1103,"mode":"imps","amount":7000},

            ]
            
        }  
        
    },
    {"acno":1002,"name":"arya ashok","balance":140000,"transactions":{
            "credit":[
                
                {"from":1091,"mode":"gpay","amount":5000},
                {"from":1123,"mode":"imps","amount":2223},
                {"from":1456,"mode":"imps","amount":10000},
                {"from":1234,"mode":"gpay","amount":6002},
                {"from":1209,"mode":"phonepay","amount":1600},
                {"from":1908,"mode":"imps","amount":643},
                {"from":2498,"mode":"phonepay","amount":656},
                
            ],
            "debit":[
                {"to":2382,"mode":"imps","amount":5450},
                {"to":1021,"mode":"gpay","amount":290},
                {"to":1103,"mode":"imps","amount":4208},
                {"to":1209,"mode":"phonepay","amount":3400},
                {"to":1103,"mode":"imps","amount":234},
                {"to":2489,"mode":"gpay","amount":2345},
                {"to":1110,"mode":"imps","amount":9876},
                {"to":1800,"mode":"gpay","amount":1928},

            ]
            
        }  
        
        },
    {"acno":1003,"name":"snehith","balance":90000,"transactions":{
            "credit":[
                
                {"from":1096,"mode":"gpay","amount":15000},
                {"from":1031,"mode":"imps","amount":2023},
                {"from":1106,"mode":"imps","amount":1000},
                {"from":1035,"mode":"phonepay","amount":600},
            ],
            "debit":[
                {"to":1032,"mode":"imps","amount":545},
                {"to":1021,"mode":"gpay","amount":2900},
                {"to":1103,"mode":"imps","amount":4000},
                {"to":1103,"mode":"imps","amount":3400},

            ]
            
        }  
        
        },
    {"acno":1004,"name":"akash c","balance":29000,"transactions":{
            "credit":[
                
                {"from":1066,"mode":"gpay","amount":1000},
                {"from":1110,"mode":"imps","amount":223},
                {"from":1101,"mode":"gpay","amount":14568},
                {"from":1777,"mode":"phonepay","amount":6340},
                {"from":1088,"mode":"phonepay","amount":6980},
                {"from":1031,"mode":"imps","amount":600},
            ],
            "debit":[
                {"to":1037,"mode":"imps","amount":5450},
                {"to":1110,"mode":"phonepay","amount":200},
                {"to":1088,"mode":"imps","amount":3467},
                {"to":1031,"mode":"gpay","amount":3444}

            ]
            
        }  
        
        }

]



#print account num balance below 1lakh
#print total amount credited for each account
#print amount credited to each account by the mode of gpay