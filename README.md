# Nogizaka API

## 概要

乃木坂46のメンバーデータ、楽曲データ、メンバー・楽曲間のリレーションを返すAPI。REST APIになっている。

## 技術的特徴

- Djangoアプリケーション
- REST API (Django REST flamework)
    - 一覧表示
    - 詳細表示
    - 新規投稿
    - 修正
    - 削除
- pipenv

## 使い方

1. このリポジトリをクローン

1. 依存関係のインストール


    ```
    pipenv install
    ```

1. マイグレーションファイル作成

    ```
    python manage.py makemigrations
    ```

1. マイグレーション実行

    ```
    python manage.py migrate
    ```

1. 管理者作成

    ```
    python manage.py createsuperuser
    ```

1. アプリケーション実行

    ```
    python manage.py runserver
    ```

## 最後に

このプロジェクトに何か問題を見つけた方はぜひissueをお待ちしております。