from duckduckgo_images_api import search
import requests
PharmacyDB = [
    {"Image": "./Server/DB/Images/polyethylene-glycol-250x250.webp",
    "Name": "Polyethylene glycol pegred powder",
    "Price": "180"},
    {"Image": "./Server/DB/Images/novorapid-flexpens-500x500.webp",
    "Name": "Novorapid Flexpens",
    "Price": "2050.3"},
    {"Image": "./Server/DB/Images/pediasure-complete-500x500.webp",
    "Name": "Pediasure Complete",
    "Price": "750"},
    {"Image": "./Server/DB/Images/hcg-pregnancy-test-kit-500x500.webp",
    "Name": "Pregnancy Test Kit",
    "Price": "453"},
    {"Image": "./Server/DB/Images/health-d-500x500 (1).webp",
    "Name": "Health-D",
    "Price": "500"},
    {"Image": "./Server/DB/Images/cinnarizine-tablets-500x500.webp",
    "Name": "Cinnarizine Tablets",
    "Price": "200"},
    {"Image": "./Server/DB/Images/coxiblu-90-tablets-500x500.webp",
    "Name": "Coxiblu 90 Tablets",
    "Price": "300"},
    {"Image": "./Server/DB/Images/Paracetamol-500-MG-Tablet-manufcaturer-india-Taj-Life-Sciences-6-scaled.webp",
    "Name": "Paracetamol-500-MG-Tablet",
    "Price": "260"},
    {"Image": "./Server/DB/Images/rosuvastatin-10mg-fenofibrate-145mg-medicine-500x500.webp",
    "Name": "Rosuvastatin 10mg Fenofibrate 145mg Medicine",
    "Price": "300"},
    {"Image": "./Server/DB/Images/atazor-200-tablets-500x500.webp",
    "Name": "Atazor 200 Tablets",
    "Price": "300"},
    {"Image": "", "Name": "Amoxicillin Capsules", "Price": "50"},
    {"Image": "", "Name": "Ibuprofen Tablets", "Price": "30"},
    {"Image": "", "Name": "Acetaminophen Tablets", "Price": "25"},
    {"Image": "", "Name": "Omeprazole Capsules", "Price": "75"},
    {"Image": "", "Name": "Metformin Tablets", "Price": "40"},
    {"Image": "", "Name": "Atorvastatin Tablets", "Price": "80"},
    {"Image": "", "Name": "Ciprofloxacin Tablets", "Price": "60"},
    {"Image": "", "Name": "Levothyroxine Tablets", "Price": "35"},
    {"Image": "", "Name": "Lisinopril Tablets", "Price": "45"},
    {"Image": "", "Name": "Losartan Tablets", "Price": "50"},
    {"Image": "", "Name": "Simvastatin Tablets", "Price": "70"},
    {"Image": "", "Name": "Metoprolol Tablets", "Price": "55"},
    {"Image": "", "Name": "Aspirin Tablets", "Price": "20"},
    {"Image": "", "Name": "Naproxen Tablets", "Price": "35"},
    {"Image": "", "Name": "Loratadine Tablets", "Price": "30"},
    {"Image": "", "Name": "Furosemide Tablets", "Price": "40"},
    {"Image": "", "Name": "Fluoxetine Capsules", "Price": "50"},
    {"Image": "", "Name": "Gabapentin Capsules", "Price": "60"},
    {"Image": "", "Name": "Pantoprazole Tablets", "Price": "65"},
    {"Image": "", "Name": "Sertraline Tablets", "Price": "55"}

   
]
i=0
URLs={}
for Item in PharmacyDB:
  
    results = search(Item['Name'],3)
    j=0
    for result in results['results']:    
        j+=1
        ImageURL=result['image']
        height=result['height']
        width=result['width']
        if(width-height<100):
            URLs[f"{Item['Name']} - {j}"]=(ImageURL)
            break
print(URLs)


for key, url in URLs.items():
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check the response status code
    if response.status_code == 200:
        # Save the image to a file
        imageURLN=f"Server/DB/Images/{key}.jpg"
        with open(imageURLN, "wb") as f:
            f.write(response.content)
            for i,item in enumerate(PharmacyDB):
                if key in item:
                    PharmacyDB[i]['Image']='./'+imageURLN

        print(f"Downloaded image from {url}")
    else:
        print(f"Failed to download image from {url}")
        
print(PharmacyDB)