### 环境搭建并创建实例
   - 1.安装django(linux)  
     直接使用:pip install django  
     安装有ananconda可用:conda install django  
     查看下版本:python -c "import django; print(django.get_version())"   
   - 2.创建一个应用  
    基本上的管理都是使用django-admin命令  
    ```
    django-admin startproject mysite  
    ```  
    会创建一个为mysite的项目(目录)，tree看一下  
    ```
    mysite/
      manage.py
      mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    ```  
      * manage.py 是一个命令行实用脚本，可以通过不同的方式与 Django 项目交互
      * 内部的 mysite/ 目录是项目的 Python 包。导入这里面的内容时要使用目录的名称（如mysite.urls）。
      * mysite/init.py 是一个空文件，目的是让 Python 把这个目录识别为 Python 包。
      * mysite/settings.py 是 Django 项目的设置/配置。
      * mysite/urls.py 是 Django 项目的 URL 声明，即 Django 驱动的网站的“目录”。
      * mysite/wsgi.py 是兼容 WSGI 的 Web 服务器的入口点，用于伺服项目。  

   - 3.设置并运行
    基本上的设置都在setting.py中进行修改  
    修改前最好先备份   
    ALLOWED_HOSTS = ['*'] #允许任何ip进行访问  
    LANGUAGE_CODE = 'zh-hans' #默认语言是'en-us'，奇怪的是中文为什么是zh-hans  
    TIME_ZONE = 'Asia/Shanghai' #修改下时区  
    INSTALLED_APPS可以看到默认的一些应用  
    <br />
    在运行之前需要将这些应用进行迁移:python manage.py migrate  
    <br />
    运行一下:  
    python manage.py runserver  
    python manage.py runserver 8080  #也可以指定端口  
    python manage.py runserver 0.0.0.0:8000  #也可以监听公有ip  

   - 4.模型-视图-控制器(MVC)设计模式  
    * 模型（M）是数据的表述。它不是真正的数据，而是数据的接口。使用模型从数据库中获取数据时，  
      无需知道底层数据库错综复杂的知识。模型通常还会为数据库提供一层抽象，这样同一个模型就能使  
      用不同的数据库。
    * 视图（V）是你看到的界面。它是模型的表现层。在电脑中，视图是你在浏览器中看到的 Web 应用的  
      页面，或者是桌面应用的 UI。视图还提供了收集用户输入的接口。
    * 控制器（C）控制模型和视图之间的信息流动。它通过程序逻辑判断通过模型从数据库中获取什么信  
      息，以及把什么信息传给视图。它还通过视图从用户那里收集信息，并且实现业务逻辑：变更视图，  
      或者通过模型修改数据，或者二者兼具。  
    Django 严格遵守 MVC 模式，但是有自己的实现逻辑。“C”部分由框架处理，多数时候，我们的工作在模  
    型、模板和视图中，因此 Django 经常被称为 MTV 框架。在 MTV 开发模式中：  
      * M 表示“模型”，即数据访问层。这一层包含所有与数据相关的功能：访问数据的方式、验证数据的方  
        式、数据的行为、数据之间的关系。
      * T 表示“模板”，即表现层。这一层包含表现相关的决策：在网页或其他文档类型中如何显示某个东西。
      * V 表示“视图”，即业务逻辑层。这一层包含访问模型和选择合适模板的逻辑。你可以把视图看做模型  
        和模板之间的桥梁。
