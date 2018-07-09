
# 读取xlsx文件


```python
import pandas as pd
```


```python
data=pd.read_excel("404.xlsx",0)
data.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>ip</th>
      <th>day</th>
      <th>time</th>
      <th>domain</th>
      <th>method</th>
      <th>uri</th>
      <th>http</th>
      <th>status</th>
      <th>datasize</th>
      <th>referer</th>
      <th>useragent</th>
      <th>cdnip</th>
      <th>md5str</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16658712</td>
      <td>123.125.71.34</td>
      <td>01/Jun/2018</td>
      <td>01:50:11</td>
      <td>m.3618med.com</td>
      <td>GET</td>
      <td>/seo/shqy/</td>
      <td>HTTP/1.1</td>
      <td>404</td>
      <td>3517</td>
      <td>-</td>
      <td>Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) App...</td>
      <td>-</td>
      <td>37ccfb8930d7fcd38e149be0eeb17ff9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>16659100</td>
      <td>123.125.71.87</td>
      <td>01/Jun/2018</td>
      <td>02:15:30</td>
      <td>yingte.m.3618med.com</td>
      <td>GET</td>
      <td>/sub/company-news/tel:18155223051</td>
      <td>HTTP/1.1</td>
      <td>404</td>
      <td>3517</td>
      <td>-</td>
      <td>Mozilla/5.0 (compatible; Baiduspider/2.0; +htt...</td>
      <td>-</td>
      <td>093b0ebacbdfc36b43a909ce5c7335aa</td>
    </tr>
  </tbody>
</table>
</div>



# 读取mysql


```python
import pymysql
```


```python
cn=pymysql.connect(host="localhost",user="root",password="root",database="3618med",charset="utf8")
```


```python
data=pd.read_sql("select * from logtable_1_to_6 limit 10",con=cn)
```


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>ip</th>
      <th>day</th>
      <th>time</th>
      <th>domain</th>
      <th>method</th>
      <th>uri</th>
      <th>http</th>
      <th>status</th>
      <th>datasize</th>
      <th>referer</th>
      <th>useragent</th>
      <th>cdnip</th>
      <th>md5str</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>13111475</td>
      <td>119.167.248.2</td>
      <td>21/Apr/2018</td>
      <td>22:53:01</td>
      <td></td>
      <td>GET</td>
      <td>/product/zhaoshang-1303663.html</td>
      <td>HTTP/1.1</td>
      <td>200</td>
      <td>26468</td>
      <td>-</td>
      <td>web spider/4.0(+http://www.sogou.com/docs/help...</td>
      <td>123.126.113.132</td>
      <td>0ea45416769215f26da0c2c606cb19eb</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13111476</td>
      <td>220.181.125.67</td>
      <td>21/Apr/2018</td>
      <td>22:53:02</td>
      <td></td>
      <td>GET</td>
      <td>/bid/zhaobiao-1385157.html</td>
      <td>HTTP/1.1</td>
      <td>200</td>
      <td>17931</td>
      <td>-</td>
      <td>web spider/4.0(+http://www.sogou.com/docs/help...</td>
      <td>-</td>
      <td>c37b94c7032ac794c951df7c9f7019c7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13111474</td>
      <td>119.167.248.30</td>
      <td>21/Apr/2018</td>
      <td>22:53:01</td>
      <td></td>
      <td>GET</td>
      <td>/zh-cn/products002.html?proTypeID=70451&amp;proTyp...</td>
      <td>HTTP/1.1</td>
      <td>404</td>
      <td>11925</td>
      <td>-</td>
      <td>web spider/4.0(+http://www.sogou.com/docs/help...</td>
      <td>123.126.113.90</td>
      <td>0584a538269edabdfc104f5d898be8e4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13111473</td>
      <td>119.167.248.31</td>
      <td>21/Apr/2018</td>
      <td>22:53:01</td>
      <td></td>
      <td>GET</td>
      <td>/bid/zhaobiao-1309780.html</td>
      <td>HTTP/1.1</td>
      <td>200</td>
      <td>17255</td>
      <td>-</td>
      <td>web spider/4.0(+http://www.sogou.com/docs/help...</td>
      <td>106.38.241.174</td>
      <td>dda24ab33e0bfe31c8d83ee2f41bb0a3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13111472</td>
      <td>220.181.125.96</td>
      <td>21/Apr/2018</td>
      <td>22:53:01</td>
      <td></td>
      <td>GET</td>
      <td>/product/zhaoshang-1378457.html</td>
      <td>HTTP/1.1</td>
      <td>200</td>
      <td>28731</td>
      <td>-</td>
      <td>web spider/4.0(+http://www.sogou.com/docs/help...</td>
      <td>-</td>
      <td>e0f8350fa9ba3e4fa564d4969888e6ef</td>
    </tr>
  </tbody>
</table>
</div>




```python
help(pymysql.connections.Connection.__init__)
```

    Help on function __init__ in module pymysql.connections:
    
    __init__(self, host=None, user=None, password='', database=None, port=0, unix_socket=None, charset='', sql_mode=None, read_default_file=None, conv=None, use_unicode=None, client_flag=0, cursorclass=<class 'pymysql.cursors.Cursor'>, init_command=None, connect_timeout=10, ssl=None, read_default_group=None, compress=None, named_pipe=None, no_delay=None, autocommit=False, db=None, passwd=None, local_infile=False, max_allowed_packet=16777216, defer_connect=False, auth_plugin_map={}, read_timeout=None, write_timeout=None, bind_address=None, binary_prefix=False)
        Initialize self.  See help(type(self)) for accurate signature.
    
    
