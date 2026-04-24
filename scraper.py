from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import random
from datetime import datetime

print("🚀 Generating Advanced Sofa Dataset (200 rows)...")

products = []
prices = []

# -----------------------------
# TRY SCRAPING (OPTIONAL)
# -----------------------------
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.pepperfry.com/site_product/search?q=2%20seater%20sofa")

    time.sleep(5)

    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    items = driver.find_elements(By.XPATH, "//div")

    for item in items:
        try:
            text = item.text
            if "₹" in text and ("Sofa" in text or "Seater" in text):
                lines = text.split("\n")
                name = lines[0]

                for line in lines:
                    if "₹" in line:
                        price = int(line.replace("₹", "").replace(",", ""))
                        break

                products.append(name)
                prices.append(price)

        except:
            continue

    driver.quit()

except:
    print("⚠️ Scraping failed, using fallback...")

# -----------------------------
# FALLBACK PRODUCTS
# -----------------------------
if len(products) == 0:
    products = [
        "Modern Fabric Sofa", "Luxury Leather Sofa", "Wooden Classic Sofa",
        "Compact Urban Sofa", "Premium Designer Sofa", "Minimalist Sofa",
        "L-Shaped Sofa", "Convertible Sofa Bed", "Velvet Sofa", "Recliner Sofa"
    ]
    prices = [18000, 35000, 25000, 15000, 42000, 20000, 30000, 27000, 32000, 40000]

# -----------------------------
# STATIC PRODUCT DETAILS
# -----------------------------
brand_fixed = "ARRA"
materials = ["Wood", "Fabric", "Leather", "Velvet"]
colors = ["Brown", "Grey", "Beige", "Blue", "Black"]

data = []

# -----------------------------
# GENERATE 200 ROWS
# -----------------------------
for i in range(200):

    idx = i % len(products)

    name = products[idx]
    base_price = prices[idx]

    discount = random.randint(10, 50)
    original_price = int(base_price / (1 - discount / 100))

    rating = round(random.uniform(3.5, 4.9), 1)
    reviews = random.randint(5, 1000)

    material = random.choice(materials)
    color = random.choice(colors)

    # -----------------------------
    # RANDOMIZED PRODUCT DETAILS
    # -----------------------------
    seating_height = random.randint(14, 22)
    warranty = random.choice([6, 12, 18, 24, 36])
    weight = random.randint(20, 60)

    sku = f"FN{random.randint(1000000, 9999999)}-S-PM{random.randint(10000, 99999)}"

    dim_cm = f"H {random.randint(70, 95)} x W {random.randint(120, 200)} x D {random.randint(70, 100)}"
    dim_inch = f"H {random.randint(28, 38)} x W {random.randint(48, 80)} x D {random.randint(28, 40)}"

    data.append({
        "Product Name": name,
        "Brand": brand_fixed,
        "Price (₹)": base_price,
        "Original Price (₹)": original_price,
        "Discount (%)": f"{discount}%",
        "Rating": rating,
        "Reviews": reviews,

        "Material": material,
        "Color": color,
        "Size": "2-Seater",

        "Seating Height": seating_height,
        "Warranty (Months)": warranty,
        "Weight (KG)": weight,
        "SKU": sku,
        "Dimensions (cm)": dim_cm,
        "Dimensions (inch)": dim_inch
    })

# -----------------------------
# CREATE DATAFRAME
# -----------------------------
df = pd.DataFrame(data)

# Save file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"sofa_200_dataset_{timestamp}.csv"
df.to_csv(filename, index=False)

print(f"\n✅ Dataset Created: {filename}")
print(df.head())

# -----------------------------
# MARKET INSIGHT
# -----------------------------
avg_price = df["Price (₹)"].mean()
premium_factor = df["Rating"].mean() / 4
suggested_price = int(avg_price * premium_factor)

print("\n📊 Market Insights:")
print(f"Average Price: ₹{avg_price:.0f}")
print(f"💡 Suggested Selling Price: ₹{suggested_price}")
