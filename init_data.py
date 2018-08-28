# This file cannot run standalone 
# Must be called by init_db.sh 
from whip.models import Parameter, Post, Bid

# Parameter for Age profolio 
Parameter(key="Age Profile",value="0-10").save()
Parameter(key="Age Profile",value="10-18").save()
Parameter(key="Age Profile",value="18-30").save()
Parameter(key="Age Profile",value="30-40").save()
Parameter(key="Age Profile",value="40-50").save()
Parameter(key="Age Profile",value="50-60").save()
Parameter(key="Age Profile",value="60-80").save()
Parameter(key="Age Profile",value="80-100").save()


# parameter of Event type  
# From https://www.listchallenges.com/parties
Parameter(key="Event Type",value="Tea Party").save()
Parameter(key="Event Type",value="Dinner Party").save()
Parameter(key="Event Type",value="Wine Tasting Party").save()
Parameter(key="Event Type",value="Bachelor Party").save()
Parameter(key="Event Type",value="Pizza Party").save()

# Food quality
Parameter(key="Food Quality",value="Casual").save()
Parameter(key="Food Quality",value="Superb").save()

# Special Diet
# From https://emmafogt.com/what-is-a-special-diet/
Parameter(key = "Special Diet", value="Liquid Diets").save()
Parameter(key = "Special Diet", value="Soft Diets").save()
Parameter(key = "Special Diet", value="Diabetic Diets").save()
Parameter(key = "Special Diet", value="Low-Calorie Diets").save()
Parameter(key = "Special Diet", value="High-Calorie Diets").save()
Parameter(key = "Special Diet", value="Low-Cholesterol Diets").save()
Parameter(key = "Special Diet", value="Low-Sodium Diets").save()
Parameter(key = "Special Diet", value="High-Protein Diets").save()
Parameter(key = "Special Diet", value="Low-Protein Diets").save()
Parameter(key = "Special Diet", value="Low-Residue Diets").save()


# Religious Restriction
# From http://www.webster.edu/specialevents/planning/food-information.html
Parameter(key = "Religious Restriction", value="Vegan").save()
Parameter(key = "Religious Restriction", value="Ovo-Vegetarian").save()
Parameter(key = "Religious Restriction", value="Lacto-Vegetarian").save()
Parameter(key = "Religious Restriction", value="Lacto-Ovo Vegetarians").save()
Parameter(key = "Religious Restriction", value="Pescetarians").save()

# Food Allergies
# From http://www.webster.edu/specialevents/planning/food-information.html
Parameter(key = "Peanut Allergic", value="True").save()
Parameter(key = "Peanut Allergic", value="False").save()
Parameter(key = "Milk Allergic", value="True").save()
Parameter(key = "Milk Allergic", value="False").save()
Parameter(key = "Egg Allergic", value="True").save()
Parameter(key = "Egg Allergic", value="False").save()
Parameter(key = "Wheat Allergic", value="True").save()
Parameter(key = "Wheat Allergic", value="False").save()
Parameter(key = "Soy Allergic", value="True").save()
Parameter(key = "Soy Allergic", value="False").save()
Parameter(key = "Fish Allergic", value="True").save()
Parameter(key = "Fish Allergic", value="False").save()
Parameter(key = "Shellfish Allergic", value="True").save()
Parameter(key = "Shellfish Allergic", value="False").save()



# provision of alcohol
Parameter(key = "Provision of Alcohol", value="False").save()
Parameter(key = "Provision of Alcohol", value="Wine").save()
Parameter(key = "Provision of Alcohol", value="Wine & Beer").save()
Parameter(key = "Provision of Alcohol", value="Wine & Champagne").save()
Parameter(key = "Provision of Alcohol", value="Wine & Beer & Champagne").save()
Parameter(key = "Provision of Alcohol", value="Beer").save()
Parameter(key = "Provision of Alcohol", value="Beer & Champagne").save()
Parameter(key = "Provision of Alcohol", value="Champagne").save()

# kitchen size
Parameter(key = "Kitchen Size", value="Large").save()
Parameter(key = "Kitchen Size", value="Medium").save()
Parameter(key = "Kitchen Size", value="Small").save()
Parameter(key = "Kitchen Size", value="None").save()
# Parameter(key = "Kitchen Size", value="Outdoor").save()

"""
Extra Extra Parameter
"""
# Outdoor
Parameter(key = "Outdoor", value="True").save()
Parameter(key = "Outdoor", value="False").save()

# crockery
Parameter(key = "Crokery Provided", value="True").save()
Parameter(key = "Crokery Provided", value="False").save()

# Glasses
Parameter(key = "Glasses Provided", value="True").save()
Parameter(key = "Glasses Provided", value="False").save()

# Cutlery 
Parameter(key = "Cutlery Provided", value="True").save()
Parameter(key = "Cutlery Provided", value="False").save()

# Chairs
Parameter(key = "Chairs Provided", value="True").save()
Parameter(key = "Chairs Provided", value="False").save()
