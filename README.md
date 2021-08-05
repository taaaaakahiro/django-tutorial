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
 polls/urls.py  
 polls/views.py  

## その５  
 - 自動テストの導入  
 python manage.py shell 未来の日付の質問のメソッドをチェックするには、 shell を使用してバグを確認  
 python manage.py test polls  
 - 解説  
 manage.py test polls は、polls アプリケーション内にあるテストを探します  
 django.test.TestCase クラスのサブクラスを発見します  
 テストのための特別なデータベースを作成します  
 テスト用のメソッドとして、test で始まるメソッドを探します  
 test_was_published_recently_with_future_question の中で、pub_date フィールドに今日から30日後の日付を持つ Question インスタンスが作成されます  
 そして最後に、 assertIs() メソッドを使うことで、本当に返してほしいのは False だったにもかかわらず、 was_published_recently() が True を返していることを発見します  
 - テスト作成  
 polls/test.py  
 - ビューをテスト  
python manage.py shell  

## その６  
 - アプリの構造をカスタマイズ  
 - 背景画像を追加  

## その７  
 - adminフォームのカスタマイズ  
 - リレーションを貼ったオブジェクトを張ったオブジェクトの追加  
 - 管理サイトのチェンジリストページをカスタマイズする  
 - 管理サイトのルック＆フィールをカスタマイズする  
