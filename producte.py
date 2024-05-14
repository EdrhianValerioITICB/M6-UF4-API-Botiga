# Esquema de un solo producto
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

# Esquema de todos los productos
def productes_schema(productes):
    return [producte_schema(producte) for producte in productes]

# Esquema de todos los productos, pero el que se utiliza en el endpoint de readAll
def readAll_schema(result):
    return [{
        "categoria": row[0],
        "subcategoria": row[1],
        "producto": row[2],
        "marca": row[3],
        "precio": row[4]
    } for row in result]