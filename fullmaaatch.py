#first character start with k
#
# from re import*
# rule="[k][369][a-zA-Z0-9]*"
# var_name="k3efrds"
# matcher=fullmatch(rule,var_name)
# if matcher!=None:
#     print("valid")
# else:
#     print("invalid")

#to check python variable condition
# from re import*

# rule="[a-zA-Z_][a-zA-Z_]*"
# var_name="num#"
# matcher=fullmatch(rule,var_name)
# if matcher==None:
#     print("invalid")
# else:
#     print("valid")


#java variable rule
#start with alphabet
#special$_
#lengh limit1,10
# from re import*
# rule="[a-zA-Z][a-zA-Z0-9_$]{0,10}"#2nd character can or not present
# var_name="E"
# matcher=fullmatch(rule,var_name)
# # if matcher==None:
# #     print("invalid")
# # else:
# #     print("valid")
# print("invalid" if matcher==None else "valid")


#KERALA VEHICLE NUMBER
# #kL-08-bn-4970
# from re import*
# rule="[k][L][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
# var="kL-08-bn-4970"
# matcher=fullmatch(rule,var)
# print("invalid" if matcher==None else "valid")

#all india vehicle 
# from re import*
# rule="[A-Z]{2}[-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
# var="ab-08-bn-4970"
# matcher=fullmatch(rule,var)
# print("invalid" if matcher==None else "valid")


violations=["kl-08-av-2794",
            "kl-08-av-4970",
            "kl-01-av-14",
            "kl-01-av-1",
            "kl-01-av-12",
            "TN-01-av-1",
            "ghz-01-avO-1",
            "kl0-01-av0-10"

            ]

from re import*
rule="[k][l][-][0-9]{2}[-][a-z]{2}[-][0-9]{1,4}"

for v in violations:
    matcher=fullmatch(rule,v)

    if matcher:
        print(matcher,"kerala")
    else:
        print(matcher,"not kerala")



