# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# # browser setup
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
#
# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()),
#     options=options
# )
#
# # ecommerce site URL
# driver.get("https://chaldal.com")
# time.sleep(5)  # page load wait
#
# print("\n[INFO] Scraping first category only...\n")
#
# # Step 1: get all categories
# categories = driver.find_elements(By.CLASS_NAME, "category-name")
# if not categories:
#     print("[WARNING] No categories found!")
#     driver.quit()
#     exit()
#
# # take the first category
# first_category = categories[0]
# cat_name = first_category.text.strip()
# print(f"[INFO] First category: {cat_name}\n")
# # ------------------- START MULTI-CATEGORY LOOP -------------------
# categories = driver.find_elements(By.CLASS_NAME, "category-name")
# total_categories = len(categories)
# print(f"[INFO] Total categories found: {total_categories}")
#
# def open_home():
#     driver.get("https://chaldal.com")
#     time.sleep(4)
#
# def get_categories():
#     return driver.find_elements(By.CLASS_NAME, "category-name")
#
# open_home()
#
# for cat in get_categories():
#     cat_name = cat.text.strip()
#     if not cat_name:
#         continue
#
#     open_home()
#     cats = get_categories()
#
#     # re-find same category fresh
#     for c in cats:
#         if c.text.strip() == cat_name:
#             driver.execute_script("arguments[0].click();", c)
#             break
#
#     time.sleep(3)
#
#     products = driver.find_elements(By.CLASS_NAME, "productV2Catalog")
#
#     # 👉 parent category
#     if len(products) == 0:
#         subcats = get_categories()
#
#         for sub in subcats:
#             sub_name = sub.text.strip()
#             if not sub_name:
#                 continue
#
#             open_home()
#
#             # go cat → subcat
#             for c in get_categories():
#                 if c.text.strip() == cat_name:
#                     driver.execute_script("arguments[0].click();", c)
#                     break
#
#             time.sleep(2)
#
#             for s in get_categories():
#                 if s.text.strip() == sub_name:
#                     driver.execute_script("arguments[0].click();", s)
#                     break
#
#             time.sleep(3)
#
#             # 🔥 HERE scrape products
#             # product scraping block stays SAME
#
#     else:
#         # 🔥 HERE scrape products
#         pass
#
#     #  product scraping stays EXACTLY same here
#
#     for t_index, card in enumerate(product_cards, start=1):
#         try:
#             try:
#                 card.click(); time.sleep(1)
#             except:
#                 pass
#
#             try:
#                 title = card.find_element(By.CLASS_NAME, "nameTextWithEllipsis").text.strip()
#             except:
#                 title = ""
#
#             try:
#                 old_price = card.find_element(By.CSS_SELECTOR, "div.price > span").text.strip()
#             except:
#                 old_price = ""
#
#             try:
#                 new_price = card.find_element(By.CSS_SELECTOR, "div.price + span").text.strip()
#             except:
#                 new_price = ""
#
#             try:
#                 img_src = card.find_element(By.TAG_NAME, "img").get_attribute("src")
#             except:
#                 img_src = ""
#
#             print(f"{t_index}. [{cat_name}] {title} | Old:৳{old_price} | New:৳{new_price} | Img: {img_src}")
#
#         except Exception as e:
#             print(f"[WARNING] Could not scrape product {t_index} in {cat_name}: {e}")
#
#     driver.get("https://chaldal.com")
#     time.sleep(5)
#
# print("\n[DONE] First category products scraped.\n")
# product_cards2 = driver.find_elements(By.CLASS_NAME, "category")
# for res in product_cards2:
#     print(res.text)
# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

csv_file = open("data.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Category", "Subcategory", "Title", "Old Price", "New Price", "Image URL"])

# browser setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ecommerce site URL
driver.get("https://chaldal.com")
time.sleep(5)  # page load wait

print("\n[INFO] Scraping first category only...\n")

# Step 1: get all categories
categories = driver.find_elements(By.CLASS_NAME, "category-name")
if not categories:
    print("[WARNING] No categories found!")
    driver.quit()
    exit()


# take the first category
first_category = categories[0]
cat_name = first_category.text.strip()
print(f"[INFO] First category: {cat_name}\n")
# ------------------- START MULTI-CATEGORY LOOP -------------------
categories = driver.find_elements(By.CLASS_NAME, "category-name")
total_categories = len(categories)
print(f"[INFO] Total categories found: {total_categories}")

for c_index in range(total_categories):
    categories = driver.find_elements(By.CLASS_NAME, "category-name")  # fresh fetch
    category = categories[c_index]
    cat_name = category.text.strip()
    if not cat_name:
        continue

    try:
        category.click()
        time.sleep(3)
    except:
        print(f"[WARNING] Could not click category: {cat_name}")
        continue


    # Step 2: find all product cards in this category
    product_cards = driver.find_elements(By.CLASS_NAME, "productV2Catalog")
    total_cards = len(product_cards)

    # check for sub-categories if no products found
    # check for sub-categories if no products found
    # after finding product_cards
    if len(product_cards) == 0:
        # 0 product → check for subcategories
        subcats = driver.find_elements(By.CLASS_NAME, "category-name")
        for sc_index in range(len(subcats)):
            subcats = driver.find_elements(By.CLASS_NAME, "category-name")  # fresh fetch
            subcat = subcats[sc_index]
            sub_name = subcat.text.strip()
            if not sub_name:
                continue

            # click subcategory
            try:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", subcat)
                driver.execute_script("arguments[0].click();", subcat)
                time.sleep(2)
            except:
                continue

            # check for products in subcategory
            product_cards = driver.find_elements(By.CLASS_NAME, "productV2Catalog")
            if len(product_cards) == 0:
                # recursive-ish → aro subcategories thakle ei same block run korte pare
                # ekdom serial, ekta kore
                # queue logic or for-loop diye abar same block
                continue

                # ager moto scraping logic start
            for t_index, card in enumerate(product_cards, start=1):
                try:
                    try:
                        card.click(); time.sleep(1)
                    except:
                        pass

                    try:
                        title = card.find_element(By.CLASS_NAME, "nameTextWithEllipsis").text.strip()
                    except:
                        title = ""

                    try:
                        old_price = card.find_element(By.CSS_SELECTOR, "div.price > span").text.strip()
                    except:
                        old_price = ""

                    try:
                        new_price = card.find_element(By.CSS_SELECTOR, "div.price + span").text.strip()
                    except:
                        new_price = ""

                    try:
                        img_src = card.find_element(By.TAG_NAME, "img").get_attribute("src")
                    except:
                        img_src = ""

                    print(
                        f"{t_index}. [{cat_name} → {sub_name}] {title} | Old:৳{old_price} | New:৳{new_price} | Img: {img_src}")

                except Exception as e:
                     print( csv_writer.writerow([cat_name, sub_name if 'sub_name' in locals() else "", title, old_price, new_price, img_src]))

    driver.get("https://chaldal.com")
    time.sleep(5)

print("\n[DONE] First category products scraped.\n")
product_cards2=driver.find_elements(By.CLASS_NAME, "category")
for res in product_cards2:
    print(res.text)
driver.quit()
csv_file.close()
