## StudyBot
알고리즘 문제풀이 레포지토리와 연동하여 노션 데이터베이스 값을 업데이트하는 백엔드 서비스

## 사용 기술
Flask, python3, notion API, 

## 사용법
[1.파이썬3 설치](https://www.python.org/downloads/)

2.가상환경 구성
```
python3 -m venv venv
```
3.가상환경 실행
- windows
```
venv\Scripts\activate
```
- linux
```
source venv\Scripts\activate
```
4.flask 설치
```
pip install flask
```
5.notion-client 설치
```
pip install notion-client
```
6.환경변수 세팅과 함께 서비스 실행
- windows
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
- linux
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
