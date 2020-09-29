import requests
from bs4 import BeautifulSoup


class Helper(object):
    session = None
    username = None
    password = None
    res = None

    def __init__(self, username='2017210146', password='05061971'):
        self.username = username
        self.password = password
        self.session = requests.Session()
        url = 'https://auth.bupt.edu.cn/authserver/login?service=http://order.bupt.edu.cn/loginall.aspx?page='
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
        data = {'username': username, 'password': password}
        r = self.session.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        v1 = soup.select("#casLoginForm > input:nth-child(5)")[0]['value']
        v2 = soup.select("#casLoginForm > input:nth-child(6)")[0]['value']
        v3 = soup.select("#casLoginForm > input:nth-child(7)")[0]['value']
        v4 = soup.select("#casLoginForm > input:nth-child(11)")[0]['value']
        data.update({'lt': v1, 'execution': v2, '_eventId': v3, 'rmShown': v4})
        self.res = self.session.post(url, headers=headers, data=data)


help_me = Helper()
print(help_me.res.text)


'''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <link rel="stylesheet"  type="text/css" href="js/jquery-ui.css" />
        <script type="text/javascript" src="/authserver/js/jquery.min.js"></script>
    <script type="text/javascript" src="/authserver/js/jquery-validation/jquery.validate.js"></script>
    <script type="text/javascript" src="/authserver/js/jquery-validation/messages_cn.js"></script>

<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="bupt/css/bootstrap.min.css" rel="stylesheet">
<link href="bupt/css/mystyle.css" rel="stylesheet">
<link href="bupt/css/auth.css" rel="stylesheet">
<!--[if lt IE 9]>
<script src="bupt/js/html5shiv.min.js"></script>
<script src="bupt/js/respond.min.js"></script>
<![endif]-->


<title>统一身份认证平台-北京邮电大学</title>
</head>

<body>

<div class="wbox logobox clearfix">
        <a class="logo pull-left" href=""><img src="bupt/images/logo.png" class="img-responsive"></a>
    <div class="searchbox pull-right">
                <div class="input-group">

                </div><!-- /input-group -->
        </div>
</div>

<div class="slidebox">
    <!--slide-->
    <div class="fullSlide">
                <div class="bd">
                        <ul class="list-unstyled">
                                <li style="background:url(bupt/images/banner1010.jpg) 20% 0 no-repeat;"></li>
                                <!-- <li style="background:url(bupt/images/banner1.jpg) 20% 0 no-repeat;"></li>
                                <li style="background:url(bupt/images/banner21.jpg) 20% 0 no-repeat;"></li>
                                <li style="background:url(bupt/images/banner31.jpg) 20% 0 no-repeat;"></li> -->
                        </ul>
                </div>
        </div>
    <!--slide--->

    <div class="regbox">
        <div class="wbox clearfix">
                <div class="loginbox">
                <h3>欢迎登录</h3>
                <form id="casLoginForm" class="fm-v clearfix" action="/authserver/login?service=http://order.bupt.edu.cn/loginall.aspx?page=" method="post">
                                        <!-- 密码错误信息 -->

                        <div class="userbox clearfix">
                        <div class="iconuser"></div>
                                                <input id="username" name="username" class="inputuser required" tabindex="1" placeholder="请输入学工号／手机号／邮箱" type="text" value=""
size="25" autocomplete="false"/>
                    </div>
                    <div class="userbox clearfix">
                        <div class="iconpass"></div>
                                                <input id="password" name="password" class="required inputuser" tabindex="2" placeholder="请输入密码" type="password" value="" size="25" au
tocomplete="off"/>
                    </div>
                                        <div id="casCaptcha" class="userbox clearfix hidden" style="margin:10px 0;">

                                        </div>

                    <div class="login-link">
                                                <span class="login-forpwd"><a href="#;" onclick="javascript:window.location.href='getBackPasswordMainPage.do'">忘记密码?</a></span>
                                                <span class="login-help"><a href="#;"  onclick="javascript:window.location.href='/authserver/loginHelp.jsp'">登录帮助</a></span>
                                        </div>

                                        <input type="hidden" name="lt" value="LT-2638367-lUSqPXFSXvJ5Bd9ZltUq70Zh0dSsjJ-1601391899436" />
                                        <input type="hidden" name="execution" value="e1s1" />
                                        <input type="hidden" name="_eventId" value="submit" />
                                        <input type="submit" value="立即登录" class="btnsubmit btn btn-primary btn-lg">
                                         <div style="display: none">
                                                <input id="warn" name="warn" value="true" tabindex="3" accesskey="w" type="checkbox" />
                                                <strong class="remember-label">
                                                        <span class="accesskey">W</span>arn me before logging me into other sites.
                                                </strong>
                                        </div>

                                        <label class="remember" onclick="">
                                                <a id="link-forgot-passwd" href="" target="_top"></a>
                                        </label>
                                        <input type="hidden" name="rmShown" value="1">
                </form>
            <a class="prevTheme" title="上一张"></a>
                        <a class="nextTheme" title="下一张"></a>
            </div>

        </div>
    </div>
<script type="text/javascript" src="js/cas-wisedu.js" ></script>

</div>

<div class="bgwhite pdtb45">
        <div class="wbox clearfix">
        <div class="groupgird group1">
                <h4>数字校园</h4>
            <p>数据互联互通，信息高度共享。</p>
        </div>
        <div class="groupgird group2">
                <h4>泛在校园</h4>
            <p>数据广泛获取，感知无处不在。</p>
        </div>
        <div class="groupgird group3">
                <h4>智慧校园</h4>
            <p>数据认知计算，服务持续创新。</p>
        </div>
        <!-- <div class="weixingird pull-left">
                移动校园IOS
            <div class="bgwechat">
                <img src="bupt/images/ios.jpg">
                <div class="wechatname">IOS版本</div>
            </div>
        </div>
        <div class="weixingird pull-right">
                移动校园Android
            <div class="bgwechat">
                <img src="bupt/images/android.jpg">
                <div class="wechatname">Android</div>
            </div>
        </div> -->
    </div>
</div>

<div class="copyright text-center bgeee">版权所有 &copy 北京邮电大学  地址:北京市西土城路10号  邮编:100876  京ICP备 05064445号 京公网安备110402430070</div>
<script type="text/javascript" src="/authserver/js/cas-wisedu.js"></script>
<script src="bupt/js/texiao.js"></script>
<script>
//jQuery(".fullSlide").slide({ titCell:".hd li", mainCell:".bd ul", effect:"fold",  autoPlay:true, delayTime:6400 });
jQuery(function(){
    var speed=4000;var i=parseInt(3*Math.random());
    jQuery(".fullSlide .bd li").width(jQuery(window).width())
    jQuery(".list-unstyled li").eq(i).show().siblings().hide();
    jQuery(".prevTheme").click(function(){
        i--;
        i<0?i=2:i=i;
        jQuery(".list-unstyled li").eq(i).fadeIn("slow").siblings().hide();

    })
    jQuery(".nextTheme").click(function(){
        i++;
        i>=3?i=0:i=i;
        jQuery(".list-unstyled li").eq(i).fadeIn("slow").siblings().hide();
    })
})
</script>
</body>
</html>
'''