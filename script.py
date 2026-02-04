from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# ================= CSV =================
# ================= CSV =================

csv_file = open("ankon.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Category", "Subcategory", "Title", "Old Price", "New Price", "Image URL"])

# ================= LINKS =================
CATEGORY_LINKS = [
    "https://chaldal.com/fruits-vegetables",
    "https://chaldal.com/fresh-vegetable",
    "https://chaldal.com/fresh-fruit",
    "https://chaldal.com/meat-fish",
    "https://chaldal.com/chicken-poultry",
    "https://chaldal.com/premium-perishables",
    "https://chaldal.com/frozen-fish",
    "https://chaldal.com/meat-new",
    "https://chaldal.com/tofu-meat-alternatives",
    "https://chaldal.com/dried-fish",
    "https://chaldal.com/cooking",
    "https://chaldal.com/spices",
    "https://chaldal.com/salt-sugar",
    "https://chaldal.com/rices",
    "https://chaldal.com/dal-or-lentil",
    "https://chaldal.com/ready-mix",
    "https://chaldal.com/shemai-suji",
    "https://chaldal.com/miscellaneous",
    "https://chaldal.com/oil",
    "https://chaldal.com/colors-flavours",
    "https://chaldal.com/ghee",
    "https://chaldal.com/premium-ingredients",
    "https://chaldal.com/tomato-sauces",
    "https://chaldal.com/pickles",
    "https://chaldal.com/cooking-sauces",
    "https://chaldal.com/other-sauces",
    "https://chaldal.com/eggs",
    "https://chaldal.com/powder-milk",
    "https://chaldal.com/liquid-uht-milk",
    "https://chaldal.com/yogurt",
    "https://chaldal.com/cheeses",
    "https://chaldal.com/condensed-milk-cream",
    "https://chaldal.com/butter-sour-cream",
    "https://chaldal.com/eggs-2",
    "https://chaldal.com/breads",
    "https://chaldal.com/tea-coffee-2",
    "https://chaldal.com/local-breakfast",
    "https://chaldal.com/cereals",
    "https://chaldal.com/honey",
    "https://chaldal.com/spreads-syrups",
    "https://chaldal.com/energy-boosters",
    "https://chaldal.com/jams-jellies",
    "https://chaldal.com/chocolates",
    "https://chaldal.com/wafers",
    "https://chaldal.com/candies",
    "https://chaldal.com/mints-mouth-fresheners",
    "https://chaldal.com/halal-marshmallows",
    "https://chaldal.com/noodles",
    "https://chaldal.com/cookies-2",
    "https://chaldal.com/local-snacks",
    "https://chaldal.com/chips-pretzels",
    "https://chaldal.com/plain-biscuits",
    "https://chaldal.com/toast-biscuits",
    "https://chaldal.com/cream-biscuits",
    "https://chaldal.com/pasta-macaroni",
    "https://chaldal.com/soups",
    "https://chaldal.com/popcorn-nuts",
    "https://chaldal.com/salted-biscuits",
    "https://chaldal.com/cakes",
    "https://chaldal.com/salad-dressing",
    "https://chaldal.com/beverages-tea",
    "https://chaldal.com/soft-drinks",
    "https://chaldal.com/coffees",
    "https://chaldal.com/powder-mixes",
    "https://chaldal.com/juice",
    "https://chaldal.com/water",
    "https://chaldal.com/flour",
    "https://chaldal.com/nuts-dried-fruits",
    "https://chaldal.com/baking-ingredients",
    "https://chaldal.com/baking-tools",
    "https://chaldal.com/baking-mixes",
    "https://chaldal.com/dish-wash",
    "https://chaldal.com/laundry",
    "https://chaldal.com/toilet-cleaning",
    "https://chaldal.com/paper-products",
    "https://chaldal.com/pest-control",
    "https://chaldal.com/floor-glass-cleaners",
    "https://chaldal.com/cleaning-accessories",
    "https://chaldal.com/air-freshners",
    "https://chaldal.com/trash-bags",
    "https://chaldal.com/shoe-care",
    "https://chaldal.com/trash-bin-basket",
    "https://chaldal.com/kitchen-accessories",
    "https://chaldal.com/kitchen-appliances",
    "https://chaldal.com/lights-electrical",
    "https://chaldal.com/lights",
    "https://chaldal.com/mosquito-swatter",
    "https://chaldal.com/electric-multiplug",
    "https://chaldal.com/electronics",
    "https://chaldal.com/tools-hardware",
    "https://chaldal.com/baskets-buckets",
    "https://chaldal.com/box-container",
    "https://chaldal.com/gardening",
    "https://chaldal.com/rack-organizer",
    "https://chaldal.com/disposables",
    "https://chaldal.com/medium-2",
    "https://chaldal.com/large-2",
    "https://chaldal.com/extra-large-15-kg-diapers",
    "https://chaldal.com/small-2",
    "https://chaldal.com/newborn-2",
    "https://chaldal.com/milk-juice-drinks",
    "https://chaldal.com/toddler-food",
    "https://chaldal.com/formula",
    "https://chaldal.com/womens-soaps",
    "https://chaldal.com/hair-care",
    "https://chaldal.com/female-shampoo",
    "https://chaldal.com/feminine-care",
    "https://chaldal.com/female-moisturizer",
    "https://chaldal.com/face-wash-scrub",
    "https://chaldal.com/female-deo",
    "https://chaldal.com/womens-perfume",
    "https://chaldal.com/womens-shower-gel",
    "https://chaldal.com/masks-cleansers",
    "https://chaldal.com/serum-oil-toners",
    "https://chaldal.com/mens-soaps",
    "https://chaldal.com/mens-perfume",
    "https://chaldal.com/shampoo",
    "https://chaldal.com/shaving-needs",
    "https://chaldal.com/beard-grooming",
    "https://chaldal.com/deodorants",
    "https://chaldal.com/razors-blades",
    "https://chaldal.com/mens-hair-care",
    "https://chaldal.com/lotion-cream",
    "https://chaldal.com/mens-facewash",
    "https://chaldal.com/mens-shower-gels",
    "https://chaldal.com/liquid-handwash",
    "https://chaldal.com/hand-sanitizer",
    "https://chaldal.com/toothpastes",
    "https://chaldal.com/toothbrushes",
    "https://chaldal.com/mouthwash-others",
    "https://chaldal.com/soaps",
    "https://chaldal.com/lotions",
    "https://chaldal.com/petroleum-jelly",
    "https://chaldal.com/creams",
    "https://chaldal.com/face-wash-mask",
    "https://chaldal.com/body-hair-oil",
    "https://chaldal.com/lipsticks-lip-balm",
    "https://chaldal.com/batteries",
    "https://chaldal.com/calculators",
    "https://chaldal.com/glue-tapes",
    "https://chaldal.com/stapler-punch",
    "https://chaldal.com/organizing-accessories",
    "https://chaldal.com/cutting-2",
    "https://chaldal.com/file-folder",
    "https://chaldal.com/measuring",
    "https://chaldal.com/desk-organizers",
    "https://chaldal.com/bird-food",
    "https://chaldal.com/keto-food",
    "https://chaldal.com/antiseptics",
]


