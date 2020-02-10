# Pina Colada Original Recipe
how_much = 1500 # ml
coco = 85.0
pineapple = 170.0
rum = 43.0
total = coco + pineapple + rum
p_coco = coco/total
p_pine = pineapple/total
p_rum = rum/total
print("To get {}ml of Pina Colada u need {}ml of coconut cream, {}ml of pineapple juice and {}ml of rum".format(how_much, round(p_coco*how_much), round(p_pine*how_much),round(p_rum*how_much)))
