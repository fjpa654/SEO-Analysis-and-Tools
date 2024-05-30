import csv
import pandas as pd
import json

# Define the path to the output CSV file
output_csv_file_path = r'adjacency_matrix.csv'
json_file_path = r'crawled_links.json'
adjacency_matrix = pd.read_csv(output_csv_file_path, index_col=0)

# global visited vector
visited_vector = []

def get_all_links_from_page(url):
    # Find in the json file the links of the current page
    print("Finding links for page: " + url)
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        urls = []
        for item in data:
            if item['url'] == url:
                # Find the url in the json file and append all the links to the urls list
                urls = item['links']
                break
    return urls

# empty matrix with a vector as a parameter
def create_empty_matrix(vector):
    #the matrix should have only zeros
    #the matrix should have the same number of rows and columns as the vector all filled with zeros
    #the matrix should be a square matrix
    # Create a matrix filled with zeros
    matrix = [[0 for i in range(len(vector))] for j in range(len(vector))]
    return matrix

def generate_csv(matrix):
    # Convert the matrix to a DataFrame
    df = pd.DataFrame(matrix)
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv_file_path)

def update_matrix(i, links, matrix):
    for a_link in links:
        matrix[int(i)][int(a_link)] = 1
    return matrix

def main():
    #read the output.csv file and put the data in a dictoy format the following way:
    # key: url, value: id
    #make sure that we put the dictory in a global variable and remove the double brakets '[[]]' from the id before storing in the dictory
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        # vector_index = key : url, value : id starting from 0 enumarate the id
        index_vector = {item['url']: str(i) for i, item in enumerate(data)}
        the_matrix = create_empty_matrix(index_vector)

        #iterate over the index_vector
        for a in range(len(index_vector)):
            #pass the first url to the variable cur_url of the index_vector
            cur_url = list(index_vector.keys())[a]

            #pass the first value of the index_vector to the variable cur_key
            cur_key = list(index_vector.values())[a]

            # set cur_url_list to the list of links from the first url from the data
            cur_url_list = get_all_links_from_page(cur_url)

            #set cur_key_list to the list of links from the first key from the index_vector, if not found do not append
            cur_key_list = [index_vector.get(link) for link in cur_url_list]

            #update the adjacency matrix
            the_matrix = update_matrix(int(cur_key), cur_key_list, the_matrix)

        generate_csv(the_matrix)

if __name__ == '__main__':
    main()