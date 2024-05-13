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
