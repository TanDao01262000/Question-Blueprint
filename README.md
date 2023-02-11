# For dev team
 *Please make sure to create your own branch to work on the project.*


# SJSU-CMPE-133-Group-1

Members: 
  - Hunter Adams
  - Tan Dao
  - Yohannes Habtemariam
  - Sahiti Hibane
  - Vivekanand Koya

Topic: Question and Answer (Q&A) web based application

# Tools
1. Virtual environment:
  1. Why virtual environment is needed?
      In simple words, developing a project in a sperated enviroment is helping developers control over libraries or depedencies more efficiently.
      For example, let say, you are working on a project A and it requires you to install Boostrap5. At the same time, another project askes you to use Boostrap4.
      If you install all the libraries in the global environment, it will be time consuming to manage and reinstall them.
      Therefore, each project should have a seperated virtual environment.
  2. How to set up and virtual environment?
      1. Install virtualenv by running the following command:
      ``pip install virtualenv``
      2. Create a virtual environment by running the following command:
      ``virtualenv <env_name>`` (replace <env_name> with the name you'd like to give to your virtual environment)
      3. Activate the virtual environment by running the following command:
        For Windows: ``<env_name>\Scripts\activate`` 
        For Unix or Linux: ``source <env_name>/bin/activate``
        
2. Django
  1. Why Django?
  2. 
# Clone project
  1. Clone repo to local machine: 
         ``git clone git@github.com:TanDao01262000/Question-Blueprint.git``
  2. Create a virtual environment and activate it
  3. Install list of requirements: 
        ``pip install -r requirement.txt``
  4. Navigate to the project directory:
        ``cd QB``
  4. Run project: 
        `` python manage.py runserver``
  
          

