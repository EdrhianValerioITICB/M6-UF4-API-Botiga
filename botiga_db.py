from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from product")

        products = cur.fetchall()

        return products
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}
    
    finally:
        conn.close()

def read_one(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = cur.execute("select * from PRODUCT WHERE id = %s")
        value = (id, )
        cur.execute(query, value)
        product = cur.fetchone()

        return product

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}
    
    finally:
        conn.close()

def afegir_producte(name, description, company, price, units, subcategory, created_at, updated_at):
    try:
        conn = db_client()  
        cur = conn.cursor()
        query = "INSERT INTO PRODUCT (name, description, company, price, units, subcategory, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, description, company, price, units, subcategory, created_at, updated_at)
        cur.execute(query, values)
        conn.commit()
        return {
            "message": "Producte afegit correctament"
        }

    except Exception as e: 
        return {"status": -1, "message": f"Error de connexió:{e}"}
    
    finally:
        conn.close()


def readAll():
    try:
        conn = db_client()
        cursor = conn.cursor()
        cursor.execute("SELECT c.name AS categoria, s.name AS subcategoria, p.name AS producto, p.company AS marca, p.price AS precio FROM product p INNER JOIN subcategory s ON p.subcategory_id = s.subcategory_id INNER JOIN category c ON s.category_id = c.category_id; ")

        result = cursor.fetchall()

    except Exception as e:
        return  {"status": -1, "message": f"Error de conexion: {e}"}
    
    finally:
        conn.close()

    return result

def delete_product(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM product WHERE id = %s;"
        cur.execute(query, (id,))

        conn.commit()
        
    except Exception as e:
        return {"status": -1, "message": f"Error de conexió{e}"}
    finally:
        conn.close()

def update_producte(id, price, units):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "UPDATE product SET price = %s, units = %s WHERE id = %s"
        values = (price, units, id)
        cur.execute(query, values)

        conn.commit()
        return {
            "message": "Producte modificat correctament"
        }
    except Exception as e:
        return {"status": -1, "message": f"Error de conexió{e}"}
    finally:
        conn.close()
