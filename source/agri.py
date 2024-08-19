def crop_selection(soil_type, ph_level, water_resources):
    if soil_type == "loamy" and water_resources == "moderate" and ph_level > 6.5 and ph_level < 7.5:
        return "Recommended Crop: Wheat or Maize"
    elif soil_type == "clay" and water_resources == "low" and ph_level <= 6.5:
        return "Recommended Crop: Millet or Sorghum"
    else:
        return "Recommended Crop: Rice or Barley"

def disease_identification(symptoms):
    if symptoms in "yellow leaves" :
        return "Possible Disease: Nitrogen deficiency. Treatment: Apply nitrogen-rich fertilizer."
    elif symptoms in "spots on leaves" :
        return "Possible Disease: Fungal infection. Treatment: Use fungicide."
    else:
        return "Disease not identified. Please consult an expert."

while True:
    print("Welcome to the Farming Assistant")
    print("1. Crop Selection")
    print("2. disease identifiation")
    print("3. Exit")
        
    choice = input("Enter the number of the module you want to use: ")
        
    if choice == "1":
        soil_type = input("Enter soil type (e.g., loamy, clay): ")
        ph_level = float(input("Enter soil pH level: "))
        water_resources = input("Enter water resources (e.g., low, moderate, high): ")
        
        crop = crop_selection(soil_type, ph_level, water_resources)
        print(crop)
        
        
            
    elif choice=="2":
        disease_check = input("Do you want to perform disease identification? (yes/no): ")
        if disease_check== "y":
            symptoms = input("Describe the symptoms observed on the crops: ")
            print(disease_identification(symptoms))

        
    elif choice == "3":
        break
        
    else:
        print("Invalid choice. Please select a valid module.")
