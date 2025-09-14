# backend/app/db/init_db.py

import pymysql
from .session import engine
from .base import Base
from app.models import *
from app.core.config import settings


def create_database_if_not_exists():
    """데이터베이스가 없으면 생성"""
    try:
        # 데이터베이스 이름을 제외한 연결 정보로 연결
        connection = pymysql.connect(
            host=settings.DATABASE_HOST,
            user=settings.DATABASE_USER_NAME,
            password=settings.DATABASE_PASSWORD,
            port=int(settings.DATABASE_PORT),
            charset='utf8mb4'
        )
        
        with connection.cursor() as cursor:
            # 데이터베이스 생성
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.DATABASE_NAME}")
            print(f"Database '{settings.DATABASE_NAME}' created or already exists")
        
        connection.close()
    except Exception as e:
        print(f"Error creating database: {e}")
        raise


def init_db():
    # 먼저 데이터베이스 생성
    create_database_if_not_exists()
    
    # 그 다음 테이블 생성
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")


if __name__ == "__main__":
    init_db()
    