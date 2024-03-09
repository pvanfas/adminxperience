Configuring the AdminXperience
======================================

AdminXperience provides various configuration options to customize its behavior according to your project's requirements. These options are typically set in your Django project's settings file (``settings.py``). Below are some common configuration options:

1. ADMINXPERIENCE_THEME: This option allows you to specify the theme used for the AdminXperience interface. You can choose from predefined themes such as light or dark, or specify custom theme colors.

   Example:

   ::

      ADMINXPERIENCE_THEME = 'dark'

2. ADMINXPERIENCE_LOGO: You can customize the logo displayed in the AdminXperience interface by specifying the path to the image file.

   Example:

   ::

      ADMINXPERIENCE_LOGO = 'path/to/logo.png'

3. ADMINXPERIENCE_MENU: Customize the navigation menu items displayed in the AdminXperience interface by specifying a list of menu items.

   Example:

   ::

      ADMINXPERIENCE_MENU = [
          {'label': 'Dashboard', 'url': '/admin/dashboard/'},
          {'label': 'Users', 'url': '/admin/users/'},
          {'label': 'Settings', 'url': '/admin/settings/'},
      ]

4. ADMINXPERIENCE_EXTENSIONS: Enable or disable specific AdminXperience extensions by specifying a list of extension names.

   Example:

   ::

      ADMINXPERIENCE_EXTENSIONS = ['breadcrumbs', 'quick_actions']

These are just a few examples of the configuration options available in AdminXperience. Refer to the documentation for a comprehensive list of available options and their usage.
