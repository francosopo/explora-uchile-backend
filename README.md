# Explora UChile Backend

## Defina las variables de entorno:

EXPLORA_UCHILE_DB_PASSWORD
EXPLORA_UCHILE_DJANGO_SECRET_KEY

# Base de datos

Defina una base de datos en el settings.py

```js
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME":"explora_uchile_db",
        "USER": "explora_uchile_user",
        "PASSWORD": os.environ["EXPLORA_UCHILE_DB_PASSWORD"],
        "HOST": "localhost",
        "PORT":5432
    }
}
```
