import json
from datetime import datetime
import csv
class NewsFormatter:
    """
    This class performs formatting of a JSON file into HTML format, 
    extracts data from the JSON file to a text file, and to a CSV file
    """
    def __init__(self, type,print_message):
        """
        Construct a new class NewsFormatter object.
        :param type: "This is the type into which the JSON file will be formatted
        :param print_message: This is a lambda function for printing        
        :return: no return value
        """
        self.type = type
        self.print_mess=print_message
        self.print_mess("Initializing News Formatter...")

    def format(self):
        """
        This is a method for formatting a JSON file into an HTML file. The result is written into index.html.
        :return: no return value
        """
        if(self.type == "html"):
            news_json=""
            try:
                with open('news.json') as json_file:
                    news_json = json.load(json_file)
            except Exception:
                self.print_mess("Unsuccessful file opening")
            finally:
                json_file.close()
            html_head = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                    <title>PyNews</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
                    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.3/dist/jquery.slim.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
                    </head>
                    <body>
                    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
                    <!-- Brand/logo -->
                    <a class="navbar-brand" href="#">PyNews - Vijesti koje su Vama važne</a>
                    </nav>
                    <div class="container-fluid" style="width=100%">
                """

            html_news_cards = ""
            #Generate cards from JSON news file
            for news_log in news_json:
                html_card = """
                <br>
                <div class="card card-default" style="width: 100%;">
                <div class="card-body">
                """
                html_card += '<h5 class="card-title">'+ news_log.get("title") +'</h5>'
                html_card += '<h6 class="card-subtitle mb-2 text-muted"><h6>'+ news_log.get("pubDate") +'</h6>'
                html_card += '<p class="card-text">'+ news_log.get("description") +'</p>'
                html_card += ''
                html_card += '</div><div class="card-body"><br><a href="'+ news_log.get("link") +'" class="btn btn-primary">Otvori članak</a></div></div><br>'
                html_news_cards += html_card

            html_tail = """
                </div>
                </body>
                </html>
            """
            
            #Write html content to a html file
            self.print_mess("Generating HTML file...")
            try:
                f = open("./output/" + "index.html", "w", encoding='utf-8')
                f.write(html_head + html_news_cards + html_tail)
            except Exception:
                self.print_mess("Failed to write to the file")
            finally:
                f.close()
            
    def format_txt(self):
        """
        This is a method for formatting a JSON file into an .txt file. The result is written into news.txt.
        :return: no return value
        """
        news_json=""
        try:
            with open('news.json') as json_file:
                news_json = json.load(json_file)
        except Exception:
            self.print_mess("Unsuccessful file opening")
        finally:
            json_file.close()
        txt_content = ""
        for news in news_json:
            if news.get("title") is not None and news.get("pubDate") is not None and news.get("description") is not None and news.get("link") is not None:
                title = news.get("title")
                pubDate = news.get("pubDate")
                description1 = news.get("description")
                description=""
                if "," in description1:
                    description=description1.split(",")
                else:
                    description=description1
                link = news.get("link")
                part1 = description[:len(description)//2]
                part2 = description[len(description)//2:]    
                # Formatiranje teksta
                txt_vest_1 = f"{'='*80}\n{title}\n{'='*80}\nDatum i vrijeme objavljivanja ({pubDate})\n"
                txt_vest_2 = f"{'-'*80}\nKratak sadržaj vijesti\n{part1}\n{part2}\n{'-'*80}\nlink\n{link}\n{'='*80}\n\n"

                txt_content += txt_vest_1+txt_vest_2

        # Upisivanje teksta u tekstualni dokument
        self.print_mess("Generating .txt file...")
        try:
            f = open("./output/" + "news.txt", "w", encoding='utf-8')
            f.write(txt_content)
        except Exception:
            self.print_mess("Failed to write to the file")
        finally:
            f.close()


    def generate_csv(self):
        """
        This is a method for formatting a JSON file into an CSV file. The result is written into news.csv.
        :return: no return value
        """
        news_json=""
        try:
            with open('news.json') as json_file:
                news_json = json.load(json_file)
        except Exception:
            self.print_mess("Unsuccessful file opening")
        finally:
            json_file.close()
        self.print_mess("Generating CSV file...")
        try:
            with open("./output/" + "news.csv", "w", newline='', encoding='utf-8') as csvfile:
                fields = ["naslov", "opis", "link", "datum_objavljivanja"]
                writer = csv.DictWriter(csvfile, fieldnames=fields)

                # Upisivanje zaglavlja u CSV fajl
                writer.writeheader()

                # Upisivanje podataka u CSV fajl
                for news in news_json:
                    title = news.get("title")
                    pubDate = news.get("pubDate")
                    description = news.get("description")
                    link = news.get("link")

              
                    # Upisivanje reda u CSV fajl
                    row={"naslov": title, "opis": description, "link": link, "datum_objavljivanja": pubDate}
                    writer.writerow(row)
        except Exception:
            self.print_mess("Failed to write to CSV file")
        finally:
            csvfile.close()
            
#print_message = lambda message: print(f"===> {message}")
#newsFormatter = NewsFormatter("html",print_message)
#newsFormatter.format()
#newsFormatter.format_txt()
#newsFormatter.generate_csv()