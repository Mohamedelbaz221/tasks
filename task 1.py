# Step 01- Define Documents
docs = {
    "doc1": "new home sales top forecasts.",
    "doc2": "home sales rise in July",
    "doc3": "increase in home sales in July.",
    "doc4": "July new home sales rise"
}

# Step 02- Define the inverted index
inverted_index = {}

# Step 03- Build the inverted index
for doc_id, doc_content in docs.items():
    words = doc_content.split()
    for word in words:
        if word not in inverted_index:
            inverted_index[word] = set()
        inverted_index[word].add(doc_id)

# Step 04- Get the postings list for a given term
term = input("Enter a term: ")
if term in inverted_index:
    postings_list = inverted_index[term]
    print("Postings List:", ", ".join(str(doc_id) for doc_id in postings_list))
else:
    print("Term not found in documents.")