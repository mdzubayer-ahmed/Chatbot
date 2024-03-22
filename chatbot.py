from googlesearch import search as google_search
import webbrowser

def search(query, num_results=5):
    results = []
    count = 0
    for result in google_search(query, num=5, stop=num_results):
        results.append({'title': result, 'link': result})
        count += 1
        if count == num_results:
            break
    return results


def open_in_browser(link):
    webbrowser.open(link, new=-2)

def main():
    query = input("Enter your search query: ")
    num_results = int(input("Enter the number of search results to display: "))

    results = search(query, num_results)

    if not results:
        print("No results found.")
    else:
        for idx, result in enumerate(results, start=1):
            print(f"{idx}. {result['title']}")
            print(result['link'])
            print()

        open_result = input("Do you want to open any of the above results in a browser? (y/n): ")
        if open_result.lower() == 'y':
            try:
                choice = int(input("Enter the number of the result you want to open: "))
                if 1 <= choice <= len(results):
                    open_in_browser(results[choice - 1]['link'])
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    main()
