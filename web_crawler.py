import json
import urllib.request
import ssl
class WebCrawler:
    """
    This class encapsulates data and functionalities for fetching raw
    data from the internet.
    """
    def __init__(self,print_message):
        self.print_mess=print_message
        """
        Construct a new WebCrawler object.

        :return: no return value
        """
        self.print_mess("Initializing Web Crawler...")

    def getAllRawData(self):
        """
        Get raw content from the internet and store data from sources into
        separate files.

        :return: no return value
        """
        ssl_context = ssl._create_unverified_context()
        sources_data=""
        try:
            with open('sources.json') as json_file:
                sources_data = json.load(json_file)
        except Exception:
            self.print_mess("Unsuccessful file opening")
        finally:
            json_file.close()
        self.print_mess("Parsing sources...")
        #Loop through all sources and store raw data to separate files.
        for source_record in sources_data:
            self.print_mess("Parsing source: " + source_record.get("tag") + " ...")
            file = urllib.request.urlopen(source_record.get("address"), context=ssl_context)
            content_bytes = file.read()
            content_txt = content_bytes.decode("utf8")
            file.close()
            #Write content to a temp file
            self.print_mess("Writing fetched content to file...")
            try:
                f = open("./temp_files/" + source_record.get("tag") + ".txt", "w",encoding='utf-8')
                f.write(content_txt)
            except Exception:
                self.print_mess("Failed to write to the file...")
            finally:
                f.close()
        self.print_mess("Web Crawler - done.")

#print_message = lambda message: print(f"===> {message}")
#wb=WebCrawler(print_message)
#wb.getAllRawData()