def producte_schema(producte):
    return {
        "id": producte[0],
        "name": producte[1],
        "description": producte[2],
        "company": producte[3],
        "price": producte[4],
        "units": producte[5],
        "subcategory_id": producte[6],
        "created_at": producte[7],
        "updated_at": producte[8]
    }

def productes_schema(productes):
    return [producte_schema(producte) for producte in productes]