# ================= DRIVER =================
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--headless")  # headless mode on
options.add_argument("--disable-gpu")  # optional, Windows এ দরকার হতে পারে
options.add_argument("--window-size=1920,1080")  # full page rendering এর জন্য

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ================= HELPERS =================
def full_scroll():
    last = 0
    stall = 0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)
        cards = driver.find_elements(By.CLASS_NAME, "productV2Catalog")
        if len(cards) > last:
            last = len(cards)
            stall = 0
        else:
            stall += 1
        if stall >= 3:
            break

# ================= MAIN =================
print("\n[INFO] Scraping started...\n")

for link in CATEGORY_LINKS:
    driver.get(link)
    time.sleep(4)

    category = link.split("/")[-1].replace("-", " ").title()
    subcategory = category

    print(f"\n[OPENED] {category}\n")

    full_scroll()
    cards = driver.find_elements(By.CLASS_NAME, "productV2Catalog")

    for idx, card in enumerate(cards, start=1):
        try:
            try:
                title = card.find_element(By.CLASS_NAME, "nameTextWithEllipsis").text.strip()
            except:
                title = ""

            try:
                old_price = card.find_element(By.CSS_SELECTOR, "div.price > span").text.strip()
            except:
                old_price = ""

            try:
                new_price = card.find_element(By.CSS_SELECTOR, "div.currency + span").text.strip()
            except:
                new_price = ""

            try:
                img = card.find_element(By.TAG_NAME, "img").get_attribute("src")
            except:
                img = ""

            csv_writer.writerow([category, subcategory, title, old_price, new_price, img])
            csv_file.flush()  # flush করে দিলে runtime-এ CSV update হয়

            print(f"{idx}. [{category}] {title}")
            print(f"    Old: ৳{old_price} | New: ৳{new_price}")
            print(f"    Image: {img}\n")

        except Exception as e:
            print("ERROR:", e)

print("\n✅ DONE — Data printed & saved\n")

driver.quit()
csv_file.close()
