import pandas as pd

df = pd.read_csv("recipe.csv")

categories = [
    "#cakeweek", "#wasteless", "22-minute meals", "3-ingredient recipes", "30 days of groceries",
    "advance prep required", "alabama", "alaska", "alcoholic", "anniversary", "anthony bourdain",
    "aperitif", "appetizer", "arizona", "aspen", "atlanta", "australia", "back to school", "backyard bbq",
    "bake", "bastille day", "beverly hills", "birthday", "blender", "boil", "bon appétit", "boston",
    "braise", "breakfast", "broil", "brooklyn", "brunch", "buffet", "bulgaria", "cake", "california",
    "cambridge", "camping", "canada", "candy", "candy thermometer", "casserole/gratin", "chicago",
    "chile", "chill", "christmas", "christmas eve", "cocktail party", "colorado", "columbus", "condiment",
    "condiment/spread", "connecticut", "cook like a diner", "cookbook critic", "costa mesa", "cuba", "dairy",
    "dairy free", "dallas", "deep-fry", "denver", "dessert", "dinner", "dip", "diwali", "dominican republic",
    "dorie greenspan", "double boiler", "drink", "drinks", "easter", "edible gift", "egypt", "emeril lagasse",
    "engagement party", "england", "entertaining", "epi + ushg", "epi loves the microwave", "escarole", "fall",
    "family reunion", "fat free", "father's day", "flaming hot summer", "florida", "food processor",
    "fortified wine", "fourth of july", "france", "frangelico", "frankenrecipe", "freeze/chill",
    "freezer food", "friendsgiving", "fry", "game", "georgia", "germany", "gourmet", "graduation", "grill",
    "grill/barbecue", "guam", "haiti", "halibut", "halloween", "hanukkah", "harpercollins", "hawaii",
    "healdsburg", "healthy", "high fiber", "hollywood", "hot drink", "houston", "ice cream machine", "idaho",
    "illinois", "indiana", "iowa", "ireland", "israel", "italy", "jamaica", "japan", "juicer", "kansas",
    "kansas city", "kentucky", "kentucky derby", "kid-friendly", "kidney friendly", "kirsch", "kitchen olympics",
    "kwanzaa", "labor day", "lancaster", "las vegas", "liqueur", "london", "long beach", "los angeles",
    "louisiana", "louisville", "low cal", "low carb", "low cholesterol", "low fat", "low sodium", "low sugar",
    "low/no sugar", "lunar new year", "lunch", "maine", "mandoline", "mardi gras", "marinade", "marinate",
    "maryland", "massachusetts", "mexico", "mississippi", "missouri", "mixer", "mortar and pestle",
    "mother's day", "minneapolis", "minnesota", "nancy silverton", "nebraska", "new hampshire", "new jersey",
    "new mexico", "new orleans", "new year's day", "new year's eve", "new york", "no meat, no problem",
    "no sugar added", "no-cook", "non-alcoholic", "noodle", "north carolina", "ohio", "oklahoma", "oktoberfest",
    "one-pot meal", "oregon", "organic", "pacific palisades", "paleo", "pan-fry", "parade", "paris", "party",
    "pasadena", "pasta maker", "pastry", "peanut free", "Pennsylvania", "persian new year", "peru",
    "pescatarian", "philippines", "picnic", "pittsburgh", "pistachio", "pizza", "plantain", "plum", "poach",
    "poblano", "poker/game night", "passover", "port", "portland", "potluck", "pressure cooker", "providence",
    "quick & easy", "quick and healthy", "ramadan", "ramekin", "raw", "rhode island", "rosh hashanah/yom kippur",
    "san francisco", "sandwich theory", "santa monica", "sauté", "side", "simmer", "skewer", "slow cooker",
    "smoker", "snapper", "soufflé/meringue", "soup/stew", "south carolina", "spain", "spring", "st. louis",
    "st. patrick's day", "steak", "steam", "stew", "stir-fry", "stock", "sugar conscious", "sukkot", "summer",
    "super bowl", "suzanne goin", "switzerland", "tailgating", "tennessee", "tested & improved", "texas",
    "thanksgiving", "tree nut free", "triple sec", "tropical fruit", "utah", "valentine's day", "vegan",
    "vegetarian", "virginia", "washington", "washington, d.c.", "wedding", "weelicious", "west virginia",
    "westwood", "wheat/gluten-free", "winter", "wisconsin", "wok", "yonkers", "cookbooks", "leftovers", "snack",
    "snack week"
]

