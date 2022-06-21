
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys





distance= input("Enter total distance for driver, remeber to include where they're driving from:   ")
distance = float(distance)

payout = input("Enter payout:   ")
payout = float(payout)

gas_price = input("enter the gas price per gallon:    ")

"""""
baseURL = "http://www.gasbuddy.com/"

browser = webdriver.Chrome(executable_path=geckodriver)
zipcode = gas_price

browser.get(baseURL)
elem = browser.find_element_by_id("ctl00_Content_GBZS_txtZip").send_keys(zipcode)
elem = browser.find_element_by_id("ctl00_Content_GBZS_btnSearch").click()
"""""

gas_price = float(gas_price)


miles_per_gallon = input("Enter miles per gallon:   ")
miles_per_gallon = float(miles_per_gallon)

##### connect to api you bum

dxg = distance * gas_price

cost_per_distance = dxg / miles_per_gallon




adj_payout = payout - cost_per_distance

res = "{:.2f}".format(adj_payout)

print(res)



print(f"The driver's adjusted payout is ${res}")
