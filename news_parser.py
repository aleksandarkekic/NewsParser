import xml.etree.ElementTree as ET
import json

class NewsParser:
    """
    This method is a news parser. It receives information about news sources from file 'sources.json'. 
    After parsing, it saves the content to a JSON file
    """
    def __init__(self, config,print_message):
        """
        Construct a new class NewsParser object.
        :param config: This data is read from the settings.json file and provides information about the number of news articles to be accepted 
        from each source and the name of the file in which the parsed news will be saved.
        :param print_message: This is a lambda function for printing        
        :return: no return value
        """
        self.config = config
        self.print_mess=print_message
        self.print_mess("Initializing parser...")

    def parse(self):
        """
         This method parses the content from XML files and writes the parsed content to a JSON file news.json
         :return: no return value
        """
        sources_data=""
        try:
            with open('sources.json') as json_file:
                sources_data = json.load(json_file)
        except Exception:
            self.print_mess("Unsuccessful file opening")
        finally:
            json_file.close()
        news = []
        #Loop through raw content files and extract and format data
        for source_record in sources_data:
            try:
                f = open("./temp_files/"+source_record.get("tag")+".txt", "r",encoding='utf-8')
                source_txt = f.read();
            except Exception:
                self.print_mess("Unsuccessful file opening and reading")
            finally:
                f.close()
            #Source-specific parsing
            if(source_record.get("tag")=="rtrs"):
                tree=""
                try:
                    self.print_mess("Parsing news from "+ source_record.get("description"))
                    #Parsing XML file type
                    tree = ET.parse("./temp_files/"+source_record.get("tag")+".txt")
                    root = tree.getroot()
                    #Parsing desired number of news
                    number_of_news = self.config.get("number_of_news_per_source") + 5
                    for index in range(5, number_of_news):
                        news_log = {}
                        for x in root[0][index]:
                            if(x.tag != "guid"):
                                #Add record to news_log dictionary
                                news_log[x.tag] = x.text
                        #Add news_log dictionary to an array of all news
                        news.append(news_log)
                except FileNotFoundError as file_not_found_error:
                    self.print_mess(f"Error: {file_not_found_error}. File not found.")
                except ET.ParseError as parse_error:
                    self.print_mess(f"Error while parsing XML: {parse_error}")
                except Exception as general_error:
                    self.print_mess(f"An unexpected error occurred: {general_error}") 
                finally:
                    pass
            elif(source_record.get("tag")=="naslovi"):
                tree=""
                try:
                    self.print_mess("Parsing news from "+ source_record.get("description"))
                    #Parsing XML file type
                    tree = ET.parse("./temp_files/"+source_record.get("tag")+".txt")
                    root = tree.getroot()
                    #Parsing desired number of news
                    number_of_news = self.config.get("number_of_news_per_source") + 5
                    for index in range(5, number_of_news):
                        news_log = {}
                        for x in root[0][index]:
                            if(x.tag != "guid"):
                                #Add record to news_log dictionary
                                news_log[x.tag] = x.text
                        #Add news_log dictionary to an array of all news
                        news.append(news_log)
                except FileNotFoundError as file_not_found_error:
                    self.print_mess(f"Error: {file_not_found_error}. File not found.")
                except ET.ParseError as parse_error:
                    self.print_mess(f"Error while parsing XML: {parse_error}")
                except Exception as general_error:
                    self.print_mess(f"An unexpected error occurred: {general_error}") 
                finally:
                    pass
            elif(source_record.get("tag")=="vesti"):
                tree=""
                try:
                    self.print_mess("Parsing news from "+ source_record.get("description"))
                    #Parsing XML file type
                    tree = ET.parse("./temp_files/"+source_record.get("tag")+".txt")
                    root = tree.getroot()
                    #Parsing desired number of news
                    number_of_news = self.config.get("number_of_news_per_source") + 5
                    for index in range(5, number_of_news):
                        news_log = {}
                        for x in root[0][index]:
                            if(x.tag != "guid"):
                                #Add record to news_log dictionary
                                news_log[x.tag] = x.text
                        #Add news_log dictionary to an array of all news
                        news.append(news_log)
                #Save all news array to a JSON file
                except FileNotFoundError as file_not_found_error:
                    self.print_mess(f"Error: {file_not_found_error}. File not found.")
                except ET.ParseError as parse_error:
                    self.print_mess(f"Error while parsing XML: {parse_error}")
                except Exception as general_error:
                    self.print_mess(f"An unexpected error occurred: {general_error}") 
                finally:
                    pass
            self.print_mess("==>Creating news.json ...")
            try:
                f = open("news.json", "w")
                f.write(json.dumps(news, indent=2))
            except Exception:
                self.print_mess("Failed to write t")
            f.close()
            self.print_mess("News Parser - done.")
            
#print_message = lambda message: print(f"===> {message}")           
#with open('settings.json') as json_file:
#    config = json.load(json_file)               
#ns=NewsParser(config,print_message)
#ns.parse()