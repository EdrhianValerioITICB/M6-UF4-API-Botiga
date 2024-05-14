from client import db_client
import datetime


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
        query = "select * from product where product_id = %s"
        value = (id, )
        cur.execute(query, value)
        product = cur.fetchone()

        return product

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}
    
    finally:
        conn.close()

def afegir_producte(name, description, company, price, units, subcategory_id):
    try:
        conn = db_client()  
        cur = conn.cursor()

        query = "INSERT INTO product (name, description, company, price, units, subcategory_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, description, company, price, units, subcategory_id)
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
        return result

    except Exception as e:
        return  {"status": -1, "message": f"Error de conexion: {e}"}
    
    finally:
        conn.close()


def delete_product(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM product WHERE product_id = %s;"
        cur.execute(query, (id,))

        conn.commit()
        return {
            "message": "Producte borrat correctament"
        }
    except Exception as e:
        return {"status": -1, "message": f"Error de conexió{e}"}
    finally:
        conn.close()

def update_producte(id, price, units):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "UPDATE product SET price = %s, units = %s WHERE product_id = %s;"
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


def carregar_csv(file):
    try:
        conn = db_client()  
        cur = conn.cursor()
                    
        with file.file as f:
            lines = f.readlines()[1:]

            for line in lines:
                decoded_line = line.decode('utf-8')
                values = decoded_line.strip().split(',')

                # Comprobar si la categoría existe
                cur.execute("SELECT * FROM category WHERE category_id = %s", (values[0],))
                category_exists = cur.fetchone()

                # Insertar o actualizar la categoría
                if category_exists:
                    cur.execute("UPDATE category SET name = %s WHERE category_id = %s", (values[1], values[0]))
                else:
                    cur.execute("INSERT INTO category (name) VALUES ('%s')", (values[1]))

                # Comprobar si la subcategoría existe
                cur.execute("SELECT * FROM subcategory WHERE subcategory_id = %s", (values[2],))
                subcategory_exists = cur.fetchone()

                # Insertar o actualizar la subcategoría
                if subcategory_exists:
                    cur.execute("UPDATE subcategory SET name = %s WHERE subcategory_id = %s", (values[3], values[2]))
                else:
                    cur.execute("INSERT INTO subcategory (name, category_id) VALUES (%s, %s)", (values[3], values[0]))

                # Comprobar si el producto existe
                cur.execute("SELECT * FROM product WHERE product_id = %s", (values[4],))
                product_exists = cur.fetchone()

                # Insertar o actualizar el producto
                if product_exists:
                    cur.execute("UPDATE product SET name = %s, description = %s, company = %s, price = %s, units = %s WHERE product_id = %s", (values[5], values[6], values[7], values[8], values[9], values[4]))
                else:
                    cur.execute("INSERT INTO product (name, description, company, price, units, subcategory_id) VALUES (%s, %s, %s, %s, %s, %s)", (values[5], values[6], values[7], values[8], values[9], values[2]))

            conn.commit()
            return {"message": "Càrrega massiva de productes realitzada correctament"}

    except Exception as e: 
        return {"status": -1, "message": f"Error de connexió: {e}"}
    
    finally:
        conn.close()
