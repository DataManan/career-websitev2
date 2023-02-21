from sqlalchemy import create_engine, text
import os



db_connection_str = "mysql+pymysql://fql0xqnbuzi8q725vxip:pscale_pw_x0CpoZcErwypgkcrLJNhQz6JOiuWGfxUqz0BEs2k05E@ap-south.connect.psdb.cloud/careerswebsitev2?charset=utf8mb4"
# os.environ['DBCONNECTIONSTRING']
# my_secret = os.environ['DBCONNECTIONSTRING']
engine = create_engine(db_connection_str,
                      connect_args={
                        "ssl":{
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      }
                      )


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs
