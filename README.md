### Django Final Project

[**PythonAnywhere連結**](http://station4178.pythonanywhere.com/)

#### 系統架構
![image](https://github.com/Station9586/Django_Final/blob/main/System_structure.png)

#### 網頁部分
主要以**template模板**的形式來完成

#### 主要功能
1. **排版**：手刻 CSS 檔案
2. **資料庫**：django內建，資料表跟php用的完全一樣
   資料表內容：![image](https://github.com/Station9586/Django_Final/blob/main/DB_plot.png)
3. **登入介面**
    - LoginForm 用 forms.Form
    - Authentication Login導入到後台資料庫
    - Register 用一般註冊
4. **messages**
    - 內建的messages套件，搭配CSS去做樣式變化

**Session存登入資訊才能瀏覽以下功能**

5. **首頁**
    - static 載入image
    - iframe放youtube影片
6. **所有預約資訊**
    - 資料庫叫資料用for迴圈印出來，empty印出沒有預約資料
    - 刪除按鈕用URL反解傳到刪除頁面
    - 篩選功能用Javascript寫的
7. **新增預約**
    - 預約表格用forms.ModelForm實作
8. **修改預約**
    - 一般table去做修改
9. **密碼修改 / 刪除帳號**
    - 一般table去修改
    - 刪除是判斷密碼有沒有對才能進行刪除
10. **登出**
    - 回傳到登入頁面且清空Session


> 期末專題下次一定認真做...
