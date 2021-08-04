# django-tutorial  
## その1  
 手順  
  - プロジェクト作成  
  django-admin startproject mysite  
  - アプリケーションを作成  
  python manage.py startapp polls  
  - ビューの作成(アプリ)  
  polls/views.py  
  polls/urls.py  
  mysite/urls.py  
## その2  
 手順  
  - Databaseの設定  
  ENGINE:'django.db.backends.postgresql' ※postgreSQL/dockerを使用   
  - データベースにテーブルを作る  
  docker-compose exec web python manage.py migrate  
  - モデルの作成にする  
  polls/models.py  
  - モデルを有効にする  
  mysite/settings.py  
  docker-compose exec web python manage.py makemigrations polls  
  - マイグレーションが実行するSQLを確認する  
  docker-compose exec web python manage.py sqlmigrate polls 0001  
  - モデル作成後  
  python manage.py migrate  
  - 管理ユーザーを作成  
  python manage.py createsuperuser  
  - pollsアプリをadmin上で編集できるようにする  
  polls/admin.py  
## その3  

## その4  

## その5  

## その6  

## その7  