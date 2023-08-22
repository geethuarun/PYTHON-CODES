from re import*
tweets="What a game , @ hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
rule="[@][a-zA-Z0-9_]+"
# tw=tweets.split()
# print(tw)
# for t in tw:
#     matcher=fullmatch(rule,t)
#     if matcher:
#         print(matcher)

matcher=finditer(rule,tweets) 
for m in matcher:
    print(m.group())      