ingredients_list = ["almond","amaretto","anchovy","anise","apple","apple juice","apricot","artichoke","arugula",
                    "asian pear","asparagus","avocado","bacon","banana","barley","basil","bass","bean","beef",
                    "beef rib","beef shank","beef tenderloin","beer","beet","bell pepper","berry","biscuit","bitters","blackberry","blue cheese",
                    "blueberry","bok choy","bourbon","bran","brandy","bread","breadcrumbs","brie","brine","brisket",
                    "broccoli","broccoli rabe","brown rice","brownie","brussel sprout","buffalo","bulgur","burrito",
                    "butter","buttermilk","butternut squash","butterscotch/caramel","cabbage","calvados","campari",
                    "cantaloupe","capers","caraway","cardamom","carrot","cashew","cauliflower","caviar","celery",
                    "chambord","champagne","chard","chartreuse","cheddar","cheese","cherry","chestnut","chicken",
                    "chickpea","chile pepper","chili","chive","chocolate","cilantro","cinco de mayo","cinnamon",
                    "citrus","clam","clove","cobbler/crumble","cocktail","coconut","cod","coffee","coffee grinder",
                    "cognac/armagnac","collard greens","cookie","cookies","coriander","corn","cornmeal","cottage cheese",
                    "couscous","crab","cranberry","cranberry sauce","cream cheese","créme de cacao","crêpe","cucumber",
                    "cumin","cupcake","currant","curry","custard","date","digestif","dill","dried fruit","duck","eau de vie",
                    "egg","egg nog","eggplant","endive","fennel","feta","fig","fish","flat bread","fontina","frittata","fritter",
                    "frozen dessert","fruit","fruit juice","garlic","gin","ginger","goat cheese","goose","gouda","grains","grand marnier",
                    "granola","grape","grapefruit","grappa","green bean","green onion/scallion","ground beef","ground lamb","guava","ham",
                    "hamburger","hazelnut","herb","hominy/cornmeal/masa","honey","honeydew","hors d'oeuvre","horseradish","hot pepper",
                    "house cocktail","hummus","ice cream","iced coffee","iced tea","jalapeño","jam or jelly","jerusalem artichoke","jícama",
                    "kahlúa","kale","kiwi","kosher","kosher for passover","kumquat","lamb","lamb chop","lamb shank","lasagna","leafy green",
                    "leek","legume","lemon","lemon juice","lemongrass","lentil","lettuce","lima bean","lime","lime juice","lingonberry",
                    "lobster","lychee","macadamia nut","macaroni and cheese","mango","maple syrup","margarita","marsala","marscarpone",
                    "marshmallow","martini","mayonnaise","meat","meatball","meatloaf","melon","mezcal","miami","michigan","microwave",
                    "midori","milk/cream","mint","molasses","monterey jack","mozzarella","muffin","mushroom","mussel","mustard","mustard greens",
                    "nectarine","nut","nutmeg","oat","oatmeal","octopus","okra","olive","omelet","onion","orange","orange juice","oregano","orzo",
                    "oscars","oyster","pancake","papaya","paprika","parmesan","parsley","parsnip","passion fruit","pasta","pea","peach","peanut",
                    "peanut butter","pear","pecan","pepper","pernod","persimmon","phyllo/puff pastry dough","pickles","pie","pine nut","pineapple",
                    "pomegranate","pomegranate juice","poppy","pork","pork chop","pork rib","pork tenderloin","pot pie","potato","potato salad",
                    "poultry","poultry sausage","prosciutto","prune","pumpkin","punch","purim","quail","quiche","quince","quinoa","rabbit","rack of lamb",
                    "radicchio","radish","raisin","raspberry","red wine","rhubarb","rice","ricotta","roast","root vegetable","rosemary","rosé","rub","rum",
                    "rutabaga","rye","saffron","sage","sake","salad","salad dressing","salmon","salsa","sandwich","sangria","sardine","sauce","sausage",
                    "scallop","scotch","seafood","seattle","seed","self","semolina","sesame","sesame oil","shallot","shavuot","shellfish","sherry","shower",
                    "shrimp","smoothie","sorbet","sour cream","sourdough","soy","soy free","soy sauce","sparkling wine","spice","spinach","spirit","spritzer",
                    "squash","squid","strawberry","stuffing/dressing","sugar snap pea","sweet potato/yam","swiss cheese","swordfish","taco","tamarind","tangerine",
                    "tapioca","tarragon","tart","tea","tequila","thyme","tilapia","tofu","tomatillo","tomato","tortillas","tree nut","trout","tuna","turnip","vanilla",
                    "veal","vegetable","venison","vermont","vermouth","vinegar","vodka","waffle","walnut","wasabi","watercress","watermelon","whiskey","white wine","whole wheat",
                    "wild rice","windsor","wine","yellow squash","yogurt","yuca","zucchini","turkey"]
def find_ingredients(df_row):
    ones_list = []
    for column, value in df_row.items(): 
        if any(column == item for item in ingredients_list):
            if value == 1.0:  
                ones_list.append(str(column))  
    return ", ".join(ones_list) 

def find_categories(df_row):
    ones_list = []
    for column, value in df_row.items(): 
        if any(column == item for item in categories):
            if value == 1.0:  
                ones_list.append(str(column))  
    return ", ".join(ones_list) 

df_new = df.loc[:, "title":"sodium"].copy()  # Copy the subset of the original DataFrame
df_new["ingredients"] = df.apply(find_ingredients, axis=1)
df_new["description"] = df.apply(find_categories, axis=1)

df_new = df_new.dropna(subset=['calories']) 

###filling NaN
df_new['protein'] = df_new['protein'].fillna("NO DATA")
df_new['fat'] = df_new['fat'].fillna("NO DATA")
df_new['sodium'] = df_new['sodium'].fillna("NO DATA")
df_new['fat'] = df_new['fat'].fillna("NO DATA")
shape = df_new.shape
df_new.to_csv("modified_recipe.csv", index=False)
print(shape)

###create
df_new.to_csv("modified_recipe.csv", index=False)