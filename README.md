# Blog Website

A full-featured Django-based blog platform with user authentication, content management, category organization, and an admin dashboard for managing posts, categories, and users.

## Features

✅ **User Authentication**
- User registration and login
- Secure password hashing
- Session management

✅ **Blog Management**
- Create, read, update, and delete blog posts
- Post categorization
- Post status management (Draft, Published, etc.)
- Author tracking

✅ **Comments System**
- Users can comment on blog posts
- Comment display with author information

✅ **Category Management**
- Organize posts by categories
- Easy category filtering

✅ **Admin Dashboard**
- Manage blog posts (create, edit, delete)
- Manage categories
- Manage user accounts
- User-friendly interface for content creators

✅ **Search Functionality**
- Search posts by title and content
- Filter posts by category

✅ **Media Management**
- Upload images for blog posts
- Image processing with Pillow

✅ **Responsive Design**
- Bootstrap-based UI
- Mobile-friendly templates

## Tech Stack

- **Backend:** Django 5.2.7
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **Image Processing:** Pillow
- **Form Styling:** Django Crispy Forms, Crispy Bootstrap4
- **Python Version:** 3.x

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd "Blog website"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   - On Windows (PowerShell):
     ```bash
     .\env\Scripts\Activate.ps1
     ```
   - On Windows (CMD):
     ```bash
     .\env\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: `http://localhost:8000/`
   - Admin panel: `http://localhost:8000/admin/`

## Project Structure

```
Blog website/
├── blog_main/              # Main project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   ├── views.py            # Main views
│   ├── forms.py            # Main forms
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
│
├── blogs/                  # Blog app
│   ├── models.py           # Blog, Category, Comment models
│   ├── views.py            # Blog views
│   ├── urls.py             # Blog URL patterns
│   ├── forms.py            # Blog forms
│   ├── admin.py            # Admin customization
│   ├── context_processors.py  # Context processors
│   └── migrations/         # Database migrations
│
├── dashboard/              # Admin dashboard app
│   ├── models.py           # Dashboard models
│   ├── views.py            # Dashboard views
│   ├── urls.py             # Dashboard URL patterns
│   ├── forms.py            # Dashboard forms
│   └── migrations/         # Database migrations
│
├── templates/              # HTML templates
│   ├── base/               # Base templates
│   ├── dashboard/          # Dashboard templates
│   ├── home.html           # Home page
│   ├── blogs.html          # Blog list page
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   └── search.html         # Search results page
│
├── static/                 # Static files (CSS, images)
│   ├── css/
│   └── images/
│
├── media/                  # User-uploaded files
│   └── uploads/
│
├── env/                    # Virtual environment
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── requirement.txt         # Project dependencies
└── README.md               # This file
```

## Database Models

### Blog Model
- Title
- Content
- Author (ForeignKey to User)
- Category (ForeignKey to Category)
- Created date
- Updated date
- Status (Draft/Published)
- Featured image

### Category Model
- Name
- Description
- Created date

### Comment Model
- Content
- Author (ForeignKey to User)
- Post (ForeignKey to Blog)
- Created date

### User Model
- Uses Django's built-in User model
- Email
- Username
- Password (hashed)

## Usage

### Creating a Blog Post
1. Log in to your account
2. Navigate to Dashboard → Add Posts
3. Fill in the post details (title, content, category, image)
4. Click "Publish"

### Managing Categories
1. Go to Dashboard → Categories
2. Add new categories or edit existing ones
3. Categories can be assigned to posts during creation

### Searching Posts
1. Use the search bar on the public blog page
2. Search by post title or content keywords
3. Filter results by category if needed

### Admin Panel
1. Access `/admin/` with superuser credentials
2. Manage databases, users, and site-wide settings

## Running the Project

### Development Server
```bash
python manage.py runserver
```

### Create Migrations (if you modify models)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create New Superuser
```bash
python manage.py createsuperuser
```

## Future Improvements

- [ ] Add comprehensive unit and integration tests
- [ ] Implement API endpoints (Django REST Framework)
- [ ] Add pagination for better performance
- [ ] Implement caching (Redis)
- [ ] Add user roles and permissions system
- [ ] Email notifications for comments
- [ ] Advanced search with filters
- [ ] User profiles
- [ ] Post likes/reactions
- [ ] Scheduled post publishing

## Security Notes

- Always set `DEBUG = False` in production
- Use environment variables for `SECRET_KEY`
- Enable HTTPS
- Set `ALLOWED_HOSTS` appropriately
- Use a production database (PostgreSQL) instead of SQLite
- Implement CSRF protection (enabled by default)
- Validate all user inputs

## Troubleshooting

**Port 8000 is already in use:**
```bash
python manage.py runserver 8080
```

**Database errors after model changes:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Static files not loading:**
```bash
python manage.py collectstatic
```

## Contributing

Feel free to fork this project and submit pull requests for improvements.

## License

This project is open-source and available under the MIT License.

## Support

For issues or questions, feel free to reach out or open an issue in the repository.

---

**Happy Blogging! 🚀**