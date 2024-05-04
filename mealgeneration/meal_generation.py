import flet as ft
import pandas as pd
import random 


class person_info: ### information of user and parameters for meal generation
    def __init__(self, max_calorie, num_meals,num_snacks, typeList):
        self.parameters = { "max_calorie" : max_calorie, "num_meals": num_meals, "num_snacks": num_snacks,
                           "total_calories": 0, "meal_calories": 0, "snack_calories":0} ##
        if self.parameters["num_snacks"] == 0:
            self.parameters["meal_calories"] = self.parameters["max_calorie"] // self.parameters["num_meals"]
        elif self.parameters["num_meals"] == 0:
            self.parameters["snack_calories"] = self.parameters["max_calorie"] // self.parameters["num_snacks"]
        else: ###already divided per meal and snacks
            self.parameters["meal_calories"] = (self.parameters["max_calorie"] * 0.9)/self.parameters["num_meals"]
            self.parameters["snack_calories"] = self.parameters["max_calorie"] * 0.1/self.parameters["num_snacks"]
        self.mealtypes = typeList
        self.meals_info =[]### list of dictionaries, total meal cal, total snack cal
        self.total_meal_cal = 0
        self.total_snacks_calories = 0
        self.leftovercalories = 0
  
        
    def meals_generation(self):
        df = pd.read_csv("modified_recipe_updated.csv")
        meals_info = []
        total_meal_cal = 0
        snacks_calories = 0
        count = 0
        meal_parameters = self.parameters["meal_calories"]
        snack_parameters = self.parameters["snack_calories"] 

        # Generate meals no need to worry about snack number since we filtered it out
        #we can join the contents of the list together then go if breakfast in 
        if self.parameters["num_meals"] != 0: 
            current_mealname=None
            current_meals_blacklist = []
            for i in range(int(self.parameters["num_meals"])): 
                count = i
                keyword = "|".join(self.mealtypes[i])
                current_mealname = df.loc[
                    ((df["calories"] == meal_parameters) |
                    (df["description"].str.contains(keyword, case=False)) #change
                    & ~((df["title"]).isin(current_meals_blacklist)))]
                if current_mealname.empty:
                    current_mealname = df.loc[((df["calories"] >= meal_parameters - meal_parameters * 0.20) &
                    (df["calories"] <= meal_parameters + meal_parameters * 0.20) &
                    (df["description"].str.contains(self.mealtypes[i], case=False)) #change
                    & ~((df["title"]).isin(current_meals_blacklist)))]

                if not current_mealname.empty:
                    shape = current_mealname.shape
                    length = random.randint(0,shape[0]-1)
                    current_mealname = current_mealname.iloc[length]
                    current_meals_blacklist.append(current_mealname["title"])
                    total_meal_cal += current_mealname["calories"]
                    temp = {
                        ###"meal_num": i + 1,
                        "meal_type": self.mealtypes[i],
                        "meal_name": current_mealname["title"],
                        "meal_calories": current_mealname["calories"],
                        "meal_ingredients": current_mealname["ingredients"],
                        "meal_desc": current_mealname["description"]
                    }
                    meals_info.append(temp)
                else:
                    print(f"No meal found for meal number {i+1}")

        # Generate snacks if num_snacks is not zero
        if self.parameters["num_snacks"] != 0:
            current_snacks_blacklist = []
            for i in range(int(self.parameters["num_snacks"])):
                keyword = "any|".join(self.mealtypes[count+1])
                current_snack = df.loc[
                    (df["calories"] == snack_parameters) & 
                    (df["description"].str.contains(keyword, case=False)) & 
                    ~(df["title"].isin(current_snacks_blacklist))]
                if current_snack.empty:
                    current_snack = df.loc[
                    ((df["calories"] >=  snack_parameters- snack_parameters * 0.20) &
                    (df["calories"] <=  snack_parameters + snack_parameters * 0.20))&
                    (df["description"].str.contains("any", case=False))
                    & (~(df["title"]).isin(current_snacks_blacklist))]


                if not current_snack.empty:
                    shape = current_snack.shape
                    length = random.randint(0,shape[0]-1)
                    current_snack = current_snack.iloc[length]
                    current_snacks_blacklist.append(current_snack["title"])
                    snacks_calories += current_snack["calories"]
                    temp = {
                        ###"meal_num": i + 1,
                        "meal_type": self.mealtypes[count+1],
                        "meal_name": current_snack["title"],
                        "meal_calories": current_snack["calories"],
                        "meal_ingredients": current_snack["ingredients"],
                        "meal_desc": current_snack["description"]
                    }
                    meals_info.append(temp)
                else:
                    print(f"No snack found for snack number {i+1}")
        leftover_calories = int(self.parameters["max_calorie"]) - (total_meal_cal + snacks_calories)
        
        self.meals_info = meals_info 
        self.total_meal_cal = total_meal_cal
        self.snacks_calories = snacks_calories
        self.leftovercalories = leftover_calories

    def print_meal(self):
        print(f"total meal calories: {self.total_meal_cal}")
        print(f"total snack calories: {self.total_snacks_calories}")
        print(f"Leftover Calories: {self.leftovercalories}")
    
        for i in range(len(self.meals_info)):
            meal_dict = self.meals_info[i]
            print(f"meal {i + 1}:")
            for key, value in meal_dict.items():
                print(f"{key}: {value}")