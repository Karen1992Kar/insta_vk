
import  re


text = """['\ufeff--------------------------', '-- Поиск ID у Instagram-аккаунтов по списку логинов в Инстаграме', 
'-- Расчёт выполнен при помощи сервиса https://vk.barkov.net/instagramid.aspx', '---/
-----------------------', '-- Просмотрено: 9 человек', '-- Instagram ID найден у 8 человек', '---------------------',
 '4140382325', '2159987149', '3546778913', '9002460298', '183348332/
4', '5722460741', '8387770910', '11085304520']/True/['\ufeff--------------------------', '-- Поиск ID у 
Instagram-аккаунтов по списку логинов в Инстаграме', '-- Расчёт выполнен при помощи сервиса 
https://vk.barkov.net/instagramid.aspx', '---/
-----------------------', '-- Просмотрено: 9 человек', '-- Instagram ID найден у 8 человек', '----------------------',
 '39125038002', '1435883725', '3936046301', '9312580237', '72351162/
72', '34814892927', '6607581001', '25301588380']/
True
"""

regex_virajeniya = r"..+"
a = re.findall(regex_virajeniya, text)


print(a)