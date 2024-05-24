import web_crawler as wc
import news_parser as np
import news_formatter as nf
from datetime import date
import json

#Get current date
today = date.today()
# dd/mm/YY
formatted_date = today.strftime("%d.%m.%Y")
print_message = lambda message: print(f"{message}")
#Open sources.json to read all of the sources to be parsed
try:
    with open('settings.json') as json_file:
        config = json.load(json_file)
except Exception:
    print_message("Failed to read the file")
finally:
    json_file.close()

print_message("============= PyNews " + formatted_date + " =============")
webCrawler = wc.WebCrawler(print_message)
webCrawler.getAllRawData()
newsParser = np.NewsParser(config,print_message)
newsParser.parse()
newsFormatter = nf.NewsFormatter("html",print_message)
#newsFormatter.format()
newsFormatter.format_txt()
newsFormatter.generate_csv()
print_message("==================== Done! ==================")