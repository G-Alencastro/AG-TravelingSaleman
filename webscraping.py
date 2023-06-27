from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.rotamapas.com.br/')

def search_dis(city01, city02):
    driver.get('https://www.rotamapas.com.br/')

    sleep(1)
    start_search_button = driver.find_element(By.ID, 'search-start')
    end_search_button = driver.find_element(By.ID, 'search-end')
    submit_button = driver.find_element(By.ID, 'submitBtn')

    start_search_button.clear()
    end_search_button.clear()

    start_search_button.send_keys(city01)
    sleep(3)
    end_search_button.send_keys(city02)
    sleep(3)
    submit_button.click()

    distancia_km_text = driver.find_element(By.ID, 'distancia-km')
    distancia_reta_text = driver.find_element(By.ID, 'reta-viagem')
    
    sleep(3)

    distancia_km = distancia_km_text.text[:-3]
    reta_km = distancia_reta_text.text[:-3]

    return distancia_km, reta_km
    

if __name__ == '__main__':
    dis = []
    line_dis = []
    citys = ('Boa Vista','Macapá','Manaus',)
    for i in range(len(citys)):
        actual_city_dis_list = []
        actual_city_line_list = []
        for c in range(i+1, len(citys)):
            actual_city_dis_list.append(search_dis(citys[i], citys[c])[0])
            actual_city_line_list.append(search_dis(citys[i], citys[c])[1])

        dis.append(actual_city_dis_list)
        line_dis.append(actual_city_dis_list)

print(dis)
print()
print(line_dis)