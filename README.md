# Django Request-Response Mastering

This Django project demonstrates **mastering request and response handling**, including plain text, numbers, booleans, JSON, redirects, headers, cookies, query strings, form data, and JSON body handling.

---

## 🚀 Features

### 1. Response Examples

| Type | Example |
|------|---------|
| Simple Plain Text | `HttpResponse('Plane Text Response')` |
| Number Response | `HttpResponse(str(10))` |
| Boolean Response | `HttpResponse(str(False))` |
| JSON Response | `JsonResponse({'Name': 'Raihan', 'age': '18'})` |
| Redirect Response | `HttpResponseRedirect('/')` |
| Not Found Response | `HttpResponseNotFound('Page Not Found')` |
| Custom Status Code | `HttpResponse('Status Code', status=202)` |
| Custom Header | `resp = HttpResponse('Plane Text'); resp['token']='784001'` |
| Response Cookies | `resp = HttpResponse('Plane Text Response with Cookie'); resp.set_cookie('Text_Cookie','784001adf')` |

> **Note:** Only one `return` statement is executed per view. Multiple `return` statements cannot all run in one view.

---

### 2. Request Examples

| Type | Example |
|------|---------|
| Request Methods | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` handled in `TypesOfRequest` |
| Query String | Access via `request.GET.get('param_name')` e.g., `QueryString` view |
| Custom Headers | Access via `request.headers.get('header_name')` e.g., `CustomHeader` view |
| Form Data | Access via `request.POST.dict()` e.g., `FormData` view |
| JSON Body | Access via `json.loads(request.body)` e.g., `RequestBody` view |

---

## 📝 Example Usage

### GET Request with Query String
```http
GET /QueryString/?name=Raihan&city=Dhaka
Response: Query String: Raihan, Dhaka
```

### POST Request with Form Data
```http
POST /FormData/
Content-Type: application/x-www-form-urlencoded
name=Raihan&city=Dhaka
Response: {"name":"Raihan","city":"Dhaka"}
```

### POST Request with JSON Body
```http
POST /RequestBody/
Content-Type: application/json
{
  "name": "Raihan",
  "age": 18,
  "city": "Dhaka"
}
Response:
{
  "name": "Raihan",
  "age": 18,
  "city": "Dhaka"
}
```

### Accessing Custom Header
```http
GET /CustomHeader/
Headers:
mytoken: 784001
password: mypass
Response: Query String: 784001, mypass
```

---

## ⚡ Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Django
pip install django

# Start Project & App
django-admin startproject request_response_mastering
cd request_response_mastering
python manage.py startapp myapp

# Add 'core' to INSTALLED_APPS in settings.py
# Create urls.py in core app and connect views
# Run migrations and start server
python manage.py migrate
python manage.py runserver
```

---

## 📝 Notes

- Use `@csrf_exempt` for POST requests during development/testing.  
- Only one response can be returned from a view.  
- Cookie names cannot have spaces; use letters, digits, underscores, or hyphens.  
- JSON responses are best handled with `JsonResponse`.  
- Query parameters and headers can be accessed via `request.GET` and `request.headers`.  
- Form data can be converted to dict with `request.POST.dict()`.  

---

**Author:** MD. Mostafa Raihan  
**Technology:** Django, Python  
**Purpose:** Learn and master Django Request-Response handling.  
