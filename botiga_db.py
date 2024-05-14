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
    print("carregant csv")
    
    # id_categoria,nom_categoria,id_subcategoria,nom_subcategoria,id_producto,nom_producto,descripcion_producto,companyia,precio,unidades
    # from a csv file, fill database
    try:
        conn = db_client()  
        cur = conn.cursor()
                    
        with file.file as f:  # Access the file object directly

            lines = f.readlines()[1:]
            print(lines)
            global antCategoryId
            global antSubcategoryId

            antCategoryId = -1
            antSubcategoryId = -1

            for line in lines:
                decoded_line = line.decode('utf-8')
                values = decoded_line.strip().split(',')
            
                if antCategoryId != values[0]:
                    print("a")
                    query = "INSERT INTO category (name) VALUES ('%s');"
                    exe_values = (values[1])
                    cur.execute(query, exe_values)
                    antCategoryId = values[0]
                                    
                if antSubcategoryId != values[2]:
                    print("b")
                    query = "INSERT INTO subcategory (name, category_id) VALUES ('%s', %s);"
                    exe_values = (values[3], values[0])
                    
                    cur.execute(query, exe_values)
                    antSubcategoryId = values[2]

                print("c")
                query = "INSERT INTO product (name, description, company, price, units, subcategory_id) VALUES (%s, %s, %s, %s, %s, %s);"
                exe_values = (values[5], values[6], values[7], values[8], values[9], values[2])
                cur.execute(query, exe_values)
                print("d")

            conn.commit()
        return {
            "message": "Producte afegit correctament"
        }

    except Exception as e: 
        return {"status": -1, "message": f"Error de connexió:{e}"}
    
    finally:
        conn.close()
