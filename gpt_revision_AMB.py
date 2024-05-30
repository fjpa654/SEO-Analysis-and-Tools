import csv
import pandas as pd
import json

# Define the path to the output CSV file
output_csv_file_path = r'adjacency_matrix.csv'
json_file_path = r'crawled_links.json'

# Function to get all links from a page
def get_all_links_from_page(url, data):
    print(f"Finding links for page: {url}")
    for item in data:
        if item['url'] == url:
            return item['links']
    return []

# Function to create an empty adjacency matrix
def create_empty_matrix(vector):
    size = len(vector)
    return [[0 for _ in range(size)] for _ in range(size)]

# Function to generate CSV from the adjacency matrix
def generate_csv(matrix):
    df = pd.DataFrame(matrix)
    df.to_csv(output_csv_file_path, index=False)

# Function to update the adjacency matrix
def update_matrix(i, links, matrix, index_vector):
    for link in links:
        if link in index_vector:
            j = int(index_vector[link])
            matrix[i][j] = 1
    return matrix

# Main function
def main():
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        # Create index vector: key is URL, value is its index
        index_vector = {item['url']: str(i) for i, item in enumerate(data)}
        the_matrix = create_empty_matrix(index_vector)

        # Iterate over each URL in the index_vector
        for url, index in index_vector.items():
            cur_url_list = get_all_links_from_page(url, data)
            the_matrix = update_matrix(int(index), cur_url_list, the_matrix, index_vector)

        generate_csv(the_matrix)
        #put the index_vector on a text file as a single colum where the with this format id, url
        with open('index_vector.txt', 'w') as file:
            for url, index in index_vector.items():
                file.write(f"{index}, {url}\n")

if __name__ == '__main__':
    main()
