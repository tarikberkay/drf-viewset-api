
# DRF VIEWSET API

Django Rest Framework ViewSet yapısı ile Blog API projesi.



## Kurulum

Not: Sol taraftaki veriler Mac kurulumu için sağ taraftaki veriler Windows kurulumu içindir.

Projeyi Kurma  

```bash
  git clone https://github.com/tarikberkay/drf-viewset-api.git
```

Sanal Ortam Oluşturma
```bash
  python3 -m venv venv || python -m venv venv
```

Sanal Ortamı Aktif Etme
```bash
  source venv/bin/activate  ||  venv\Scripts\activate
```

Gerekli Paketleri Kurma
```bash
  pip3 install -r requirements.txt  ||  pip install -r requirements.txt
```


Projeyi Çalıştırma
```bash
  python3 manage.py runserver || python manage.py runserver
```

  
## API Kullanımı

#### Öğeyi getir

```http
  http://127.0.0.1:8000/auth/login/
```

Login'i getirir.


#### Öğeyi getir

```http
  http://127.0.0.1:8000/auth/logout/
```

Logout'u getirir.


#### Öğeyi getir

```http
  http://127.0.0.1:8000/auth/logoutall/
```

Logoutall'u getirir.


#### Öğeyi getir

```http
  http://127.0.0.1:8000/auth/register/
```

Register'ı getirir.



#### Tüm öğeleri getir

```http
  http://127.0.0.1:8000/api/posts
```
Tüm Postları getirir.



#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/authors/
```

Tüm yazarları getirir.




#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/tags/
```

Tüm Tag'leri getirir.




#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/swagger/
```

Swagger ile API belgelenmesi kısmıdır.






  
