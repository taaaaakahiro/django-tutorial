# django-tutorial  
## その１  
 手順  
  - プロジェクト作成  
  django-admin startproject mysite  
  - アプリケーションを作成  
  python manage.py startapp polls  
  - ビューの作成(アプリ)  
  polls/views.py  
  polls/urls.py  
  mysite/urls.py  

## その２  
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

## その３ 
 手順  
  - オーバービュー(views.index)を使う場合  
  polls/view.py  
  - 404エラー検出(views.detail)  
  - テンプレートシステムを使う  
  - テンプレート内のハードコードされたurlを削除  
  polls/templates/polls/index.html  
  - urlの名前空間  
  polls/urls.py app_name = 'polls'  

## その４  
 - フォームの作成  


## その５  

## その６  

## その７  