````markdown
# 🛒 Django + OpenSearch Product Search Backend

This project provides a lightweight, extensible backend for product search using **Django** and **OpenSearch**. It supports tag-based filtering, free-text search, and future-ready support for semantic vector search (e.g., via CLIP or custom embeddings).

---

## 🔧 Tech Stack

- **Django** (Models, Admin, API logic)
- **Django REST Framework** (Search endpoint)
- **OpenSearch** (Indexed search + filters)
- **Redis** _(optional)_ for caching
- **Celery** _(optional)_ for async indexing
- **Docker** _(recommended)_ for local dev

---

## 🚀 Features

- Index products with `name`, `description`, `tags`, and optional `tag_vector`
- Search by:
  - Free-text query (across name & description)
  - Filter by one or more tags
- Built-in support for AI-generated tags (via `ProductTag` model and `tag_vector`)
- Simple REST endpoint for search

---

## 📦 Installation

```bash
git clone https://github.com/your-user/django-opensearch-search.git
cd django-opensearch-search

# Setup virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start OpenSearch (use Docker or local setup)
docker-compose up -d opensearch

# Run Django
python manage.py migrate
python manage.py runserver
```
````

---

## 📁 Key Files

### `models.py`

Defines the `Product`, `Tag`, and `ProductTag` models with support for tag metadata and JSON vectors.

### `product_indexer.py`

Handles indexing of `Product` objects to OpenSearch, including tag names and tag vectors.

### `views.py`

Exposes a REST API endpoint (`GET /search`) to:

- Search by keyword
- Filter by tags
- Return matching product documents from OpenSearch

---

## 🔍 Example Search Request

```http
GET /search?tags=shoes&tags=green&q=summer
```

Returns all products matching the term `summer` in name/description AND tagged with both `shoes` and `green`.

---

## 🧠 Future Additions

- Cosine similarity vector search (CLIP integration)
- Faceted filtering (categories, brands, price ranges)
- Real-time updates via Celery tasks
- OpenAPI/Swagger auto-docs

---

## 🛠️ Index Setup Tips

- Use OpenSearch's `text` fields for full-text queries
- Use `keyword` fields for tag filters
- Define custom analyzers for fuzzy matching, synonyms, or edge n-grams if needed
- Store `tag_vector` as dense vectors to enable semantic search in the future

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome!
Feel free to fork and build on top of this to suit your own product catalog or tagging system.

---

## 📄 License

MIT — Use freely, launch fast, and remember to re-index responsibly 😉

```

Let me know if you’d like a `docker-compose.yml` or `.env` example included too!
```
