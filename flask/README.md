.
├── README.md  
├── __pycache__  
├── app.py                                                      //主要完成应用的配置、初始化、蓝图注册、请求装饰器定义、应用的启动和监听  
├── blueprints                                                  //蓝图                                                
│   ├── __init__.py     
│   ├── __pycache__                                                
│   ├── forms.py                                                //验证表单数据是否符合预期格式  
│   ├── qa.py                                                   //问答模块蓝图  
│   └── user.py                                                 //用户模块蓝图   
├── config.py                                                   //配置文件参数信息  
├── decorators.py                                               //验证是否登录的装饰器  
├── exts.py                                                     //公共类（避免循环调用）  
├── migrations                                                  //ORM模型映射数据库时生成的文件  
│   ├── README  
│   ├── __pycache__  
│   ├── alembic.ini  
│   ├── env.py  
│   ├── script.py.mako  
│   └── versions  
├── models.py                                                   //ORM数据库模型  
├── requirements.txt                                            //需要安装的第三方库  
├── static                                                      //js以及css静态文件  
│   ├── bootstrap                                               //bootstrap的css文件  
│   │   └── bootstrap@4.6.min.css                               //总体的css文件  
│   ├── css                                                     //自定义css样式文件  
│   │   ├── detail.css                                          //问答详情页面css样式文件  
│   │   ├── index.css                                           //问答首页页面css样式文件    
│   │   └── init.css                                            //css初始化样式文件  
│   ├── images                                                  //图片存放文件夹  
│   │   └── 1.jpg                                               //用户头像图片文件  
│   ├── jquery                                                  //jquery的js文件    
│   │   └── jquery.3.6.min.js                                   //总体的js文件  
│   └── js                                                      //自定义js文件  
│       └── register.js                                         //通过js发送网络请求：ajax（注册时邮箱发送验证码）  
└── templates                                                   //html页面文件   
    ├── base.html                                               //父页面，所有页面都包括的内容    
    ├── detail.html                                             //继承base.html的问答详情页面  
    ├── index.html                                              //继承base.html的问答首页页面  
    ├── login.html                                              //继承base.html的登录页面  
    ├── public_question.html                                    //继承base.html的发布问题页面  
    └── register.html                                           //继承base.html的注册页面  

14 directories, 43 files

## 环境配置  

# pip install  
需要安装的第三方库信息存放在`requirements.txt`文件中  

# html文件  
html文件源码来自bootstrap，链接： https://v4.bootcss.com/  
html代码内容可根据需求自行更改  

# css文件  
css文件源码来自bootstrap，链接： https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css  

# js文件  
js文件源码来自jquery，链接： https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.min.js  


环境配置好之后，需要配置数据库环境，更改config.py中相应数据参数信息，然后通过Flask-Migrate插件将ORM模型映射到数据库中，具体参考`note.md`文件  
注：如无法启动项目请查看本地环境配置或在app.py中app.run()处指定IP和端口等信息如：  
app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )  
此项目目前可扩展的地方还有很多，如用户注册时可上传头像等（目前用户头像均为static/images/1.jpg文件）  
