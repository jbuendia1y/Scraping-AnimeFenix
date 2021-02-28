import pymysql
import config

def executable_query(query,param=False):
    db = pymysql.connect(**config.config)
    db_cursor = db.cursor()

    if param :
        db_cursor.execute(query,param)
    else :
        db_cursor.execute(query)

    data = db_cursor.fetchall()

    db.commit()
    db_cursor.close()
    db.close()
    return data

def addAnime(data):
    query = "INSERT INTO animes(idAnime,title,poster,url) VALUES(idAnime,%s,%s,%s)"
    param = (data['title'],data['poster'],data['url'])
    res = executable_query(query,param)
