import requests

url = 'https://www.eghtesadnews.com/markets/euro'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
euro_value = soup.find('td',text='تاریخ').find_next('td').text


toman_value = int(input('gheimat be toman:'))
euro_value = euro_value[0:2]
final_value = toman_value/int(euro_value)

print(final_value)