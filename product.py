from dbconnect import dbcon
from flask import jsonify


def saveProd(data):
    try:
        brand = data['brand']
        model = data['model']
        storage = data['storage']
        processor = data['processor']
        con = dbcon()
        cursor = con.cursor()
        sql = "insert into mobiles(Brand, Model, Storage, Processor) values(%s,%s,%s,%s)"
        cursor.execute(sql,(brand,model,storage,processor))
        con.commit()
        cursor.close()
        con.close()
        return {"status": "success", "message":"Product added successfully"}
    except Exception as e:
        return {"status": "error", "message": f"Error : {{str(e)}}"}


def getProdId():
    try:
        sql="select Id from mobiles"
        con = dbcon()
        cursor = con.cursor()
        cursor.execute(sql) # 
        res = cursor.fetchall()
        cursor.close()
        con.close()
        return [ row[0]  for row in res]
    except Exception as e:
        return "Invalid"


def getProduct(id):
    try:
        sql="select Brand, Model, Storage, Processor from mobiles where Id=%s"
        con = dbcon()
        cursor = con.cursor()
        cursor.execute(sql,(id))
        res= cursor.fetchone()
        cursor.close()
        con.close()
        if res:
            return jsonify({
                "Brand": res[0],
                "Model": res[1],
                "Storage":res[2],
                "Processor": res[3]                
            })
        else:
            return jsonify({"error":"Product not found"})   
    except Exception as e:
        return jsonify({"error":str(e)})     


def updateRate(data):
    id = data['id']
    rate = data['rate']
    try:
        sql="Update mobiles Set RoP=%s where Id=%s"
        con=dbcon()
        cursor = con.cursor()
        cursor.execute(sql,(rate, id))
        con.commit()
        print("Rate =  ",rate)
        cursor.close()
        con.close()
        return{"status":"success","message":"Rate  updated Successfuly"}
    except Exception as e:
        print("Error ",str(e))
        return {"status":"error","message": str(e)}
    

def delProduct(id):
    try:
        sql ="delete from mobiles where Id=%s"
        con= dbcon()
        cursor = con.cursor()
        cursor.execute(sql,(id))
        con.commit()
        cursor.close()
        con.close()
        return{"status":"success","message":"Recorded deleted"}
    except Exception as e:
        return{"status":"eroor","message":"Operation failed..."}

