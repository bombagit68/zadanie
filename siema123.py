from bs4 import BeautifulSoup

def extract_book_info(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    books = []

    title_elements = soup.find_all('h3', class_='book-title')
    price_elements = soup.find_all('div', class_='price')

    for title_elem, price_elem in zip(title_elements, price_elements):
        title = title_elem.text.strip()
        price = float(price_elem.text.strip().replace(' zł', '').replace(',', '.'))

        books.append({'title': title, 'price': price})

    for book in books:
        print(f"Tytuł: {book['title']}, Cena: {book['price']} zł")

if __name__ == "__main__":
    html_file = 'siema123.html'
    extract_book_info(html_file)
