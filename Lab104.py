#The authors are Maggie Dunn and Cody Brown
rv_dict = {"cake flour" : 3, "baking soda" : 1, "cocoa powder" : 2, "salt" : .5, "unsalted butter" : .5, "granulated sugar" : 2, "vegetable oil" : 1, "eggs" : 4, "vanilla extract" : 1, "distilled vineger" : 1, "buttermilk" : 1}
lemon_dict = {'all purpose flour':3,'baking powder':3,'baking soda':1,'salt':1,'unsalted butter':1,'granulated sugar': 2,'eggs':3,'vanilla extract':2,'milk': 6, 'lemon zest': 1,'lemon juice':1}
def similar_ing(dict_1, dict_2):
    ing = []
    for i in rv_dict:
        for j in lemon_dict:
            if i == j:
                ing.append(i)
    return ing
