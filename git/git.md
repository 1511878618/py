#  Git 教程

从本地git库到github同步

####  初始化git仓库

在一个文件夹内调用gitbash终端

使用`git init` 初始化Git 仓库

#### 对本地仓库进行初步管理

1. `git add filename`  添加文件到仓库
2. `git commit -m `本次上传的描述'

以上步骤完成基本完成对文件的上传

之后，若有修改则需要使用来同步

此外查看两次版本的差异使用`git status`

#### 远程仓管理

##### SSH添加

需要在github上添加自己电脑的ssh

##### 添加远程仓

`git remote add python [sshUrl`] 添加远方的仓库（sshUrl是远程仓库的地址，里面应当没有内容），python 是自定义的命名不一定要与远方的仓库同名



`git push python master`是上传命令

`git push -u python master`是上传所有

那么如果在一次更改后，怎么更新呢

使用以下代码即可

git 

