'''
Virtual Environment

A virtual environment is a tool used used to isolate specific Python environment on a single
machine, allowing you to work on multiple projects with different dependencies and packages
and packages without conflicts. The can be especially useful when working on projects that
have conflicting package versions or packages that are not compatible with each other.

To create a virtual environment in Python, you can use the venv module that comes with
Python Here's an example of how to create virtual environment and activate it:

-------------------------------------------------------------------
# Create virtual environment
python -m venv myenv


# Activate the virtual environment (Linux/macOS)

sourse myenv/bin/activate

# Activate the virtual environment (Windows)

myenv\Scripts\activate

-------------------------------------------------------------------


Once the virtual environment is activated,, any packages that you install using pip will be
installed in the virtula environment, rather than in the global Pyton environment. This
allow you to have a separate set of packages for each project, without affectin the packages
installed in the environment.

To deactivate the virtual environment, you can use the deactivate command:

# Deactivate the virtual environment

deactivate
--------------------------

The "requirements.txt" file

In addition to creating and activating a virtual environment, it can be useful to create
a requirements.txt file that lists the packages and their versions that your project
depends on. This file can be used to easily install all the required packages in a new
environment.

To create a requirements.txt file, you can use the pip freeze command, which outputs a
list of installed packages and their versions.

For example:

#Install the packages listed i the requirements.txt file

pip install -r requirements.txt

--------------
Using a virtual environment and a requirements.txt file can help you mangae the
dependencies  for your Python projects and ensure taht your projects are protable
and can be easily  set yp on a new machine.































'''
