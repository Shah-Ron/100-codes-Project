import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    """
    To fetch the data from the URL
    """

    # Requests the data from URL
    response = requests.get(url)

    # Checks whether the status code is 200, i.e. access provided
    if response.status_code == 200:

        # Parsing the HTML content to text
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:   # If no access return None
        return None
    
def find_data(soup, keyword):
    """
    To find the data according to the specific keyword
    """

    # Finds all the elelments containing the keyword
    results = soup.find_all(string = lambda text: keyword.lower() in text.lower())
    return results

def print_results(search_results):
    """
    Prints the elements with the keyword
    """
    if search_results:
                
         # Prints all the texts related to the keyword
        print("Found matching results:")
        for results in search_results:
            result =  results.strip()
            if "{" in result:
                continue
            else:
                print(result.strip())
        else:   # For no results related to the keyword
            print("There are no elements containing that Keyword")
    else:       # For not returning any data from the URL
            print("Failed to fetch data from the URL")

def option1(url):
    """
    Calls this function when the Option 1 is chosen as input
    """
    # Checks whether the given URL starts with http, making sure we are given a URL itself
    if url.startswith("http"):

        #Calls the fetch_data function to get all the text data from the URL
        soup = fetch_data(url)

        # Checking whether they URL provided some text data
        if soup:
            
            # Inputs the keyword to search for
            keyword = input("Enter the keyword to search on the webpage : ")

            # Calls the find_data function to get all the text data related to the keyword
            search_result = find_data(soup, keyword)
            print_results(search_result)
            # Checking whether there was any such keyword
            
    else:           # For not providing a proper URL
        print("Provide an actual URL")

def option2(url):
    """
    Calls this function when the Option 2 is chosen as input
    """
    keyword = input("Enter the keyword to search on the webpage : ")
    search_url = url + "Special:Search?search=" + keyword
    soup = fetch_data(search_url)
    if soup:
        search_result = find_data(soup, keyword)
        print_results(search_result)


def main():
    """
    Inputs the URL and keyword and prints the data collected
    """

    print("Do you have a URL or do you want to scrape from Wikipedia")
    option = int(input("Choose 1 for URL and 2 for Wikipedia: "))

    if option == 1:
        # Inputs the URL
        url = input("Enter the URL : ")
        option1(url)
    elif option == 2:
        # Wikipedia URL
        url ="https://en.wikipedia.org/wiki/"
        option2(url)
    else:
        print("Provide a proper option")
    
    

if __name__ == "__main__":
    main()