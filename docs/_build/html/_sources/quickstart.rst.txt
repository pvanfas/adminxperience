Quick start guide
======================================

AdminXperience is a Django admin redesign package aimed at enhancing the default Django admin interface with modern design elements and improved user experience. It provides developers and administrators with a sleek and intuitive interface for managing Django models and data efficiently.

Key Features
----------------

- Modern and elegant redesign of the Django admin interface.
- Improved usability and productivity for managing Django projects.
- Customizable design elements to match your project's branding and requirements.
- Compatible with Django versions 3.0 and above.


Installation
----------------

This quickstart guide will help you get started with AdminXperience in your Django project.

1. Installation: Install AdminXperience using pip:

   ::

      pip install adminxperience

2. Integration: Add 'adminxperience' to the ``INSTALLED_APPS`` list in your Django project's ``settings.py`` file:

   ::

      INSTALLED_APPS = [
          ...
          'adminxperience',
          ...
      ]

3. Migrations: Run migrations to apply any necessary changes to your database models:

   ::

      python manage.py makemigrations
      python manage.py migrate

4. Start Server: Start your Django development server:

   ::

      python manage.py runserver

5. Access Admin Interface: Access the Django admin interface in your web browser, and you'll see the redesigned interface provided by AdminXperience.

For more detailed usage instructions and customization options, please refer to the documentation.
