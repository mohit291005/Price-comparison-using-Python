from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# ==== Path to ChromeDriver ====
chromedriver_path = r"D:\Webdriver\chromedriver-win64\chromedriver.exe"
assert os.path.isfile(chromedriver_path), f"❌ ChromeDriver not found at: {chromedriver_path}"

# ==== Categorized Product List ====
categories = {
    "Mobile Phones": [
        {
            "name": "iPhone 15",
            "flipkart": "https://www.flipkart.com/apple-iphone-15-black-256-gb/p/itm6f0727e3e3b52?pid=MOBGTAGPSMHFKHT5",
            "amazon": "https://www.amazon.in/Apple-iPhone-15-256-GB/dp/B0CHX2WQLX?th=1",
            "croma": "https://www.croma.com/apple-iphone-15-256gb-black-/p/300700"
        },
        {
            "name": "Samsung Galaxy S23",
            "flipkart": "https://www.flipkart.com/samsung-galaxy-s23-5g-phantom-black-256-gb/p/itm347e695feffe7",
            "amazon": "https://www.amazon.in/Samsung-Galaxy-Phantom-Black-Storage/dp/B0BT9FZZKP?th=1",
            "croma": "https://www.croma.com/samsung-galaxy-s23-5g-8gb-ram-256gb-phantom-black-/p/268871"
        },
        {
            "name": "Realme Narzo 60x 5G",
            "flipkart": "https://www.flipkart.com/realme-narzo-60x-5g-stellar-green-128-gb/p/itm906a3c913a97f?pid=MOBGTJCKHSEFZC4G",
            "amazon": "https://www.amazon.in/realme-5G%EF%BC%88Stellar-External-Segments-Supervooc/dp/B0CGDQ9SN7?th=1",
            "croma": None
        },
        {
            "name": "OnePlus 10 Pro",
            "flipkart": "https://www.flipkart.com/oneplus-10-pro-5g-volcanic-black-128-gb/p/itm3ef418a3c7510",
            "amazon": "https://www.amazon.in/OnePlus-Volcanic-Black-128GB-Storage/dp/B09V2P9C3S",
            "croma": "https://www.croma.com/oneplus-10-pro-5g-8gb-ram-128gb-volcanic-black-/p/250719"
        }
    ],
    "Laptops": [
        {
            "name": "HP Victus Gaming Laptop",
            "flipkart": "https://www.flipkart.com/hp-victus-intel-core-i5-12th-gen-16-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-2050-15-fa1351tx-gaming-laptop/p/itm9ad6649afe111",
            "amazon": "https://www.amazon.in/HP-Victus-Processor-Graphics-15-fa0070TX/dp/B0D2DDJ6PJ?th=1",
            "croma": "https://www.croma.com/hp-victus-fa0998tx-intel-core-i5-12th-gen-15-inch-16gb-512gb-windows-11-ms-office-2021-nvidia-geforce-rtx-3050-graphics-full-hd-ips-display-performance-blue-805x4pa-/p/272249"
        },
        {
            "name": "ASUS TUF Gaming Laptop",
            "flipkart": "https://www.flipkart.com/asus-tuf-gaming-f15-core-i5-10th-gen-16-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-ti-144-hz-fx506li-hn279t-laptop/p/itm8bdedba0dbeb6",
            "amazon": "https://www.amazon.in/ASUS-SmartChoice-i5-11400H-GeForce-FX506HF-HN025W/dp/B0C27SD9YR?th=1",
            "croma": "https://www.croma.com/asus-tuf-gaming-f15-fx507zc4-hn116ws-intel-core-i5-12th-gen-gaming-laptop-16gb-512gb-ssd-windows-11-home-4gb-gddr6-15-6-inch-fhd-ips-display-ms-office-2021-mecha-gray-2-2kg-/p/275951"
        }
    ],
    "Smart Watches": [
        {
            "name": "Fire Boltt Phoenix Pro",
            "flipkart": "https://www.flipkart.com/fire-boltt-phoenix-pro-1-39-bluetooth-calling-smartwatch-ai-voice-assistant-metal-body-smartwatch/p/itme77bb8112a0f9?pid=SMWGWFHHFU3XSRP6",
            "amazon": "https://www.amazon.in/Fire-Boltt-Bluetooth-Smartwatch-Assistant-Monitoring/dp/B0BRKXXPZ7",
            "croma": "https://www.croma.com/fire-boltt-phoenix-pro-smartwatch-with-bluetooth-calling-35-3mm-hd-display-ip67-water-resistant-black-strap-/p/305130"
        },
        {
            "name": "Noise Vortex Plus",
            "flipkart": "https://www.flipkart.com/noise-noisefit-vortex-plus-smartwatch/p/itmff55443513f97?pid=SMWH889NQAZBMHJR",
            "amazon": "https://www.amazon.in/Noise-Launched-Display-Calling-Battery/dp/B0CG1WKV3W?th=1",
            "croma": None
        }
    ]
}

# ==== Category Selection ====
print("📂 Categories:")
category_names = list(categories.keys())
for i, cat in enumerate(category_names, 1):
    print(f"{i}. {cat}")

try:
    cat_choice = int(input("\nSelect a category number: "))
    assert 1 <= cat_choice <= len(category_names)
except:
    print("❌ Invalid category choice.")
    exit()

selected_category = category_names[cat_choice - 1]
products = categories[selected_category]

# ==== Product Selection ====
print(f"\n📦 Products in '{selected_category}':")
for i, product in enumerate(products, 1):
    print(f"{i}. {product['name']}")

try:
    prod_choice = int(input("\nSelect a product number: "))
    assert 1 <= prod_choice <= len(products)
except:
    print("❌ Invalid product choice.")
    exit()

selected_product = products[prod_choice - 1]
print(f"\n🔍 You selected: {selected_product['name']}")

# ==== WebDriver Setup ====
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# ==== Flipkart ====
print("\n🛒 Flipkart:")
try:
    driver.get(selected_product["flipkart"])
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.B_NuCI"))).text
    price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._30jeq3._16Jk6d"))).text
    print(f"✅ {name} - {price}")
except Exception as e:
    print(f"❌ Flipkart error: {e}")

# ==== Amazon ====
print("\n🛍️ Amazon:")
try:
    driver.get(selected_product["amazon"])
    name = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text.strip()
    try:
        price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-price span.a-offscreen"))).text
    except:
        price = wait.until(EC.presence_of_element_located((By.ID, "priceblock_dealprice"))).text
    print(f"✅ {name} - {price}")
except Exception as e:
    print(f"❌ Amazon error: {e}")

# ==== Croma ====
print("\n🏬 Croma:")
if selected_product["croma"]:
    try:
        driver.get(selected_product["croma"])
        name = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
        price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "amount"))).text
        print(f"✅ {name} - ₹{price}")
    except Exception as e:
        print(f"❌ Croma error: {e}")
else:
    print("ℹ️ No Croma link available.")

# ==== Done ====
driver.quit()
print("\n✅ Price comparison complete. Browser closed.")
