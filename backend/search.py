def search_products(query, products):
    # PERFORMANCE BUG: O(n²) complexity
    results = []
    for product in products:
        for word in query.split():
            if word in product['name']:
                if product not in results:
                    results.append(product)
    return results

def find_similar_products(product_id, all_products):
    # PERFORMANCE BUG: Inefficient algorithm
    similar = []
    target = None
    for p in all_products:
        if p['id'] == product_id:
            target = p
            break
    
    for p in all_products:
        if p['category'] == target['category']:
            similar.append(p)
    return similar